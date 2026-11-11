
from base_conhecimento import BaseConhecimento
from assistente import Assistente


def iniciar():
    print("=" * 50)
    print("INICIANDO O PRIMEIRO PASSO")
    print("=" * 50)

    base = BaseConhecimento("data/base_conhecimento.json")

    base.carregar()

    if not base.orientacoes:
        print("\nNão foi possível iniciar o assistente.")
        print("Verifique o arquivo base_conhecimento.json.")
        return

    assistente = Assistente("Jarvis", base)

    assistente.menu()

if __name__ == "__main__":
    iniciar()
