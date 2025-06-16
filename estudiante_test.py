import unittest

# Importamos el codigo a testear.
from estudiante import Estudiante

####################################################################

class TestEstudiante(unittest.TestCase):
    
    ##### Tests del constructor

    def test_init_asigna_atributos(self):
        # verificar si el inicializador guarda bien los atributos
        e:Estudiante = Estudiante("CBA", 766.34728, 98.88, -0.3232, "Urbano", "Estatal")
        self.assertEqual(e.provincia, "CBA")
        self.assertAlmostEqual(e.puntaje_matematica, 766.34728)
        self.assertAlmostEqual(e.puntaje_lengua, 98.88)
        self.assertAlmostEqual(e.puntaje_nse, -0.3232)
        self.assertEqual(e.ambito, "Urbano")
        self.assertEqual(e.sector, "Estatal")
        
        e:Estudiante= Estudiante("CRR", 230.423423, 100.3123123, -1.324232, "Rural", "Estatal")
        self.assertEqual(e.provincia, "CRR")
        self.assertAlmostEqual(e.puntaje_matematica, 230.423423)
        self.assertAlmostEqual(e.puntaje_lengua, 100.3123123)
        self.assertAlmostEqual(e.puntaje_nse, -1.324232)
        self.assertEqual(e.ambito, "Rural")
        self.assertEqual(e.sector, "Estatal")
        
        e:Estudiante=Estudiante("LPA", 690.87878, 498.328390, -2.839213, "Rural", "Privado")
        self.assertEqual(e.provincia, "LPA")
        self.assertAlmostEqual(e.puntaje_matematica, 690.87878)
        self.assertAlmostEqual(e.puntaje_lengua, 498.328390)
        self.assertAlmostEqual(e.puntaje_nse, -2.839213)
        self.assertEqual(e.ambito, "Rural")
        self.assertEqual(e.sector, "Privado")
        
        e:Estudiante=Estudiante("SDE", 120.931209, 671.183798, 0.43243234, "Urbano", "Privado")
        self.assertEqual(e.provincia, "SDE")
        self.assertAlmostEqual(e.puntaje_matematica, 120.931209)
        self.assertAlmostEqual(e.puntaje_lengua, 671.183798)
        self.assertAlmostEqual(e.puntaje_nse, 0.43243234)
        self.assertEqual(e.ambito, "Urbano")
        self.assertEqual(e.sector, "Privado")
    
    def test_init_strings_con_espacios_o_vacios(self):
        # verificar si se guarda tal cual los espacios o cadenas vacias
        e:Estudiante = Estudiante("    ", 873.98, 433.23, -0.3123, "", "")
        self.assertEqual(e.provincia, "    ")
        self.assertAlmostEqual(e.puntaje_matematica, 873.98)
        self.assertAlmostEqual(e.puntaje_lengua, 433.23)
        self.assertAlmostEqual(e.puntaje_nse, -0.3123)
        self.assertEqual(e.ambito, "")
        self.assertEqual(e.sector, "")
        
        e:Estudiante=Estudiante("", 345.1231,329.123213, 1.42342, "          ", "   ")
        self.assertEqual(e.provincia, "")
        self.assertAlmostEqual(e.puntaje_matematica, 345.1231)
        self.assertAlmostEqual(e.puntaje_lengua, 329.123213)
        self.assertAlmostEqual(e.puntaje_nse, 1.42342)
        self.assertEqual(e.ambito, "          ")
        self.assertEqual(e.sector, "   ")
        
        e:Estudiante=Estudiante("         ", 876.321321, 234.213213, 0.32345555, " ", "            ")
        self.assertEqual(e.provincia, "         ")
        self.assertAlmostEqual(e.puntaje_matematica, 876.321321)
        self.assertAlmostEqual(e.puntaje_lengua, 234.213213)
        self.assertAlmostEqual(e.puntaje_nse, 0.32345555)
        self.assertEqual(e.ambito, " ")
        self.assertEqual(e.sector, "            ")
        
        e:Estudiante= Estudiante("", 234.13221312, 98.3232, -1.32323, "", "")
        self.assertEqual(e.provincia, "")
        self.assertAlmostEqual(e.puntaje_matematica, 234.13221312)
        self.assertAlmostEqual(e.puntaje_lengua, 98.3232)
        self.assertAlmostEqual(e.puntaje_nse, -1.32323)
        self.assertEqual(e.ambito, "")
        self.assertEqual(e.sector, "")
        
    def test_init_strings_largos(self):
        # los atributos de tipo string son muy "largos"
        e:Estudiante= Estudiante("P"*100, 500.33, 45.99, -0.545, "W"*100, "V"*100)
        self.assertEqual(e.provincia, "P"*100)
        self.assertAlmostEqual(e.puntaje_matematica, 500.33)
        self.assertAlmostEqual(e.puntaje_lengua, 45.99)
        self.assertAlmostEqual(e.puntaje_nse, -0.545)
        self.assertEqual(e.ambito, "W"*100)
        self.assertEqual(e.sector, "V"*100)
        
        e:Estudiante=Estudiante("ballenas"*50, 234.546, 23.24324, 0.987, "serpientes"*50, "pandas"*50)
        self.assertEqual(e.provincia, "ballenas"*50)
        self.assertAlmostEqual(e.puntaje_matematica, 234.546)
        self.assertAlmostEqual(e.puntaje_lengua, 23.24324)
        self.assertAlmostEqual(e.puntaje_nse, 0.987)
        self.assertEqual(e.ambito, "serpientes"*50)
        self.assertEqual(e.sector, "pandas"*50)
        
        e:Estudiante= Estudiante("entrenar"*80, 234.54353, 234.789998, -1.897987,"testear"*87, "deploy"*87)
        self.assertEqual(e.provincia, "entrenar"*80)
        self.assertAlmostEqual(e.puntaje_matematica,234.54353)
        self.assertAlmostEqual(e.puntaje_lengua, 234.789998)
        self.assertAlmostEqual(e.puntaje_nse, -1.897987)
        self.assertEqual(e.ambito, "testear"*87)
        self.assertEqual(e.sector, "deploy"*87)
        
        e:Estudiante=Estudiante("***$$"*90, 211.98999, 545.9888, -2.7363636, "???--"*50, "<>"*60)
        self.assertEqual(e.provincia, "***$$"*90)
        self.assertAlmostEqual(e.puntaje_matematica,211.98999)
        self.assertAlmostEqual(e.puntaje_lengua, 545.9888)
        self.assertAlmostEqual(e.puntaje_nse, -2.7363636)
        self.assertEqual(e.ambito, "???--"*50)
        self.assertEqual(e.sector, "<>"*60)
        
    def test_init_floats_muchos_decimales(self):
        # los atributos de tipo float tienen muchos decimales
        e:Estudiante= Estudiante("LRI", 300.84279847329847239874293, 89.7892374827492, -0.79823742983742, "Urbano", "Estatal")
        self.assertEqual(e.provincia, "LRI")
        self.assertAlmostEqual(e.puntaje_matematica, 300.84279847329847239874293)
        self.assertAlmostEqual(e.puntaje_lengua, 89.7892374827492)
        self.assertAlmostEqual(e.puntaje_nse, -0.79823742983742)
        self.assertEqual(e.ambito, "Urbano")
        self.assertEqual(e.sector, "Estatal")
        
        e:Estudiante=Estudiante("ETR", 678.376127361273612836123212, 653.612876736427423648234, 0.463287642364234, "Rural", "Estatal")
        self.assertEqual(e.provincia, "ETR")
        self.assertAlmostEqual(e.puntaje_matematica, 678.376127361273612836123212)
        self.assertAlmostEqual(e.puntaje_lengua, 653.612876736427423648234)
        self.assertAlmostEqual(e.puntaje_nse, 0.463287642364234)
        self.assertEqual(e.ambito, "Rural")
        self.assertEqual(e.sector, "Estatal")
        
        e:Estudiante=Estudiante("FOR", 3.141592653589793238462643383279, 1.4142135623730950488016887242 ,2.71828182845904523536028747135266, "Urbano", "Privado" )
        self.assertEqual(e.provincia, "FOR")
        self.assertAlmostEqual(e.puntaje_matematica, 3.141592653589793238462643383279)
        self.assertAlmostEqual(e.puntaje_lengua, 1.4142135623730950488016887242)
        self.assertAlmostEqual(e.puntaje_nse, 2.71828182845904523536028747135266)
        self.assertEqual(e.ambito, "Urbano")
        self.assertEqual(e.sector, "Privado")
        
        e:Estudiante=Estudiante("TDF", 782.32132138729837128731823218, 328.87183687126371263721323, 0.767136721637216321, "Urbano", "Estatal")
        self.assertEqual(e.provincia, "TDF")
        self.assertAlmostEqual(e.puntaje_matematica, 782.32132138729837128731823218)
        self.assertAlmostEqual(e.puntaje_lengua, 328.87183687126371263721323)
        self.assertAlmostEqual(e.puntaje_nse, 0.767136721637216321)
        self.assertEqual(e.ambito, "Urbano")
        self.assertEqual(e.sector, "Estatal")
        
    def test_init_casos_variados(self):
        # string con comillas adentro
        e:Estudiante= Estudiante("'CBA'", 300.93, 400.32, -0.1231, "'Urbano'", "Estatal")
        self.assertEqual(e.provincia, "'CBA'")
        self.assertAlmostEqual(e.puntaje_matematica, 300.93)
        self.assertAlmostEqual(e.puntaje_lengua, 400.32)
        self.assertAlmostEqual(e.puntaje_nse,-0.1231)
        self.assertEqual(e.ambito, "'Urbano'")
        self.assertEqual(e.sector, "Estatal")
        
        e:Estudiante=Estudiante("""LRI""", 879.321312, 890.3273,-2.7398721 ,""""Rural""", """Estatal""")
        self.assertEqual(e.provincia, "LRI")
        self.assertAlmostEqual(e.puntaje_matematica, 879.321312 )
        self.assertAlmostEqual(e.puntaje_lengua, 890.3273)
        self.assertAlmostEqual(e.puntaje_nse,-2.7398721)
        self.assertEqual(e.ambito, """"Rural""")
        self.assertEqual(e.sector, "Estatal")
        # valores float en forma string convertidos
        e:Estudiante=Estudiante("CBA", float("400.42"), float("233.23"), float("-0.2313"), "Urbano", "Privado")
        self.assertEqual(e.provincia, "CBA")
        self.assertAlmostEqual(e.puntaje_matematica, 400.42)
        self.assertAlmostEqual(e.puntaje_lengua, 233.23)
        self.assertAlmostEqual(e.puntaje_nse,-0.2313)
        self.assertEqual(e.ambito, "Urbano")
        self.assertEqual(e.sector, "Privado")
        # valores int convertidos en float
        e:Estudiante=Estudiante("SCZ", float(345), float(879), float(1), "Rural", "Estatal")
        self.assertEqual(e.provincia, "SCZ")
        self.assertAlmostEqual(e.puntaje_matematica, 345.0)
        self.assertAlmostEqual(e.puntaje_lengua, 879.0)
        self.assertAlmostEqual(e.puntaje_nse,1.0)
        self.assertEqual(e.ambito, "Rural")
        self.assertEqual(e.sector, "Estatal")
        # cadenas que parecen numeros
        e:Estudiante=Estudiante("123.43", 345.56,899.23, -0.12, "345.123","2344.12")
        self.assertEqual(e.provincia, "123.43")
        self.assertAlmostEqual(e.puntaje_matematica, 345.56)
        self.assertAlmostEqual(e.puntaje_lengua, 899.23)
        self.assertAlmostEqual(e.puntaje_nse,-0.12)
        self.assertEqual(e.ambito, "345.123")
        self.assertEqual(e.sector, "2344.12")

    ##### Test de la representacion del objeto (repr)
    def test_repr_representacion_correcta(self):
        # formato estandar
        e:Estudiante=Estudiante("MIS", 560.213, 569.32, -0.323, "Urbano", "Estatal")
        self.assertEqual(str(e), "<Mat:560.21, Len:569.32, NSE:-0.32, Urbano, Estatal, MIS>")
        
        e:Estudiante=Estudiante("NEU", 783.43824, 879.432473, 1.738273,"Urbano" ,"Privado")
        self.assertEqual(str(e), "<Mat:783.44, Len:879.43, NSE:1.74, Urbano, Privado, NEU>")
        
        e:Estudiante=Estudiante("LPA", 233.878784, 123.4342432, -2.4637743, "Rural", "Estatal")
        self.assertEqual(str(e), "<Mat:233.88, Len:123.43, NSE:-2.46, Rural, Estatal, LPA>")
        
        e:Estudiante=Estudiante("CRR", 345.3123213, 190.34444444, -0.444444444, "Rural", "Privado")
        self.assertEqual(str(e), "<Mat:345.31, Len:190.34, NSE:-0.44, Rural, Privado, CRR>")
        
    def test_repr_floats_un_decimal(self):
        # los atributos floats tienen un solo decimal ej: 23.0, 45.9
        e:Estudiante=Estudiante("PBA", 340.0, 367.0, 1.2, "Rural", "Privado")
        self.assertEqual(str(e), "<Mat:340.00, Len:367.00, NSE:1.20, Rural, Privado, PBA>")
        
        e:Estudiante=Estudiante("STA", 690.1, 100.9, 0.0, "Urbano", "Privado")
        self.assertEqual(str(e), "<Mat:690.10, Len:100.90, NSE:0.00, Urbano, Privado, STA>")
        
        e:Estudiante=Estudiante("MIS", 212.9, 999.9, -0.0, "Rural", "Estatal")
        self.assertEqual(str(e), "<Mat:212.90, Len:999.90, NSE:-0.00, Rural, Estatal, MIS>")
        
        e:Estudiante=Estudiante("JJY", 888.2, 123.7, -1.0, "Urbano", "Estatal")
        self.assertEqual(str(e), "<Mat:888.20, Len:123.70, NSE:-1.00, Urbano, Estatal, JJY>")
        
    def test_repr_redondeo_enteros(self):
        # Los float redondean en un numero un poco mas grande (en enteros)
        e:Estudiante=Estudiante("CAT", 999999.999, 88888.999, 22222.999,"Urbano","Privado")
        self.assertEqual(str(e), "<Mat:1000000.00, Len:88889.00, NSE:22223.00, Urbano, Privado, CAT>")
        
        e:Estudiante=Estudiante("PBA", 234.99999, 879.999999, 0.9999999,"Rural", "Privado")
        self.assertEqual(str(e), "<Mat:235.00, Len:880.00, NSE:1.00, Rural, Privado, PBA>")
        
        e:Estudiante=Estudiante("CHA", 99.99999, 259.9999,1.999999,"Urbano", "Estatal")
        self.assertEqual(str(e), "<Mat:100.00, Len:260.00, NSE:2.00, Urbano, Estatal, CHA>")
        
        e:Estudiante=Estudiante("SDE", 345.9999999,567.99999, -0.9999, "Rural", "Estatal")
        self.assertEqual(str(e), "<Mat:346.00, Len:568.00, NSE:-1.00, Rural, Estatal, SDE>")
        
    def test_repr_redondeo_decimales(self):
        # Los float redondean en un decimal un poco mas grande
        e:Estudiante=Estudiante("FOR", 345.4499,233.2390,1.87699, "Rural", "Estatal")
        self.assertEqual(str(e), "<Mat:345.45, Len:233.24, NSE:1.88, Rural, Estatal, FOR>")
        
        e:Estudiante=Estudiante("CBA", 876.38888, 567.175777, 1.909999, "Rural", "Privado")
        self.assertEqual(str(e), "<Mat:876.39, Len:567.18, NSE:1.91, Rural, Privado, CBA>")
        
        e:Estudiante=Estudiante("JJY",859.8999, 184.8888,-1.347999, "Urbano", "Privado")
        self.assertEqual(str(e), "<Mat:859.90, Len:184.89, NSE:-1.35, Urbano, Privado, JJY>")
        
        e:Estudiante=Estudiante("ETR", 239.16500009,481.86500 ,0.2666,"Urbano","Estatal")
        self.assertEqual(str(e), "<Mat:239.17, Len:481.87, NSE:0.27, Urbano, Estatal, ETR>")
        
    def test_repr_casi_redondeo(self):
        # Los float casi redondean en un numero distinto
        e:Estudiante=Estudiante("FOR", 456.0009999,345.99, 0.39199, "Urbano", "Privado" )
        self.assertEqual(str(e), "<Mat:456.00, Len:345.99, NSE:0.39, Urbano, Privado, FOR>")
        
        e:Estudiante=Estudiante("STA", 768.2909999,230.815, -0.8749999, "Urbano", "Estatal")
        self.assertEqual(str(e), "<Mat:768.29, Len:230.81, NSE:-0.87, Urbano, Estatal, STA>")
        
        e:Estudiante=Estudiante("TUC", 345.18199999,567.23444499,1.8749999, "Rural", "Privado")
        self.assertEqual(str(e), "<Mat:345.18, Len:567.23, NSE:1.87, Rural, Privado, TUC>")
        
        e:Estudiante=Estudiante("SLU",291.7650, 666.644999999, -1.8949999,"Rural", "Estatal")
        self.assertEqual(str(e), "<Mat:291.76, Len:666.64, NSE:-1.89, Rural, Estatal, SLU>")
        
    #### Test de comparacion de objetos (eq)
    def test_eq_objetos_iguales(self):
        #ambos objetos son iguales
        e1:Estudiante= Estudiante("RNE", 420.45982, 234.92381, 0.212321, "Urbano", "Privado")
        e2:Estudiante= Estudiante("RNE", 420.45982, 234.92381, 0.212321, "Urbano", "Privado")
        self.assertTrue(e1==e2)
        
        e1:Estudiante=Estudiante("FOR", 345.31233, 987.98989, -1.874326, "Urbano", "Estatal")
        e2:Estudiante=Estudiante("FOR", 345.31233, 987.98989, -1.874326, "Urbano", "Estatal")
        self.assertTrue(e1==e2)
        
        e1:Estudiante=Estudiante("CHU", 768.87436, 450.34434, 0.344444, "Rural", "Privado")
        e2:Estudiante=Estudiante("CHU", 768.87436, 450.34434, 0.344444, "Rural", "Privado")
        self.assertTrue(e1==e2)
        
        e1:Estudiante=Estudiante("MZA", 190.83387, 777.74484, -2.873942, "Rural", "Estatal")
        e2:Estudiante=Estudiante("MZA", 190.83387, 777.74484, -2.873942, "Rural", "Estatal")
        self.assertTrue(e1==e2)
        
        e1:Estudiante=Estudiante("LPA", 510.77766, 921.87323, 1.642323, "Rural", "Privado")
        e2:Estudiante=Estudiante("LPA", 510.77766, 921.87323, 1.642323, "Rural", "Privado")
        self.assertTrue(e1==e2)
        
    def test_eq_objetos_distintos(self):
        # Dos objetos con atributos completamente diferentes
        e1:Estudiante=Estudiante("CBA", 345.23980, 678.34876, -1.897829, "Urbano", "Estatal")
        e2:Estudiante=Estudiante("TUC", 210.98290, 340.32123, 0.281937, "Rural", "Privado")
        self.assertFalse(e1==e2)
        
        e1:Estudiante=Estudiante("SFE", 156.34562, 311.34222, 0.232498, "Urbano", "Privado")
        e2:Estudiante=Estudiante("LRI", 899.23909, 799.23888, -1.872839, "Rural", "Estatal")
        self.assertFalse(e1==e2)
        
        e1:Estudiante=Estudiante("ETR", 78.92828, 490.89999,1.289922, "Rural", "Privado")
        e2:Estudiante=Estudiante("TDF", 289.82181, 230.564736, -1.783291, "Urbano", "Estatal")
        self.assertFalse(e1==e2)
        
        e1:Estudiante=Estudiante("LPA", 345.99999, 12.38329, -0.942193, "Urbano", "Privado")
        e2:Estudiante=Estudiante("MIS", 812.37826, 200.65910, 1.723339, "Rural", "Estatal")
        self.assertFalse(e1==e2)
        
        e1:Estudiante=Estudiante("SCZ", 728.65777, 234.12882, -2.738290, "Rural", "Estatal")
        e2:Estudiante=Estudiante("SDE", 643.84012, 129.22811, 2.181922, "Urbano", "Privado")
        self.assertFalse(e1==e2)
        
    def test_eq_diferencia_un_atributo(self):
        # diferencia entre ambos estudiantes de un solo atributo
        e1:Estudiante=Estudiante("MIS", 235.83213, 450.24234, 0.192939, "Urbano", "Privado") # en este caso el puntaje nse
        e2:Estudiante=Estudiante("MIS", 235.83213, 450.24234, -0.321312, "Urbano", "Privado")
        self.assertFalse(e1==e2)
        
        e1:Estudiante=Estudiante("CRR", 320.21221, 988.39201, -0.212893, "Rural", "Privado") # en este caso la provincia
        e2:Estudiante=Estudiante("ETR", 320.21221, 988.39201, -0.212893, "Rural", "Privado")
        self.assertFalse(e1==e2)
        
        e1:Estudiante=Estudiante("CAT", 876.45982, 120.38493, 1.382373, "Urbano", "Estatal") # en este caso el puntaje mat
        e2:Estudiante=Estudiante("CAT", 900.26739, 120.38493, 1.382373, "Urbano", "Estatal")
        self.assertFalse(e1==e2)
        
        e1:Estudiante=Estudiante("CHA",567.31238, 90.32845, -2.384932, "Rural", "Estatal") # en este caso el puntaje lengua
        e2:Estudiante=Estudiante("CHA",567.31238, 789.32323, -2.384932, "Rural", "Estatal")
        self.assertFalse(e1==e2)
        
        e1:Estudiante=Estudiante("CBA", 823.32837, 271.38293, 0.281382, "Rural", "Privado") # en este caso el ambito
        e2:Estudiante=Estudiante("CBA", 823.32837, 271.38293, 0.281382, "Urbano", "Privado")
        self.assertFalse(e1==e2)
        
        e1:Estudiante=Estudiante("SFE", 910.28391, 100.21821, -1.839213, "Urbano", "Estatal") # en este caso el sector
        e2:Estudiante=Estudiante("SFE", 910.28391, 100.21821, -1.839213, "Urbano", "Privado")
        self.assertFalse(e1==e2)
        
    def test_eq_diferencia_muy_pequeña_en_decimal_iguales(self):
        # diferencia en float que roza el limite para que ambas sean iguales
        e1:Estudiante=Estudiante("JJY", 234.90098, 456.98923, 0.187312, "Rural", "Estatal" )
        e2:Estudiante=Estudiante("JJY", 234.90108, 456.98899, 0.188194, "Rural", "Estatal")
        self.assertTrue(e1==e2)
        
        e1:Estudiante=Estudiante("SJU",678.23599,209.89000, -2.83100,"Urbano", "Estatal")
        e2:Estudiante=Estudiante("SJU",678.23499,209.88900,-2.83000 ,"Urbano", "Estatal")
        self.assertTrue(e1==e2)
        
        e1:Estudiante=Estudiante("MZA",299.87292, 410.91899,2.90000,"Rural", "Privado")
        e2:Estudiante=Estudiante("MZA",299.87392, 410.91910,2.89900, "Rural", "Privado")
        self.assertTrue(e1==e2)
        
        e1:Estudiante=Estudiante("FOR", 534.29199, 911.32191, -1.319100,"Urbano", "Privado")
        e2:Estudiante=Estudiante("FOR", 534.29299,911.32291,-1.320000, "Urbano", "Privado")
        self.assertTrue(e1==e2)
        
        e1:Estudiante=Estudiante("TUC",700.119999,390.218022,1.321000, "Rural", "Estatal")
        e2:Estudiante=Estudiante("TUC",700.120999,390.217212,1.320000, "Rural", "Estatal")
        self.assertTrue(e1==e2)
        
    def test_eq_diferencia_muy_pequeña_en_decimal_distintos(self):
        # diferencia en float que roza el limite para que ambas no sean iguales
        e1:Estudiante=Estudiante("STA", 657.87987, 456.98923, -1.325346, "Rural", "Estatal")
        e2:Estudiante=Estudiante("STA", 657.88187, 456.98799,-1.326346, "Rural", "Estatal")
        self.assertFalse(e1==e2)
        
        e1:Estudiante=Estudiante("CHU",  789.32832,812.32990,-1.832732, "Urbano", "Estatal")
        e2:Estudiante=Estudiante("CHU", 789.33000,812.32039,-1.823789,"Urbano", "Estatal")
        self.assertFalse(e1==e2)
        
        e1:Estudiante=Estudiante("CAT",349.21282, 723.32838, -1.372813,"Urbano", "Privado")
        e2:Estudiante=Estudiante("CAT",349.21392, 723.32993,-1.371289,"Urbano", "Privado")
        self.assertFalse(e1==e2)
        
        e1:Estudiante=Estudiante("CBA",210.83729,610.23374,-2.986482, "Rural","Privado")
        e2:Estudiante=Estudiante("CBA",210.83900,610.23499,-2.984991, "Rural","Privado")
        self.assertFalse(e1==e2)
        
        e1:Estudiante=Estudiante("TUC", 720.74389, 261.36999,1.783243,"Urbano","Privado")
        e2:Estudiante=Estudiante("TUC", 720.74219, 261.37111,1.784990,"Urbano","Privado")
        self.assertFalse(e1==e2)
####################################################################

unittest.main()
