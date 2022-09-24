import random
import string
import datetime
from django.test import TestCase
from app_movies.models import Genero
from app_movies.models import Titulo


# Test 1: Comprobar si se puede crear un el nombre de un genero con letras random
class GeneroTestCase(TestCase):
   
    def test_creacion_genero(self):
        
        lista_letras_genero = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        print(lista_letras_genero)
        genero_prueba = "".join(lista_letras_genero)
        print(genero_prueba)
        genero_1 = Genero.objects.create(genero=genero_prueba)
               
        self.assertIsNotNone(genero_1.id)
        self.assertEqual(genero_1.genero, genero_prueba)
        print(genero_1.genero)


# Test 2: Una vez realizado el registro, debería llevarnos a la página de inicio

# Test 3: Comprobar si se puede crear una fecha de un año de lanzamiento con fecha random



