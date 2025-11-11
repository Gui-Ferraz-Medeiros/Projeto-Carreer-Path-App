# Carreer Path App
Projeto desenvolvido para a disciplina de **Pensamento Computacional e Automação com Python**  para auxiliar pessoas que não necessariamente sejam da área de TI a encontrarem novos caminhos em busca de profissões futuras. A aplicação tem o intuito de expandir horizontes e talvez inspirar aqueles que possuem receio com a evolução das tecnologias e como elas afetam seu trabalho, o objetivo é expandir o leque de opções de emprego, e jamais limitá-las.
Professor: **Alexandre Russi Jr.**
Curso: **Ciência da Computação**

## Objetivo:
O sistema analisa o perfil de competências do usuário e recomenda uma **carreira do futuro** com base nas suas habilidades.  
Agora é possível **visualizar os resultados de cada perfil cadastrado individualmente**, além de cadastrar novos.

## Tecnologias:
- Python 3.13.2
- Estruturas condicionais, funções, programação orientada a objetos, listas e dicionários

## Estrutura do Projeto:
carrer_path_app/
|--main.py # Menu principal e lógica do sistema
|-- models.py # Local onde ficam as classes: Perfil, Competência, Carreira, TrilhaAprendizado e SistemaOrientacao
|-- utils.py # Funções auxiliares para recomendações

## Como Executar:
1. Abra o terminal e vá até a pasta do projeto.

2. Execute o comando:
   ```bash
   python main.py

3. Siga as opções do menu:
'''
    1 → Cadastrar novo perfil

    2 → Listar perfis cadastrados

    3 → Visualizar resultado de um perfil (ex: usuário nº 2)

    4 → Sair
'''
