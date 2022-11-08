import unittest
from datetime import datetime

from tarefa import Tarefa


class TestConcluir(unittest.TestCase):
    def test_concluir_tarefa_altera_concluido_para_true(self):
        tarefa = Tarefa('Estudar Python')
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
        
    def test_concluir_tarefa_concluida_continua_true(self):
        tarefa = Tarefa('Estudar Python')
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
       
   
class TestAdicionarDescricao(unittest.TestCase):
    def test_adicionar_descricao_da_tarefa(self):
        tarefa = Tarefa('Criar APP')
        descricao = 'criar aplicativo para android'
        tarefa.adicionar_descricao(descricao)
        self.assertEqual(tarefa.descricao, descricao)
       
       
class TestNotificacao(unittest.TestCase):
    def test_adia_notificacao_em_X_minutos(self):
        dt_original = datetime(2022, 11, 6, 9, 10) # year, month, day, hour, minute, second, millisecond
        tarefa = Tarefa('Estudar Python', notificacao= dt_original)
        tarefa.adiar_notificacao(15)
         
        dt_esperado = datetime(2022, 11, 6, 9, 25)
        self.assertEqual(tarefa.notificacao, dt_esperado)


class TestAtrasada(unittest.TestCase):
    def test_dizer_se_tarefa_esta_atrasada(self):
        tarefa = Tarefa('Criar APP')
        tarefa.data = datetime(2022, 11, 6, 9, 10)
        self.assertEqual(tarefa.atrasada(), 'está atrasada')


unittest.main()