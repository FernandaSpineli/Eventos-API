import unittest

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
        

unittest.main()