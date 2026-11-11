
from base_conhecimento import BaseConhecimento
from assistente import Assistente


def iniciar():
    print("=" * 50)
    print("INICIANDO O PRIMEIRO PASSO")
    print("=" * 50)

    # Cria a base de conhecimento
    base = BaseConhecimento("data/base_conhecimento.json")

    # Carrega as orientações do arquivo JSON
    base.carregar()

    # Verifica se existem orientações disponíveis
    if not base.orientacoes:
        print("\nNão foi possível iniciar o assistente.")
        print("Verifique o arquivo base_conhecimento.json.")
        return

    # Cria o assistente e conecta à base de conhecimento
    assistente = Assistente("Jarvis", base)

    # Inicia o menu principal
    assistente.menu()


if __name__ == "__main__":
    iniciar()
