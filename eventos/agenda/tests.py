from django.test import TestCase, Client


class TestPaginaInicial(TestCase):
    def test_lista_eventos(self):
        client = Client()
        response = client.get('/')
        #self.assertContains(response, "<th>Nome</th>")
        self.assertTemplateUsed(response, 'agenda/listar_eventos.html')