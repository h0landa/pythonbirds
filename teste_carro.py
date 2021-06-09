from unittest import TestCase

from oo.carro import Motor

class CarroTestCase(TestCase):
    def velocidade_inicial_teste(self):
         motor = Motor()
         self.assertEqual(0, motor.velocidade)