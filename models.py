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
        total = sum([c.nota for c in self.competencias]) 
        return total / len(self.competencias)


class Carreira:
    def __init__(self, nome, descricao): # Cada carreira tem um nome e uma descrição 
        self.nome = nome
        self.descricao = descricao

class TrilhaAprendizado: # A trilha de aprendizado consiste na previsa de conteúdos para o usuário estudar
    def __init__(self, nome, conteudos):
        self.nome = nome
        self.conteudos = conteudos  

    def exibir_trilha(self):
        print(f"\nTrilha sugerida: {self.nome}")
        print("Conteúdos recomendados:")
        for item in self.conteudos:
            print(f"- {item}")


class SistemaOrientacao:  # Sistema de orientação para organizar múltiplos perfis
    def __init__(self):
        self.perfis = [] 

    def adicionar_perfil(self, perfil):
        self.perfis.append(perfil)

    def listar_perfis(self):
        if not self.perfis:
            print("Nenhum perfil cadastrado ainda.")
        else:
            print("\nPerfis cadastrados:")
            for i, p in enumerate(self.perfis, start=1):
                print(f"{i}. {p.nome}")