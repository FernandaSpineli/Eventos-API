from eventos import Evento

class EventoOnline(Evento):
    def __init__(self, nome, _=""):
        local = f"https://tamarcado.com/evento?id={Evento.id}"
        super().__init__(nome, local)
    
    def imprime_informacoes(self):
        print(f'ID do evento: {self.id}')
        print(f'nome do evento: {self.nome}')
        print(f'link para acessar o evento: {self.local}')
        print("============================")
        