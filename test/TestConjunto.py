import unittest
from src.LOGICA.conjunto import  Conjunto

class TestConjunto( unittest.TestCase ):
    def test_conjunto_vacio_retornaNone( self ):
        conjunto=Conjunto([])
        self.assertIsNone(conjunto.promedio())