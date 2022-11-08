# TEST DRIVEN DEVELOPMENT
from datetime import datetime, timedelta


class Tarefa:
    def __init__(self, titulo, descricao='', data=None, notificacao=None):
        self.titulo= titulo
        self.descricao = descricao
        self.data = data
        self.notificacao = notificacao
        self.concluida = False
        
    def concluir(self):
        self.concluida = True
    
    def adicionar_descricao(self, nova_descricao):
        self.descricao = nova_descricao
    
    def adiar_notificacao(self, minutos):
        if self.notificacao is None:
            return
        
        nova_notificacao = self.notificacao + timedelta(minutes=minutos)
        self.notificacao = nova_notificacao
        
    def atrasada(self):
        if self.data != None:
            if self.data < datetime.now():
                return 'está atrasada'
    
