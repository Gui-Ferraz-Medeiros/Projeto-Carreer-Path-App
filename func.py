# Funções auxiliares do sistema

from models import Carreira

def gerar_recomendacao(perfil):
    media = perfil.calcular_media() # Calcula a média das competências contidas no perfil

    # Regras simples baseadas na média de competências
    if media >= 8:
        carreira = Carreira(
            "Cientista de Dados",
            "Profissional que analisa grandes volumes de dados para gerar insights estratégicos."
        )
    elif media >= 6:
        carreira = Carreira(
            "Desenvolvedor de Software",
            "Profissional que cria soluções digitais e sistemas inteligentes."
        )
    elif media >= 4:
        carreira = Carreira(
            "Designer Digital",
            "Profissional focado em criatividade e experiência do usuário."
        )
    else:
        carreira = Carreira(
            "Assistente de Tecnologia",
            "Profissional em início de jornada, desenvolvendo competências básicas para o futuro digital."
        )

    return carreira