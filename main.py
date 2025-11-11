# Arquivo principal do app Carreer Path, é onde mostra o menu CLI e chama as funções principais

from models import Perfil, SistemaOrientacao
from func import gerar_recomendacao

def exibir_menu():
    print("\n===== Carreer Path App =====")
    print("1 - Cadastrar novo perfil")
    print("2 - Listar perfis cadastrados")
    print("3 - Visualizar resultado de um perfil")
    print("4 - Sair")
    print("=================================")


def cadastrar_perfil(sistema):
    nome = input("Digite seu nome: ")
    perfil = Perfil(nome)

    print("\nAvalie suas competências de 0 a 10:")
    competencias = ["Lógica", "Criatividade", "Colaboração", "Adaptabilidade", "Comunicação"]

    for comp in competencias:
        while True:
            try:
                nota = float(input(f"{comp}: "))
                if 0 <= nota <= 10:
                    perfil.adicionar_competencia(comp, nota)
                    break
                else:
                    print("Digite um valor entre 0 e 10.")
            except ValueError:
                print("Por favor, digite um número válido.")

    sistema.adicionar_perfil(perfil)
    print(f"\nPerfil '{perfil.nome}' cadastrado com sucesso!")


def visualizar_resultado(perfil):
    carreira, trilha = gerar_recomendacao(perfil)

    print("\n===== RESULTADO =====")
    print(f"Nome: {perfil.nome}")
    print(f"Média geral: {perfil.calcular_media():.2f}")
    print(f"Carreira recomendada: {carreira.nome}")
    print(f"Descrição: {carreira.descricao}")
    trilha.exibir_trilha()
    print("======================")


def escolher_perfil(sistema):
    if not sistema.perfis:
        print("Nenhum perfil cadastrado ainda.")
        return

    print("\nPerfis disponíveis:")
    for i, perfil in enumerate(sistema.perfis, start=1):
        print(f"{i}. {perfil.nome}")

    try:
        escolha = int(input("Digite o número do perfil que deseja visualizar: "))
        if 1 <= escolha <= len(sistema.perfis):
            perfil_escolhido = sistema.perfis[escolha - 1]
            visualizar_resultado(perfil_escolhido)
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")


# Programa principal
if __name__ == "__main__":
    sistema = SistemaOrientacao()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_perfil(sistema)
        elif opcao == "2":
            sistema.listar_perfis()
        elif opcao == "3":
            escolher_perfil(sistema)
        elif opcao == "4":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")