     #[classe]
class Estudante:
    escola = "Dio" # mudar a variavel de classe mudara para todas as instancias

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero # mudar a variavel de instancia ira alterar apenas a instancia citada

    def __str__(self):
        return f"{self.nome} - ({self.numero}) - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

#         [Classe]
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Raissa", 2)
    
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Rosinha" # variavel de classe   "ESCOLA" se for utilizado estudante mudará a classe e se for utilizado nome modificara a instancia
aluno_1.numero = 3 # variavel de instancia "NUMERO"(MATRICULA DO ALUNO)

mostrar_valores(aluno_1, aluno_2)



