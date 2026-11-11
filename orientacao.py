
class Orientacao:
    def __init__(
        self,
        id,
        categoria,
        titulo,
        palavras_chave,
        resposta,
        documentos,
        onde,
        fonte,
        verificado_em
    ):
        self.id = id
        self.categoria = categoria
        self.titulo = titulo
        self.palavras_chave = palavras_chave
        self.resposta = resposta
        self.documentos = documentos
        self.onde = onde
        self.fonte = fonte
        self.verificado_em = verificado_em

    def exibir(self):
        print("\n" + "=" * 50)
        print(self.titulo)
        print("=" * 50)

        print("\nResposta:")
        print(self.resposta)

        print("\nDocumentos necessários:")
        if self.documentos:
            for documento in self.documentos:
                print(f"- {documento}")
        else:
            print("Nenhum documento específico necessário.")

        print("\nOnde encontrar:")
        print(self.onde)

        print("\nFonte:")
        print(self.fonte)

        print(f"\nInformação verificada em: {self.verificado_em}")

        print("\nAtenção: este assistente não é um canal oficial.")
        print("=" * 50)
