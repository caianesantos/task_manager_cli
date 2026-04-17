class Tarefa:
    def __init__(self, titulo, descricao=''):
        self.titulo = titulo
        self.descricao = descricao
        self.concluido = False

class Lista_tarefas: 
    def __init__(self):
        self.tarefas=[]

gerenciador = Lista_tarefas()

#def adicionar_tarefa():
titulo_tarefa = input("Digite o título da tarefa: ")
descricao_tarefa = input("Digite a descrição da tarefa: ")

nova_tarefa = Tarefa(titulo_tarefa, descricao_tarefa)

gerenciador.tarefas.append(nova_tarefa)
       