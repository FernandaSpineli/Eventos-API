class ListaDeTarefas:
    def __init__(self):
        self._tarefas = []
        self._quantidade_tarefas = 0
        
    def adicionar_tarefa(self, tarefa):
        self._tarefas.append(tarefa)
    
    def get_tarefas(self, incluir_concluidas=False):
        tarefas_nao_concluidas = []
        for tarefa in self._tarefas:
            if not tarefa.concluida:
                tarefas_nao_concluidas.append(tarefa)
        return tarefas_nao_concluidas
    