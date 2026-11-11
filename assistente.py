import os
import json
import csv
import re
import time

from datetime import datetime

class Assistente:
    def __init__(self, nome, base):
        self.nome = nome
        self.base = base
        self.historico = []

        self.caminho_historico = "data/historico.json"
        self.carregar_historico()

    def carregar_historico(self):
        try:
            with open(self.caminho_historico, "r", encoding="utf-8") as arquivo:
                self.historico = json.load(arquivo)

            if not isinstance(self.historico, list):
                self.historico = []

        except FileNotFoundError:
            self.historico = []

        except json.JSONDecodeError:
            print("Aviso: o histórico está inválido. Um novo histórico será iniciado.")
            self.historico = []

    def salvar_historico(self):
        os.makedirs("data", exist_ok=True)

        with open(self.caminho_historico, "w", encoding="utf-8") as arquivo:
            json.dump(
                self.historico,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

    def contem_dado_pessoal(self, texto):
        possui_numero_longo = re.search(r"\d{8,}", texto)
        possui_email = "@" in texto

        return bool(possui_numero_longo or possui_email)

    def registrar(
        self,
        origem,
        pergunta,
        id_orientacao,
        encontrou,
        ajudou,
        tentativas,
        tempo_segundos
    ):
        atendimento = {
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "origem": origem,
            "pergunta": pergunta,
            "id_orientacao": id_orientacao,
            "encontrou": encontrou,
            "ajudou": ajudou,
            "tentativas": tentativas,
            "tempo_segundos": round(tempo_segundos, 1)
        }

        self.historico.append(atendimento)
        self.salvar_historico()

    def perguntar(self):
        inicio = time.time()
        tentativas = 0

        print("\n" + "=" * 50)
        print("COMO POSSO AJUDAR?")
        print("Digite sua dúvida sobre o primeiro emprego.")
        print("Digite 0 para voltar ao menu.")
        print("=" * 50)

        while True:
            pergunta = input("\nSua pergunta: ").strip()

            if pergunta == "0":
                return

            if not pergunta:
                print("Digite uma pergunta para continuar.")
                continue

            if self.contem_dado_pessoal(pergunta):
                print("\nPor segurança, não informe dados pessoais.")
                print("Não envie números com 8 ou mais dígitos nem endereços de e-mail.")
                print("Sua pergunta não foi registrada.")
                return

            tentativas += 1

            resultados = self.base.buscar(pergunta)

            if resultados:
                pontos, melhor_orientacao = resultados[0]

                if pontos >= 6:
                    confianca = "ALTA"
                else:
                    confianca = "MÉDIA"

                print("\nOrientação encontrada!")
                print(f"Confiança da busca: {confianca}")

                melhor_orientacao.exibir()

                alternativas = resultados[1:3]

                if alternativas:
                    print("\nOutras orientações relacionadas:")

                    for pontos_alternativa, orientacao in alternativas:
                        print(f"- {orientacao.titulo} ({pontos_alternativa} pontos)")

                id_orientacao = melhor_orientacao.id
                encontrou = True

                resposta_util = input(
                    "\nEssa orientação ajudou? (s/n): "
                ).strip().lower()

                ajudou = resposta_util == "s"

                tempo = time.time() - inicio

                self.registrar(
                    origem="pergunta",
                    pergunta=pergunta,
                    id_orientacao=id_orientacao,
                    encontrou=encontrou,
                    ajudou=ajudou,
                    tentativas=tentativas,
                    tempo_segundos=tempo
                )

                print("\nObrigado por utilizar o Primeiro Passo!")
                return

            else:
                print("\nNão encontrei uma orientação adequada para essa pergunta.")
                print("Tente utilizar outras palavras ou consultar uma categoria.")

                continuar = input(
                    "\nDeseja tentar novamente? (s/n): "
                ).strip().lower()

                if continuar != "s":
                    tempo = time.time() - inicio

                    self.registrar(
                        origem="pergunta",
                        pergunta=pergunta,
                        id_orientacao=None,
                        encontrou=False,
                        ajudou=False,
                        tentativas=tentativas,
                        tempo_segundos=tempo
                    )

                    return

    def navegar(self):
        inicio = time.time()

        categorias = self.base.categorias()

        if not categorias:
            print("\nNão existem categorias disponíveis.")
            return

        while True:
            print("\n" + "=" * 50)
            print("CONSULTAR POR CATEGORIA")
            print("=" * 50)

            for numero, categoria in enumerate(categorias, start=1):
                print(f"{numero} - {categoria}")

            print("0 - Voltar ao menu")

            escolha = input("\nEscolha uma categoria: ").strip()

            if escolha == "0":
                return

            if not escolha.isdigit():
                print("Digite um número válido.")
                continue

            numero = int(escolha)

            if numero < 1 or numero > len(categorias):
                print("Categoria inválida. Tente novamente.")
                continue

            categoria_escolhida = categorias[numero - 1]
            orientacoes = self.base.por_categoria(categoria_escolhida)

            while True:
                print(f"\nCategoria: {categoria_escolhida}")

                for indice, orientacao in enumerate(orientacoes, start=1):
                    print(f"{indice} - {orientacao.titulo}")

                print("0 - Voltar às categorias")

                opcao = input("\nEscolha uma orientação: ").strip()

                if opcao == "0":
                    break

                if not opcao.isdigit():
                    print("Digite um número válido.")
                    continue

                indice = int(opcao)

                if indice < 1 or indice > len(orientacoes):
                    print("Orientação inválida. Tente novamente.")
                    continue

                orientacao_escolhida = orientacoes[indice - 1]
                orientacao_escolhida.exibir()

                resposta_util = input(
                    "\nEssa orientação ajudou? (s/n): "
                ).strip().lower()

                ajudou = resposta_util == "s"
                tempo = time.time() - inicio

                self.registrar(
                    origem="categoria",
                    pergunta=f"Consulta pela categoria: {categoria_escolhida}",
                    id_orientacao=orientacao_escolhida.id,
                    encontrou=True,
                    ajudou=ajudou,
                    tentativas=1,
                    tempo_segundos=tempo
                )

    def indicadores(self):
        atendimentos = [
            registro for registro in self.historico
            if registro["origem"] != "avaliacao"
        ]

        if not atendimentos:
            print("\nAinda não existem atendimentos registrados.")
            return

        total = len(atendimentos)

        encontrados = sum(
            1 for registro in atendimentos
            if registro["encontrou"]
        )

        ajudaram = sum(
            1 for registro in atendimentos
            if registro["ajudou"] is True
        )

        tempo_medio = sum(
            registro["tempo_segundos"] for registro in atendimentos
        ) / total

        tentativas_media = sum(
            registro["tentativas"] for registro in atendimentos
        ) / total

        percentual_encontrado = (encontrados / total) * 100
        percentual_ajudou = (ajudaram / total) * 100

        avaliacoes = [
            registro["facilidade"]
            for registro in self.historico
            if registro["origem"] == "avaliacao"
        ]

        print("\n" + "=" * 50)
        print("INDICADORES DO PRIMEIRO PASSO")
        print("=" * 50)

        print(f"Total de atendimentos: {total}")
        print(f"Orientações encontradas: {percentual_encontrado:.1f}%")
        print(f"Atendimentos que ajudaram: {percentual_ajudou:.1f}%")
        print(f"Tempo médio: {tempo_medio:.1f} segundos")
        print(f"Média de tentativas: {tentativas_media:.1f}")

        if avaliacoes:
            media_facilidade = sum(avaliacoes) / len(avaliacoes)
            print(f"Facilidade de uso: {media_facilidade:.1f}/5")
        else:
            print("Facilidade de uso: ainda sem avaliações.")

        print("\nPerguntas não resolvidas:")

        nao_encontradas = [
            registro["pergunta"]
            for registro in atendimentos
            if not registro["encontrou"]
        ]

        if nao_encontradas:
            for pergunta in nao_encontradas:
                print(f"- {pergunta}")
        else:
            print("Nenhuma pergunta não resolvida.")

        print("=" * 50)

    def exportar_csv(self):
        os.makedirs("data", exist_ok=True)

        caminho_csv = "data/atendimentos.csv"

        colunas = [
            "data",
            "origem",
            "pergunta",
            "id_orientacao",
            "encontrou",
            "ajudou",
            "tentativas",
            "tempo_segundos",
            "facilidade"
        ]

        with open(caminho_csv, "w", newline="", encoding="utf-8-sig") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=colunas)

            escritor.writeheader()

            for registro in self.historico:
                escritor.writerow(registro)

        print(f"\nAtendimentos exportados para: {caminho_csv}")

    def avaliar_facilidade(self):
        while True:
            resposta = input(
                "\nDe 1 a 5, quão fácil foi utilizar o assistente? "
            ).strip()

            if resposta in ["1", "2", "3", "4", "5"]:
                avaliacao = {
                    "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "origem": "avaliacao",
                    "pergunta": "Avaliação geral da facilidade de uso",
                    "id_orientacao": None,
                    "encontrou": None,
                    "ajudou": None,
                    "tentativas": 0,
                    "tempo_segundos": 0,
                    "facilidade": int(resposta)
                }

                self.historico.append(avaliacao)
                self.salvar_historico()
                print("Obrigado pela avaliação!")
                return

            print("Digite somente um número entre 1 e 5.")

    def menu(self):
        print("\nBem-vindo ao Primeiro Passo!")
        print("Seu assistente de orientação para o primeiro emprego.")

        while True:
            print("\n" + "=" * 50)
            print("MENU PRINCIPAL")
            print("=" * 50)
            print("1 - Fazer uma pergunta")
            print("2 - Consultar por categoria")
            print("3 - Ver indicadores")
            print("4 - Exportar atendimentos para CSV")
            print("0 - Encerrar")
            print("=" * 50)

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.perguntar()

            elif opcao == "2":
                self.navegar()

            elif opcao == "3":
                self.indicadores()

            elif opcao == "4":
                self.exportar_csv()

            elif opcao == "0":
                self.avaliar_facilidade()
                print("\nObrigado por utilizar o Primeiro Passo!")
                print("Até a próxima!")
                break

            else:
                print("Opção inválida. Escolha uma opção do menu.")
