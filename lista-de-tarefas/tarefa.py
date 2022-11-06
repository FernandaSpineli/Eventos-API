# TEST DRIVEN DEVELOPMENT
class Tarefa:
    def __init__(self, titulo, descricao='', data=None, notificacao=None):
        self.titulo= titulo
        self.descricao = descricao
        self.data = data
        self.notificacao = notificacao
        self.concluida = False
        
    def concluir(self):
        self.concluida = True
    
    def adicionar_descricao(self, descricao):
        pass
    
    def adiar_notificacao(self, minutos):
        pass
    
    def atrasada(self):
        pass
    
