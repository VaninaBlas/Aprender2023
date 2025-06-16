import unittest

# Importamos el codigo a testear.
from resumen import Resumen
from estudiante import Estudiante
####################################################################

class TestResumen(unittest.TestCase):

    def test_init_asigna_atributos(self):
        # verificar si el inicializador guarda bien los atributos
        e1:Estudiante=Estudiante("LPA", 690.87878, 498.328390, -2.839213, "Rural", "Privado")
        e2:Estudiante=Estudiante("FOR", 345.4499,233.2390,1.87699, "Rural", "Estatal")
        e3:Estudiante=Estudiante("ETR", 239.16500009,481.86500 ,0.2666,"Urbano","Estatal")
        e4:Estudiante=Estudiante("RNE", 420.45982, 234.92381, 0.212321, "Urbano", "Privado")
        e5:Estudiante=Estudiante("SFE", 156.34562, 311.34222, 0.232498, "Urbano", "Privado")
        r:Resumen=Resumen([e1,e2,e3,e4,e5])
        self.assertEqual(r.cantidad, 5)
        self.assertAlmostEqual(r.promedio_matematica, 370.459824018)
        self.assertAlmostEqual(r.promedio_lengua, 351.939684)
        self.assertAlmostEqual(r.promedio_nse, -0.050160800000000026)
        self.assertAlmostEqual(r.proporcion_ambito_rural, 0.4)
        self.assertAlmostEqual(r.proporcion_sector_estatal, 0.4)
        
        
####################################################################

unittest.main()
