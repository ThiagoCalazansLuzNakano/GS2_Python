import json
import re
import unicodedata

from orientacao import Orientacao

class BaseConhecimento:
    def __init__(self, caminho):
        self.caminho = caminho
        self.orientacoes = []

    def normalizar(self, texto):
        texto = texto.lower().strip()

        texto = unicodedata.normalize("NFD", texto)
        texto = "".join(
            caractere for caractere in texto
            if unicodedata.category(caractere) != "Mn"
        )

        texto = re.sub(r"[^a-z0-9\s]", " ", texto)
        texto = re.sub(r"\s+", " ", texto)

        return texto

    def carregar(self):
        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            if not isinstance(dados, list):
                print("Erro: a base de conhecimento deve ser uma lista.")
                self.orientacoes = []
                return

            self.orientacoes = []

            for registro in dados:
                if not isinstance(registro, dict):
                    continue

                try:
                    orientacao = Orientacao(
                        id=registro["id"],
                        categoria=registro["categoria"],
                        titulo=registro["titulo"],
                        palavras_chave=registro["palavras_chave"],
                        resposta=registro["resposta"],
                        documentos=registro["documentos"],
                        onde=registro["onde"],
                        fonte=registro["fonte"],
                        verificado_em=registro["verificado_em"]
                    )

                    self.orientacoes.append(orientacao)

                except (KeyError, TypeError) as erro:
                    print(f"Orientação ignorada por erro nos dados: {erro}")

            print(f"Base carregada: {len(self.orientacoes)} orientações.")

        except FileNotFoundError:
            print("Aviso: arquivo da base de conhecimento não encontrado.")
            self.orientacoes = []

        except json.JSONDecodeError:
            print("Aviso: o arquivo JSON está com formato inválido.")
            self.orientacoes = []

        except OSError as erro:
            print(f"Erro ao acessar a base de conhecimento: {erro}")
            self.orientacoes = []

    def categorias(self):
        lista_categorias = {
            orientacao.categoria
            for orientacao in self.orientacoes
        }

        return sorted(lista_categorias)

    def por_categoria(self, categoria):
        return [
            orientacao
            for orientacao in self.orientacoes
            if orientacao.categoria == categoria
        ]

    def pontuar(self, pergunta, orientacao):
        pergunta_normalizada = self.normalizar(pergunta)
        titulo_normalizado = self.normalizar(orientacao.titulo)

        pontos = 0

        for palavra_chave in orientacao.palavras_chave:
            palavra_normalizada = self.normalizar(palavra_chave)

            if palavra_normalizada in pergunta_normalizada:
                pontos += 3

        palavras_pergunta = set(pergunta_normalizada.split())
        palavras_titulo = set(titulo_normalizado.split())

        for palavra in palavras_pergunta:
            if len(palavra) >= 4 and palavra in palavras_titulo:
                pontos += 1

        return pontos

    def buscar(self, pergunta):
        resultados = []

        for orientacao in self.orientacoes:
            pontos = self.pontuar(pergunta, orientacao)

            if pontos >= 3:
                resultados.append((pontos, orientacao))

        resultados.sort(key=lambda resultado: resultado[0], reverse=True)

        return resultados
