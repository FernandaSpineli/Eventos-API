class Tarefa:
    def __init__(self, titulo, descricao='', data=None, notificacao=None, concluida=False):
        self.titulo= titulo
        self.descricao = descricao
        self.data = data
        self.notificacao = notificacao
        self.concluida = concluida
        
    def concluir(self):
        pass
    
    def adicionar_descricao(self, descricao):
        pass
    
    def adiar_notificacao(self, minutos):
        pass
    
    def atrasada(self):
        pass
    
