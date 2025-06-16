import unittest

# Importamos el codigo a testear.
from pais import Pais

####################################################################

class TestPais(unittest.TestCase):
# si hago un test entonces debo saber el output, eso cambia dependiendo el dataset
#
    def test_first(self):
        self.assertEqual(resumen_provincia())

## y así con el resto de los métodos a testear.
        
####################################################################

unittest.main()
