import unittest

from tarefa import Tarefa
from lista_de_tarefas import ListaDeTarefas

class TestAdicionarTarefa(unittest.TestCase):
    def test_adiciona_tarefa_na_lista_de_tarefas(self):
        tarefa = Tarefa('Tarefa Teste')
        lista = ListaDeTarefas()
        lista.adicionar_tarefa(tarefa)
        
        #self.assertEqual(lista.get_tarefas()[0], tarefa)
        self.assertIn(tarefa, lista.get_tarefas())

class TestGetTarefas(unittest.TestCase):
    def test_retorna_lista_de_tarefas_adicionadas(self):
        tarefa_um = Tarefa('Tarefa Teste')
        tarefa_dois = Tarefa('Tarefa Teste dois')
        lista = ListaDeTarefas()
        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)
        
        self.assertEqual(lista.get_tarefas(), [tarefa_um, tarefa_dois])

unittest.main()