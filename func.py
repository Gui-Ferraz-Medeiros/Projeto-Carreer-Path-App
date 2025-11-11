# Funções auxiliares do sistema

from models import Carreira, TrilhaAprendizado

def gerar_recomendacao(perfil):
    media = perfil.calcular_media() # Calcula a média das competências contidas no perfil

    # Escolher carreira e trilha com base na média
    if media >= 8:
        carreira = Carreira(
            "Cientista de Dados",
            "Analisa grandes volumes de dados e cria soluções baseadas em IA."
        )
        trilha = TrilhaAprendizado(
            "Trilha de Ciência de Dados",
            ["Python Avançado", "Estatística", "Machine Learning", "SQL", "Power BI"]
        )

    elif media >= 6:
        carreira = Carreira(
            "Desenvolvedor de Software",
            "Cria aplicações e sistemas para diferentes plataformas."
        )
        trilha = TrilhaAprendizado(
            "Trilha de Desenvolvimento",
            ["Lógica de Programação", "Estruturas de Dados", "Banco de Dados", "APIs"]
        )

    elif media >= 4:
        carreira = Carreira(
            "Designer Digital",
            "Foca na criação de interfaces e experiências visuais."
        )
        trilha = TrilhaAprendizado(
            "Trilha de Design e UX",
            ["Design Thinking", "Figma", "Prototipagem", "Usabilidade"]
        )

    else:
        carreira = Carreira(
            "Assistente de Tecnologia",
            "Profissional iniciante que está aprendendo fundamentos digitais."
        )
        trilha = TrilhaAprendizado(
            "Trilha de Fundamentos",
            ["Introdução à Informática", "Lógica Básica", "Ferramentas Digitais"]
        )

    return carreira, trilha