# Arquivo principal do app Carreer Path, é onde mostra o menu CLI e chama as funções principais

from models import Perfil
from func import gerar_recomendacao

def exibir_menu():
    print("\n===== Carrer Path app =====")
    print("1 - Cadastrar novo perfil")
    print("2 - Sair")
    print("=================================")


def cadastrar_perfil():
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

    carreira = gerar_recomendacao(perfil)

    print("\n===== RESULTADO =====")
    print(f"Nome: {perfil.nome}")
    print(f"Média geral: {perfil.calcular_media():.2f}")
    print(f"Carreira recomendada: {carreira.nome}")
    print(f"Descrição: {carreira.descricao}")
    print("======================")


# Programa principal
if __name__ == "__main__": 
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_perfil()
        elif opcao == "2":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
