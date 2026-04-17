class Tarefa:
    def __init__(self, titulo, descricao=''):
        self.titulo = titulo
        self.descricao = descricao
        self.concluido = False

    def __str__(self):
        if self.descricao == "":
            return f" título: {self.titulo}" 
        else:
            return f" título: {self.titulo}\n Descrição: {self.descricao}"

class Lista_tarefas: 
    tarefas=[]

gerenciador = Lista_tarefas()

#def adicionar_tarefa():
titulo_tarefa = input("Digite o título da tarefa: ")
descricao_tarefa = input("Digite a descrição da tarefa: ")

nova_tarefa = Tarefa(titulo_tarefa, descricao_tarefa)

gerenciador.tarefas.append(nova_tarefa)

for tarefas in gerenciador.tarefas:
    print(tarefas)
       