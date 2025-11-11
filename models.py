# Aqui ficam as classes que representam os dados da aplicação

class Competencia:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota


class Perfil:
    def __init__(self, nome):
        self.nome = nome
        self.competencias = []  # Lista de objetos: "Competencia"

    def adicionar_competencia(self, nome, nota): # Adiciona uma competência ao perfil (atribuido ao nome; atribuindo uma nota àquela competência)
        self.competencias.append(Competencia(nome, nota))

    def calcular_media(self):
        if not self.competencias: # Se não houver nenhuma competência, retorna 0 
            return 0
        total = sum([c.nota for c in self.competencias]) # "c" é cada competência na lista de competências
        return total / len(self.competencias)


class Carreira:
    def __init__(self, nome, descricao): # Cada carreira tem um nome e uma descrição 
        self.nome = nome
        self.descricao = descricao