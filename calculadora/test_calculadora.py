import unittest

from calculadora import somar, dividir, multiplicar, subtrair
   
class TestSomar(unittest.TestCase):
    def test_soma_dois_numeros_inteiros(self):
        self.assertEqual(somar(2, 4), 6)

    def test_soma_numero_com_zero(self):
        self.assertEqual(somar(2, 0), 2)


class TestDividir(unittest.TestCase):
    def test_divide_numero_por_um(self):
        self.assertEqual(dividir(4, 1), 4)
        
    def test_divide_numero_por_zero(self):
        self.assertEqual(dividir(6, 0), 'Não é um número')
        
             
class TestMultiplicar(unittest.TestCase):
    def test_multiplica_numero_ordem_inversa(self):
        self.assertEqual(multiplicar(2, 3), multiplicar(3, 2))

    def test_multiplica_numero_por_zero(self):
        self.assertEqual(multiplicar(5,0), 0)
        
    def test_multiplica_numero_por_um(self):
        self.assertEqual(multiplicar(4, 1), 4)


class TestSubtrair(unittest.TestCase):
    def test_subtrai_numero_por_numero_negativo(self):
        self.assertEqual(subtrair(2, -2), 4)
    
    def test_subtrai_dois_numeros_inteiros(self):
        self.assertEqual(subtrair(20, 5), 15)


unittest.main()