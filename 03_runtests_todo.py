import unittest
import requests
import random


def get_random_string(length):
    letters = 'abcdefghijklmnopqrstuvxzwyk'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

class TestStringMethods(unittest.TestCase):

    def test_01_urls(self):
        r1 = requests.get("http://localhost:5000/todo/impacta/flask")
        if r1.status_code != 200:
            self.fail("nao achei nada na url /todo/impacta/flask. Ela deveria estar disponivel")
        r2 = requests.get("http://localhost:5000/todo/impacta/banana")
        if r2.status_code != 200:
            self.fail("nao achei nada na url /todo/impacta/banana. Ela deveria estar disponivel")
        string_aleatoria = get_random_string(8)
        r3 = requests.get(f"http://localhost:5000/todo/bradesco/{string_aleatoria}")
        if r3.status_code != 200:
            self.fail(f"nao achei nada na url /todo/bradesco/{string_aleatoria}. Ela deveria estar disponivel. Note que a string foi gerada aleatoriamente")

    def test_02a_add_com_get(self):
        r1 = requests.get("http://localhost:5000/todo/impacta/flask?item=rotas sao de boa")
        if r1.status_code != 200:
            self.fail("nao consegui salvar uma msg em /todo/impacta/flask usando GET")
        if 'rotas' not in r1.text:
            self.fail("Enviei uma msg em /todo/impacta/flask, mas o texto nao apareceu")
        if 'vitamina' in r1.text:
            self.fail("estranho, um texto que eu nao enviei apareceu em /todo/impacta/flask")
    
    def test_02b_add_com_get(self):
        r1 = requests.get("http://localhost:5000/todo/impacta/covid?item=vitamina d")
        if r1.status_code != 200:
            self.fail("nao consegui salvar uma msg em /todo/impacta/flask usando GET")
        if 'vitamina' not in r1.text:
            self.fail("Enviei uma msg em /todo/impacta/flask, mas o texto nao apareceu")
        if 'rotas' in r1.text:
            self.fail("estranho, um texto que eu nao enviei apareceu em /todo/impacta/flask")
    
    def test_02c_add_com_get(self):
        sala_aleatoria = get_random_string(8)
        r2 = requests.get(f"http://localhost:5000/todo/bancodobrasil/{sala_aleatoria}?item=vitamina d")
        if r2.status_code != 200:
            self.fail(f"nao consegui salvar uma msg na url /todo/bancodobrasil/{sala_aleatoria}. Essa url deveria estar disponivel. Note que a string foi gerada aleatoriamente")
        if 'vitamina' not in r2.text:
            self.fail(f"Enviei um item de todo na url /chat/{sala_aleatoria}, mas o texto nao apareceu")
        if 'rota' in r2.text:
            self.fail(f"estranho, um texto que eu nao enviei apareceu na url /chat/{sala_aleatoria}")

    def test_03a_add_com_post(self):
        sala_aleatoria = get_random_string(8)
        r2 = requests.post(f"http://localhost:5000/todo/bancodobrasil/{sala_aleatoria}", data={"item":"gato felix"})
        if r2.status_code != 200:
            self.fail(f"nao consegui salvar uma msg na url /todo/bancodobrasil/{sala_aleatoria}. Essa url deveria estar disponivel. Note que a string foi gerada aleatoriamente")
        if 'vitamina' in r2.text:
            self.fail(f"estranho, um texto que eu nao enviei apareceu na url /todo/bancodobrasil/{sala_aleatoria}")
        if 'rota' in r2.text:
            self.fail(f"estranho, um texto que eu nao enviei apareceu na url /todo/bancodobrasil/{sala_aleatoria}")
        if 'gato' not in r2.text:
            self.fail(f"Enviei uma msg na url /todo/bancodobrasil/{sala_aleatoria}, mas o texto nao apareceu")

    def test_04_empresas_validas(self):
        sala_aleatoria = get_random_string(8)
        r2 = requests.post(f"http://localhost:5000/todo/bancodobrasil/{sala_aleatoria}", data={"item":"gato felix"})
        if r2.status_code != 200:
            self.fail(f"nao consegui salvar uma msg na url /todo/bancodobrasil/{sala_aleatoria}. Essa url deveria estar disponivel. Note que a string foi gerada aleatoriamente")
        r3 = requests.post(f"http://localhost:5000/todo/impacta/{sala_aleatoria}", data={"item":"gato felix"})
        if r3.status_code != 200:
            self.fail(f"nao consegui salvar uma msg na url /todo/impacta/{sala_aleatoria}. Essa url deveria estar disponivel. Note que a string foi gerada aleatoriamente")
        r4 = requests.post(f"http://localhost:5000/todo/ventiladores_do_joao/{sala_aleatoria}", data={"item":"gato felix"})
        if r4.status_code == 200:
            self.fail(f"tentei salvar um todo numa empresa não pagante, e deu certo")

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()