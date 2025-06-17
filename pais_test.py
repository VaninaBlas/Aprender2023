import unittest

# Importamos el codigo a testear.
from pais import Pais
from estudiante import Estudiante
from resumen import Resumen
####################################################################

class TestPais(unittest.TestCase):
# si hago un test entonces debo saber el output, eso cambia dependiendo el dataset
#
    def test_init_csv_vacio(self):
        #El archivo Aprender2023_curado_v3.csv esta vacio
        p:Pais=Pais("Aprender2023_curado_v3.csv")
        self.assertEqual(p.provincias, set())
        self.assertEqual(len(p.provincias),0)
        self.assertEqual(p.estudiantes, [])
    
    def test_init_csv_no_vacio(self):
        #En este dataset hay variedad de provincias
        p:Pais=Pais("Aprender2023_curado_v1.csv")
        #Verificar datos del dataset
        self.assertEqual(p.provincias, {"MZA", "TUC", "JJY", "PBA"})
        #primer alumno
        e1:Estudiante=p.estudiantes[0]
        self.assertEqual(e1.provincia, "MZA")
        self.assertAlmostEqual(e1.puntaje_matematica, 466.75851)
        self.assertAlmostEqual(e1.puntaje_lengua, 550.31573)
        self.assertAlmostEqual(e1.puntaje_nse, 0.0057786424)
        self.assertEqual(e1.ambito, "Urbano")
        self.assertEqual(e1.sector, "Estatal")
        #ultimo alumno
        e2:Estudiante=p.estudiantes[-1]
        self.assertEqual(e2.provincia, "PBA")
        self.assertAlmostEqual(e2.puntaje_matematica, 472.45874)
        self.assertAlmostEqual(e2.puntaje_lengua, 496.53986)
        self.assertAlmostEqual(e2.puntaje_nse, 0.068856843)
        self.assertEqual(e2.ambito, "Urbano")
        self.assertEqual(e2.sector, "Estatal")
        
        #Ver que no esten en provincias
        self.assertNotIn("FOR",p.provincias)
        self.assertNotIn("CAT",p.provincias)
        self.assertNotIn("SDE",p.provincias)
        self.assertNotIn("SFE",p.provincias)
        
        #Verificar que todos los estudiantes tienen valores validos
        for e in p.estudiantes:
            self.assertIn(e.ambito, {"Rural", "Urbano"})
            self.assertIn(e.sector, {"Estatal", "Privado"})

    def test_init_otro_cvs_no_vacio(self):
        #En este dataset solo hay una provincia
        p:Pais=Pais("Aprender2023_curado_v2.csv")
        #Verificar datos del dataset
        self.assertEqual(p.provincias, {"MZA"})
        #primer alumno
        e1:Estudiante=p.estudiantes[0]
        self.assertEqual(e1.provincia, "MZA")
        self.assertAlmostEqual(e1.puntaje_matematica, 466.75851)
        self.assertAlmostEqual(e1.puntaje_lengua, 550.31573)
        self.assertAlmostEqual(e1.puntaje_nse, 0.0057786424)
        self.assertEqual(e1.ambito, "Urbano")
        self.assertEqual(e1.sector, "Estatal")
        #ultimo alumno
        e2:Estudiante=p.estudiantes[-1]
        self.assertEqual(e2.provincia, "MZA")
        self.assertAlmostEqual(e2.puntaje_matematica, 462.73212)
        self.assertAlmostEqual(e2.puntaje_lengua, 431.39847)
        self.assertAlmostEqual(e2.puntaje_nse, 0.45347098)
        self.assertEqual(e2.ambito, "Urbano")
        self.assertEqual(e2.sector, "Estatal")
        
        #Verificar que todos los estudiantes tienen valores validos
        for e in p.estudiantes:
            self.assertIn(e.ambito, {"Rural", "Urbano"})
            self.assertIn(e.sector, {"Estatal", "Privado"})
            
    def test_init_otro_csv_no_vacio_max_provincias(self):
        #En este dataset estan todas las provincias sin repetirse
        p:Pais=Pais("Aprender2023_curado_v4.csv")
        #Verificar datos del dataset
        self.assertEqual(p.provincias, {"MZA","MIS", "NEU", "CHU","FOR", "SLU","LRI","TDF","LPA","CBA","SCZ","SJU","STA","RNE",
                                        "PBA","JJY","ETR","CHA","CRR","CAB","CAT","TUC","SDE","SFE"})
        #primer alumno
        e1:Estudiante=p.estudiantes[0]
        self.assertEqual(e1.provincia, "MZA")
        self.assertAlmostEqual(e1.puntaje_matematica, 444.71057)
        self.assertAlmostEqual(e1.puntaje_lengua, 457.72147)
        self.assertAlmostEqual(e1.puntaje_nse, 0.92589754)
        self.assertEqual(e1.ambito, "Urbano")
        self.assertEqual(e1.sector, "Estatal")
        #ultimo alumno
        e2:Estudiante=p.estudiantes[-1]
        self.assertEqual(e2.provincia, "NEU")
        self.assertAlmostEqual(e2.puntaje_matematica, 491.25955)
        self.assertAlmostEqual(e2.puntaje_lengua, 487.98367)
        self.assertAlmostEqual(e2.puntaje_nse, 0.19108739)
        self.assertEqual(e2.ambito, "Urbano")
        self.assertEqual(e2.sector, "Privado")
        
        #Verificar que todos los estudiantes tienen valores validos
        for e in p.estudiantes:
            self.assertIn(e.ambito, {"Rural", "Urbano"})
            self.assertIn(e.sector, {"Estatal", "Privado"})
        
    def test_tamano_csv_vacio(self):
        p:Pais=Pais("Aprender2023_curado_v3.csv")
        self.assertEqual(p.tamano(),0)
    def test_tamano_csv_no_vacio(self):
        p:Pais=Pais("Aprender2023_curado_v1.csv") 
        self.assertEqual(p.tamano(), 20)
    def test_tamano_csv_max_provincias(self):
        p:Pais=Pais("Aprender2023_curado_v4.csv")
        self.assertEqual(p.tamano(),24)
        #en este dataset no se repiten las provincias asi que se deberia poder hacer esto
        self.assertEqual(p.tamano(), len(p.provincias))
    def test_tamano_alterando_el_objeto(self):
        #vamos a eliminar y volver a agregar a un estudiante para ver el comportamiento de la funcion
        p:Pais=Pais("Aprender2023_curado_v2.csv")
        e_eliminado:Estudiante=Estudiante("MZA", 462.73212, 431.39847, 0.45347098, "Urbano", "Estatal")
        self.assertEqual(p.tamano(), 20)
        p.estudiantes.pop()
        self.assertEqual(p.tamano(), 19)
        p.estudiantes.append(e_eliminado)
        self.assertEqual(p.tamano(), 20)
        
    def test_resumen_provincia_forma_estandar(self):
        #Ver que funcione correctamente con un dataset estandar
        #provincias {"MZA", "TUC", "JJY", "PBA"}
        p:Pais=Pais("Aprender2023_curado_v1.csv")
        r_provincia_mza:Resumen=p.resumen_provincia("MZA")
        self.assertEqual(r_provincia_mza.cantidad,4)
        self.assertAlmostEqual(r_provincia_mza.promedio_matematica, 454.024015)
        self.assertAlmostEqual(r_provincia_mza.promedio_lengua, 489.1009975)
        self.assertAlmostEqual(r_provincia_mza.promedio_nse, 0.2898807456)
        self.assertAlmostEqual(r_provincia_mza.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_mza.proporcion_sector_estatal, 1.0)
        self.assertEqual(str(p.resumen_provincia("MZA")), "<Mat:454.02, Len:489.10, NSE:0.29, Rural:0.00, Estado:1.00, N:4>")
        cantidad_mza:Resumen=p.resumen_provincia("MZA").cantidad
        
        
        r_provincia_tuc:Resumen=p.resumen_provincia("TUC")
        self.assertEqual(r_provincia_tuc.cantidad,5)
        self.assertAlmostEqual(r_provincia_tuc.promedio_matematica, 495.81574600000005)
        self.assertAlmostEqual(r_provincia_tuc.promedio_lengua, 514.8510560000001)
        self.assertAlmostEqual(r_provincia_tuc.promedio_nse,-0.167289682)
        self.assertAlmostEqual(r_provincia_tuc.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_tuc.proporcion_sector_estatal, 1.0)
        self.assertEqual(str(p.resumen_provincia("TUC")), "<Mat:495.82, Len:514.85, NSE:-0.17, Rural:0.00, Estado:1.00, N:5>")
        cantidad_tuc:Resumen=p.resumen_provincia("TUC").cantidad
        
        
        r_provincia_jjy:Resumen=p.resumen_provincia("JJY")
        self.assertEqual(r_provincia_jjy.cantidad,4)
        self.assertAlmostEqual(r_provincia_jjy.promedio_matematica, 552.3499575000001)
        self.assertAlmostEqual(r_provincia_jjy.promedio_lengua, 580.8318125000001)
        self.assertAlmostEqual(r_provincia_jjy.promedio_nse,1.02289535)
        self.assertAlmostEqual(r_provincia_jjy.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_jjy.proporcion_sector_estatal, 0.0)
        self.assertEqual(str(p.resumen_provincia("JJY")),"<Mat:552.35, Len:580.83, NSE:1.02, Rural:0.00, Estado:0.00, N:4>")
        cantidad_jjy:Resumen=p.resumen_provincia("JJY").cantidad
        
        r_provincia_pba:Resumen=p.resumen_provincia("PBA")
        self.assertEqual(r_provincia_pba.cantidad,7)
        self.assertAlmostEqual(r_provincia_pba.promedio_matematica, 426.5643442857143)
        self.assertAlmostEqual(r_provincia_pba.promedio_lengua, 485.37901142857146)
        self.assertAlmostEqual(r_provincia_pba.promedio_nse,0.10413792257142858)
        self.assertAlmostEqual(r_provincia_pba.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_pba.proporcion_sector_estatal, 1.0)
        self.assertEqual(str(p.resumen_provincia("PBA")),"<Mat:426.56, Len:485.38, NSE:0.10, Rural:0.00, Estado:1.00, N:7>")
        cantidad_pba:Resumen=p.resumen_provincia("PBA").cantidad
        tamano_total:int=cantidad_jjy+cantidad_mza+cantidad_pba+cantidad_tuc
        #tamano deberia ser igual a la suma de cada cantidad de provincia presente en el objeto
        self.assertEqual(p.tamano(), tamano_total)
        
    def test_resumen_provincia_misma_provincia(self):
        #Todos los estudiantes tienen la misma provincia, MZA
        p:Pais=Pais("Aprender2023_curado_v2.csv")
        r_provincia_mza:Resumen=p.resumen_provincia("MZA")
        self.assertEqual(r_provincia_mza.cantidad,20)
        self.assertAlmostEqual(r_provincia_mza.promedio_matematica, 436.94133300000004)
        self.assertAlmostEqual(r_provincia_mza.promedio_lengua, 436.889643)
        self.assertAlmostEqual(r_provincia_mza.promedio_nse, 0.13499930811500002)
        self.assertAlmostEqual(r_provincia_mza.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_mza.proporcion_sector_estatal, 1.0)
        self.assertEqual(str(p.resumen_provincia("MZA")), "<Mat:436.94, Len:436.89, NSE:0.13, Rural:0.00, Estado:1.00, N:20>")
        #el tamano deberia ser igual a la cantidad de estudiantes de provincia mza ya que esa es la unica provincia
        self.assertEqual(p.tamano(), p.resumen_provincia("MZA").cantidad)
    def test_resumen_provincia_proporciones_extremas(self):
        #Las proporciones son 0.0 o 1.0
        
        #Proporciones 0.0
        #en este dataset solo existe la provincia PBA
        p:Pais=Pais("Aprender2023_curado_v6.csv")
        r_provincia_pba:Resumen=p.resumen_provincia("PBA")
        self.assertEqual(r_provincia_pba.cantidad,20)
        self.assertAlmostEqual(r_provincia_pba.promedio_matematica, 554.650312)
        self.assertAlmostEqual(r_provincia_pba.promedio_lengua, 602.666722)
        self.assertAlmostEqual(r_provincia_pba.promedio_nse, 0.8617827235)
        self.assertAlmostEqual(r_provincia_pba.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_pba.proporcion_sector_estatal, 0.0)
        self.assertEqual(str(p.resumen_provincia("PBA")), "<Mat:554.65, Len:602.67, NSE:0.86, Rural:0.00, Estado:0.00, N:20>")
        
        #Proporciones 1.0
        #en este dataset solo existe la provincia MZA
        p:Pais=Pais("Aprender2023_curado_v5.csv")
        r_provincia_mza:Resumen=p.resumen_provincia("MZA")
        self.assertEqual(r_provincia_mza.cantidad,20)
        self.assertAlmostEqual(r_provincia_mza.promedio_matematica, 426.743325)
        self.assertAlmostEqual(r_provincia_mza.promedio_lengua, 432.73115399999995)
        self.assertAlmostEqual(r_provincia_mza.promedio_nse, -0.1779679383)
        self.assertAlmostEqual(r_provincia_mza.proporcion_ambito_rural, 1.0)
        self.assertAlmostEqual(r_provincia_mza.proporcion_sector_estatal, 1.0)
        self.assertEqual(str(p.resumen_provincia("MZA")), "<Mat:426.74, Len:432.73, NSE:-0.18, Rural:1.00, Estado:1.00, N:20>")
        
    def test_resumen_provincia_puntajes_variados(self):
        #Puntajes que son iguales, bajos, altos
        
        #Puntajes altos
        p:Pais=Pais("Aprender2023_curado_v7.csv")
        r_provincia_pba:Resumen=p.resumen_provincia("PBA")
        self.assertEqual(r_provincia_pba.cantidad,9)
        self.assertAlmostEqual(r_provincia_pba.promedio_matematica, 652.6186522222223)
        self.assertAlmostEqual(r_provincia_pba.promedio_lengua, 744.3447211111111)
        self.assertAlmostEqual(r_provincia_pba.promedio_nse, 0.7089793716444445)
        self.assertAlmostEqual(r_provincia_pba.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_pba.proporcion_sector_estatal, 0.2222222222222222)
        self.assertEqual(str(p.resumen_provincia("PBA")), "<Mat:652.62, Len:744.34, NSE:0.71, Rural:0.00, Estado:0.22, N:9>")
        
        #Puntajes bajos
        p:Pais=Pais("Aprender2023_curado_v8.csv")
        r_provincia_pba:Resumen=p.resumen_provincia("PBA")
        self.assertEqual(r_provincia_pba.cantidad,16)
        self.assertAlmostEqual(r_provincia_pba.promedio_matematica, 320.19726625)
        self.assertAlmostEqual(r_provincia_pba.promedio_lengua, 339.73380375)
        self.assertAlmostEqual(r_provincia_pba.promedio_nse, -0.20862220341875)
        self.assertAlmostEqual(r_provincia_pba.proporcion_ambito_rural, 0.0625)
        self.assertAlmostEqual(r_provincia_pba.proporcion_sector_estatal, 0.875)
        self.assertEqual(str(p.resumen_provincia("PBA")), "<Mat:320.20, Len:339.73, NSE:-0.21, Rural:0.06, Estado:0.88, N:16>")
        
        
    def test_resumen_provincia_casos_variados(self):
        #provincia sin estudiantes, unica provincia PBA
        p:Pais=Pais("Aprender2023_curado_v6.csv")
        r_provincia_chu:Resumen=p.resumen_provincia("CHU")
        self.assertEqual(r_provincia_chu.cantidad,0)
        self.assertAlmostEqual(r_provincia_chu.promedio_matematica, 0.0)
        self.assertAlmostEqual(r_provincia_chu.promedio_lengua, 0.0)
        self.assertAlmostEqual(r_provincia_chu.promedio_nse, 0.0)
        self.assertAlmostEqual(r_provincia_chu.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_chu.proporcion_sector_estatal, 0.0)
        self.assertEqual(str(p.resumen_provincia("CHU")), "<Mat:0.00, Len:0.00, NSE:0.00, Rural:0.00, Estado:0.00, N:0>")
        
        #provincia con solo 1 estudiante
        # datos estudiante, provincia=MZA, pun_lengua=457.72147, pun_mat=444.71057, punt_nse=0.92589754, Urbano, Estatal
        p:Pais=Pais("Aprender2023_curado_v4.csv")
        r_provincia_mza:Resumen=p.resumen_provincia("MZA")
        self.assertEqual(r_provincia_mza.cantidad,1)
        self.assertAlmostEqual(r_provincia_mza.promedio_matematica, 444.71057)
        self.assertAlmostEqual(r_provincia_mza.promedio_lengua, 457.72147)
        self.assertAlmostEqual(r_provincia_mza.promedio_nse, 0.92589754)
        self.assertAlmostEqual(r_provincia_mza.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_mza.proporcion_sector_estatal, 1.0)
        self.assertEqual(str(p.resumen_provincia("MZA")),"<Mat:444.71, Len:457.72, NSE:0.93, Rural:0.00, Estado:1.00, N:1>")
####################################################################

unittest.main()
