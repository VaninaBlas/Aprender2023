import unittest
import csv
# Importamos el codigo a testear.
from pais import Pais
from estudiante import Estudiante
from resumen import Resumen
####################################################################

class TestPais(unittest.TestCase):
# si hago un test entonces debo saber el output, eso cambia dependiendo el dataset
#

    ##### Tests del constructor
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
        
    ##### Tests de tamano
    def test_tamano_csv_vacio(self):
        p:Pais=Pais("Aprender2023_curado_v3.csv")
        self.assertEqual(p.tamano(),0)
    def test_tamano_csv_no_vacio(self):
        p:Pais=Pais("Aprender2023_curado_v1.csv") 
        self.assertEqual(p.tamano(), 20)
        p:Pais=Pais("Aprender2023_curado_v5.csv")
        self.assertEqual(p.tamano(), 20)
        p:Pais=Pais("Aprender2023_curado_v6.csv")
        self.assertEqual(p.tamano(), 20)
        p:Pais=Pais("Aprender2023_curado_v7.csv")
        self.assertEqual(p.tamano(), 9)
        p:Pais=Pais("Aprender2023_curado_v8.csv")
        self.assertEqual(p.tamano(), 16)
        p:Pais=Pais("Aprender2023_curado_v9.csv")
        self.assertEqual(p.tamano(), 1)        
        p:Pais=Pais("Aprender2023_curado_v10.csv")
        self.assertEqual(p.tamano(), 20)
        p:Pais=Pais("Aprender2023_curado_v11.csv")
        self.assertEqual(p.tamano(), 17)        
        p:Pais=Pais("Aprender2023_curado_v12.csv")
        self.assertEqual(p.tamano(), 8)        
        p:Pais=Pais("Aprender2023_curado_v13.csv")
        self.assertEqual(p.tamano(), 20)        
        p:Pais=Pais("Aprender2023_curado_v14.csv")
        self.assertEqual(p.tamano(), 13)        
        p:Pais=Pais("Aprender2023_curado_v15.csv")
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
        
        # en este dataset solo hay 1 estudiante
        p:Pais=Pais("Aprender2023_curado_v9.csv")
        self.assertEqual(p.tamano(), 1)
        e_eliminado:Estudiante=Estudiante("CAT", 385.3497, 433.43439, -0.14759018, "Urbano", "Estatal")
        p.estudiantes.pop()
        self.assertEqual(p.tamano(), 0)
        p.estudiantes.append(e_eliminado)
        self.assertEqual(p.tamano(), 1)
        
        
    ##### Tests de resumen provincia
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
        self.assertAlmostEqual(r_provincia_pba.promedio_nse, 0.8517827235000001)
        self.assertAlmostEqual(r_provincia_pba.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_pba.proporcion_sector_estatal, 0.0)
        self.assertEqual(str(p.resumen_provincia("PBA")), "<Mat:554.65, Len:602.67, NSE:0.85, Rural:0.00, Estado:0.00, N:20>")
        
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
        #Puntajes que son bajos, altos
        
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
        
        
    def test_resumen_provincia_eq_mismos_datos_distinto_orden(self):
        #Tienen los mismo datos pero estan en otro orden, deberian ser iguales
        p1:Pais=Pais("Aprender2023_curado_v2.csv")
        r1_provincia_mza:Resumen=p1.resumen_provincia("MZA")
        self.assertEqual(r1_provincia_mza.cantidad,20)
        self.assertAlmostEqual(r1_provincia_mza.promedio_matematica, 436.94133300000004)
        self.assertAlmostEqual(r1_provincia_mza.promedio_lengua, 436.889643)
        self.assertAlmostEqual(r1_provincia_mza.promedio_nse, 0.13499930811500002)
        self.assertAlmostEqual(r1_provincia_mza.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r1_provincia_mza.proporcion_sector_estatal, 1.0)
        
        p2:Pais=Pais("Aprender2023_curado_v10.csv")
        r2_provincia_mza:Resumen=p2.resumen_provincia("MZA")
        self.assertEqual(r2_provincia_mza.cantidad,20)
        self.assertAlmostEqual(r2_provincia_mza.promedio_matematica, 436.94133300000004)
        self.assertAlmostEqual(r2_provincia_mza.promedio_lengua, 436.889643)
        self.assertAlmostEqual(r2_provincia_mza.promedio_nse, 0.13499930811500002)
        self.assertAlmostEqual(r2_provincia_mza.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r2_provincia_mza.proporcion_sector_estatal, 1.0)    
        
        self.assertTrue(r1_provincia_mza==r2_provincia_mza)
        
    def test_resumen_provincia_eq_mismos_atributos_excepto_cantidad(self):
        # Dos datasets que tienen las mismas proporciones y promedios pero se diferencian en la cantidad
        p1:Pais=Pais("Aprender2023_curado_v12.csv")
        r1_provincia_pba:Resumen=p1.resumen_provincia("PBA")
        self.assertEqual(r1_provincia_pba.cantidad,8)
        self.assertAlmostEqual(r1_provincia_pba.promedio_matematica, 575.57098)
        self.assertAlmostEqual(r1_provincia_pba.promedio_lengua, 641.13306)
        self.assertAlmostEqual(r1_provincia_pba.promedio_nse, 0.6111070500000001)
        self.assertAlmostEqual(r1_provincia_pba.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r1_provincia_pba.proporcion_sector_estatal, 0.0)
        
        p2:Pais=Pais("Aprender2023_curado_v11.csv")
        r2_provincia_pba:Resumen=p2.resumen_provincia("PBA")
        self.assertEqual(r2_provincia_pba.cantidad,17)
        self.assertAlmostEqual(r2_provincia_pba.promedio_matematica, 575.5709800000002)
        self.assertAlmostEqual(r2_provincia_pba.promedio_lengua, 641.13306)
        self.assertAlmostEqual(r2_provincia_pba.promedio_nse,0.61110705)
        self.assertAlmostEqual(r2_provincia_pba.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r2_provincia_pba.proporcion_sector_estatal, 0.0)
        
        self.assertFalse(r1_provincia_pba==r2_provincia_pba)
        
    def test_resumen_provincias_mismos_puntajes(self):
        #En este dataset todos los estudiantes tienen los mismos puntajes y proporciones
        p:Pais=Pais("Aprender2023_curado_v11.csv")
        #datos de uno de los estudiantes
        e1:Estudiante=p.estudiantes[0]
        self.assertEqual(e1.provincia, "PBA")
        self.assertAlmostEqual(e1.puntaje_matematica, 575.57098)
        self.assertAlmostEqual(e1.puntaje_lengua, 641.13306)
        self.assertAlmostEqual(e1.puntaje_nse, 0.61110705)
        self.assertEqual(e1.ambito, "Urbano")
        self.assertEqual(e1.sector, "Privado")
        
        r_provincia_pba:Resumen=p.resumen_provincia("PBA")        
        self.assertEqual(r_provincia_pba.cantidad,17)
        self.assertAlmostEqual(r_provincia_pba.promedio_matematica, 575.5709800000002)
        self.assertAlmostEqual(r_provincia_pba.promedio_lengua, 641.13306)
        self.assertAlmostEqual(r_provincia_pba.promedio_nse, 0.61110705)
        self.assertAlmostEqual(r_provincia_pba.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_pba.proporcion_sector_estatal, 0.0)
        self.assertEqual(str(p.resumen_provincia("PBA")), "<Mat:575.57, Len:641.13, NSE:0.61, Rural:0.00, Estado:0.00, N:17>")
        
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
        
        #dataset con solo 1 estudiante
        p:Pais=Pais("Aprender2023_curado_v9.csv")
        r_provincia_cat:Resumen=p.resumen_provincia("CAT")
        self.assertEqual(r_provincia_cat.cantidad,1)
        self.assertAlmostEqual(r_provincia_cat.promedio_matematica, 385.3497)
        self.assertAlmostEqual(r_provincia_cat.promedio_lengua, 433.43439)
        self.assertAlmostEqual(r_provincia_cat.promedio_nse, -0.14759018)
        self.assertAlmostEqual(r_provincia_cat.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_cat.proporcion_sector_estatal, 1.0)
        self.assertEqual(str(p.resumen_provincia("CAT")),"<Mat:385.35, Len:433.43, NSE:-0.15, Rural:0.00, Estado:1.00, N:1>")
        #como solo hay un estudiante podemos decir que tamano es igual al tamaño de p.provincias
        self.assertEqual(p.tamano(), len(p.provincias))
        self.assertEqual(p.tamano(), r_provincia_cat.cantidad)
 
    ##### Tests de resumenes pais  
    def test_resumen_pais_forma_estandar(self):
        #Ver que funcione correctamente con un dataset estandar
        #provincias {"MZA", "TUC", "JJY", "PBA"}
        p:Pais=Pais("Aprender2023_curado_v1.csv")
        # Vemos datos de cada provincia
        #Provincia MZA
        r_provincia_mza:Resumen=p.resumenes_pais()["MZA"]
        self.assertEqual(r_provincia_mza.cantidad,4)
        self.assertAlmostEqual(r_provincia_mza.promedio_matematica, 454.024015)
        self.assertAlmostEqual(r_provincia_mza.promedio_lengua, 489.1009975)
        self.assertAlmostEqual(r_provincia_mza.promedio_nse, 0.2898807456)
        self.assertAlmostEqual(r_provincia_mza.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_mza.proporcion_sector_estatal, 1.0)
        
        #Provincia TUC
        
        r_provincia_tuc:Resumen=p.resumenes_pais()["TUC"]
        self.assertEqual(r_provincia_tuc.cantidad,5)
        self.assertAlmostEqual(r_provincia_tuc.promedio_matematica, 495.81574600000005)
        self.assertAlmostEqual(r_provincia_tuc.promedio_lengua, 514.8510560000001)
        self.assertAlmostEqual(r_provincia_tuc.promedio_nse, -0.167289682)
        self.assertAlmostEqual(r_provincia_tuc.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_tuc.proporcion_sector_estatal, 1.0)
        #Provincia JJY
        r_provincia_jjy:Resumen=p.resumenes_pais()["JJY"]
        self.assertEqual(r_provincia_jjy.cantidad,4)
        self.assertAlmostEqual(r_provincia_jjy.promedio_matematica, 552.3499575000001)
        self.assertAlmostEqual(r_provincia_jjy.promedio_lengua, 580.8318125000001)
        self.assertAlmostEqual(r_provincia_jjy.promedio_nse, 1.02289535)
        self.assertAlmostEqual(r_provincia_jjy.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_jjy.proporcion_sector_estatal, 0.0)
        
        
        #Provincia PBA
        r_provincia_pba:Resumen=p.resumenes_pais()["PBA"]
        self.assertEqual(r_provincia_pba.cantidad,7)
        self.assertAlmostEqual(r_provincia_pba.promedio_matematica, 426.5643442857143)
        self.assertAlmostEqual(r_provincia_pba.promedio_lengua, 485.37901142857146)
        self.assertAlmostEqual(r_provincia_pba.promedio_nse, 0.10413792257142858)
        self.assertAlmostEqual(r_provincia_pba.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_pba.proporcion_sector_estatal, 1.0)
        
        # Vemos la representacion
        #funciona para evitar errores se deja como comentario, porque el orden cambia
       # self.assertEqual(str(p.resumenes_pais()), "{'JJY': <Mat:552.35, Len:580.83, NSE:1.02, Rural:0.00, Estado:0.00, N:4>, 'MZA': <Mat:454.02, Len:489.10, NSE:0.29, Rural:0.00, Estado:1.00, N:4>, 'TUC': <Mat:495.82, Len:514.85, NSE:-0.17, Rural:0.00, Estado:1.00, N:5>, 'PBA': <Mat:426.56, Len:485.38, NSE:0.10, Rural:0.00, Estado:1.00, N:7>}")
        
        #Con esto podemos jugar un poco
        self.assertNotEqual(r_provincia_pba.cantidad, r_provincia_jjy.cantidad) #cantidades distintas (7,4)
        self.assertEqual(r_provincia_jjy.cantidad, r_provincia_mza.cantidad) #cantidades iguales (4,4)
        self.assertEqual(p.tamano(), r_provincia_jjy.cantidad+r_provincia_mza.cantidad+r_provincia_pba.cantidad+r_provincia_tuc.cantidad)
        self.assertEqual(len(p.resumenes_pais()), len(p.provincias)) #la cantidad de claves del dic, coincide con la cant de provincias
        
        #los resúmenes coinciden con los de resumen_provincia
        for provincia in p.provincias:
            self.assertEqual(p.resumenes_pais()[provincia], p.resumen_provincia(provincia))
            
    def test_resumenes_pais_datase_vacio(self):
        #Vemos que devuelve cuando le damos un dataset vacio
        p:Pais=Pais("Aprender2023_curado_v3.csv")
        self.assertEqual(p.resumenes_pais(), {}) 
        self.assertNotIn("MZA",p.resumenes_pais())
        
    def test_resumenes_pais_todas_las_provincias(self):
        # Dataset con todas las provincias
        p:Pais=Pais("Aprender2023_curado_v4.csv")
        #funciona para evitar errores se deja como comentario, porque el orden cambia
        #self.assertEqual(str(p.resumenes_pais()), "{'MZA': <Mat:444.71, Len:457.72, NSE:0.93, Rural:0.00, Estado:1.00, N:1>, 'SJU': <Mat:512.17, Len:538.81, NSE:-0.04, Rural:0.00, Estado:1.00, N:1>, 'TDF': <Mat:542.47, Len:613.14, NSE:1.06, Rural:0.00, Estado:1.00, N:1>, 'LPA': <Mat:522.78, Len:573.57, NSE:0.20, Rural:0.00, Estado:1.00, N:1>, 'STA': <Mat:633.62, Len:714.68, NSE:0.45, Rural:0.00, Estado:0.00, N:1>, 'RNE': <Mat:336.90, Len:408.01, NSE:0.43, Rural:0.00, Estado:1.00, N:1>, 'JJY': <Mat:577.31, Len:599.29, NSE:-0.36, Rural:0.00, Estado:1.00, N:1>, 'CAB': <Mat:440.91, Len:462.07, NSE:0.20, Rural:0.00, Estado:0.00, N:1>, 'CRR': <Mat:552.10, Len:569.64, NSE:0.54, Rural:1.00, Estado:1.00, N:1>, 'TUC': <Mat:391.88, Len:436.27, NSE:0.07, Rural:1.00, Estado:1.00, N:1>, 'CAT': <Mat:400.65, Len:496.77, NSE:0.22, Rural:0.00, Estado:1.00, N:1>, 'LRI': <Mat:414.91, Len:376.51, NSE:0.69, Rural:1.00, Estado:1.00, N:1>, 'MIS': <Mat:426.07, Len:381.35, NSE:-0.21, Rural:0.00, Estado:1.00, N:1>, 'SFE': <Mat:434.40, Len:483.67, NSE:-0.01, Rural:1.00, Estado:1.00, N:1>, 'SDE': <Mat:657.32, Len:727.04, NSE:-2.78, Rural:1.00, Estado:1.00, N:1>, 'ETR': <Mat:477.88, Len:532.67, NSE:0.52, Rural:0.00, Estado:0.00, N:1>, 'CBA': <Mat:548.34, Len:542.47, NSE:0.24, Rural:0.00, Estado:1.00, N:1>, 'PBA': <Mat:466.60, Len:525.84, NSE:0.91, Rural:0.00, Estado:1.00, N:1>, 'CHU': <Mat:426.92, Len:464.34, NSE:-0.98, Rural:1.00, Estado:1.00, N:1>, 'CHA': <Mat:427.76, Len:439.37, NSE:0.37, Rural:0.00, Estado:1.00, N:1>, 'NEU': <Mat:491.26, Len:487.98, NSE:0.19, Rural:0.00, Estado:0.00, N:1>, 'FOR': <Mat:469.00, Len:411.08, NSE:-0.24, Rural:0.00, Estado:1.00, N:1>, 'SCZ': <Mat:666.07, Len:633.89, NSE:1.42, Rural:0.00, Estado:0.00, N:1>, 'SLU': <Mat:504.22, Len:526.07, NSE:0.57, Rural:0.00, Estado:1.00, N:1>}")
        self.assertEqual(p.resumenes_pais().keys(), {"MZA","MIS", "NEU", "CHU","FOR", "SLU","LRI","TDF","LPA","CBA","SCZ","SJU","STA","RNE",
                                        "PBA","JJY","ETR","CHA","CRR","CAB","CAT","TUC","SDE","SFE"})
        #los resúmenes coinciden con los de resumen_provincia
        for provincia in p.provincias:
            self.assertEqual(p.resumenes_pais()[provincia], p.resumen_provincia(provincia))
            
        self.assertIn("MZA", p.resumenes_pais())
        
    def test_resumenes_pais_solo_una_provincia(self):
        #En el dataset solo hay una provincia
        p:Pais=Pais("Aprender2023_curado_v2.csv")
        r_provincia_mza:Resumen=p.resumenes_pais()["MZA"]
        self.assertEqual(r_provincia_mza.cantidad,20)
        self.assertAlmostEqual(r_provincia_mza.promedio_matematica, 436.94133300000004)
        self.assertAlmostEqual(r_provincia_mza.promedio_lengua, 436.889643)
        self.assertAlmostEqual(r_provincia_mza.promedio_nse, 0.13499930811500002)
        self.assertAlmostEqual(r_provincia_mza.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_mza.proporcion_sector_estatal, 1.0)
        #funciona para evitar errores se deja como comentario, porque el orden cambia
        #self.assertEqual(str(p.resumenes_pais()), "{'MZA': <Mat:436.94, Len:436.89, NSE:0.13, Rural:0.00, Estado:1.00, N:20>}")
        # Deberian ser iguales
        self.assertEqual(p.resumenes_pais()["MZA"], p.resumen_provincia("MZA"))
        self.assertEqual(r_provincia_mza.cantidad, p.tamano())
    def test_resumenes_pais_proporciones_extremas(self):
        #Las proporciones son 0.0 o 1.0
        
        #Proporciones 0.0
        #en este dataset solo existe la provincia PBA
        p:Pais=Pais("Aprender2023_curado_v6.csv")
        r_provincia_pba:Resumen=p.resumenes_pais()["PBA"]
        self.assertEqual(r_provincia_pba.cantidad,20)
        self.assertAlmostEqual(r_provincia_pba.promedio_matematica, 554.650312)
        self.assertAlmostEqual(r_provincia_pba.promedio_lengua, 602.666722)
        self.assertAlmostEqual(r_provincia_pba.promedio_nse, 0.8517827235000001)
        self.assertAlmostEqual(r_provincia_pba.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_pba.proporcion_sector_estatal, 0.0)
        #funciona para evitar errores se deja como comentario, porque el orden cambia
        #self.assertEqual(str(p.resumenes_pais()), "{'PBA': <Mat:554.65, Len:602.67, NSE:0.85, Rural:0.00, Estado:0.00, N:20>}")
        
        #Proporciones 1.0
        #en este dataset solo existe la provincia MZA
        p:Pais=Pais("Aprender2023_curado_v5.csv")
        r_provincia_mza:Resumen=p.resumenes_pais()["MZA"]
        self.assertEqual(r_provincia_mza.cantidad,20)
        self.assertAlmostEqual(r_provincia_mza.promedio_matematica, 426.743325)
        self.assertAlmostEqual(r_provincia_mza.promedio_lengua, 432.73115399999995)
        self.assertAlmostEqual(r_provincia_mza.promedio_nse, -0.1779679383)
        self.assertAlmostEqual(r_provincia_mza.proporcion_ambito_rural, 1.0)
        self.assertAlmostEqual(r_provincia_mza.proporcion_sector_estatal, 1.0)
        #funciona para evitar errores se deja como comentario, porque el orden cambia
        #self.assertEqual(str(p.resumenes_pais()), "{'MZA': <Mat:426.74, Len:432.73, NSE:-0.18, Rural:1.00, Estado:1.00, N:20>}")
        
        #Es identico al caso de resumen_provincia, entonces
        self.assertEqual(p.resumen_provincia("MZA"), p.resumenes_pais()["MZA"])
        self.assertEqual(r_provincia_mza.cantidad, p.tamano())
        #Como ambos tienen la misma cantidad de su provincia, y es una unica provincia, podemos decir que
        self.assertEqual(r_provincia_pba.cantidad, r_provincia_mza.cantidad)
        
        #Pero siguen siendo distintos
        self.assertFalse(r_provincia_mza==r_provincia_pba)
    def test_resumenes_pais_puntajes_variados(self):
        #Con variedad de provincia
        #Puntajes bajos
        p:Pais=Pais("Aprender2023_curado_v14.csv")
        
        #funciona para evitar errores se deja como comentario, porque el orden cambia
        #self.assertEqual(str(p.resumenes_pais()),"{'CHU': <Mat:250.35, Len:449.70, NSE:0.24, Rural:0.00, Estado:1.00, N:1>, 'SDE': <Mat:250.78, Len:386.14, NSE:-0.38, Rural:0.00, Estado:1.00, N:1>, 'CRR': <Mat:250.41, Len:350.96, NSE:-0.71, Rural:0.00, Estado:1.00, N:1>, 'CHA': <Mat:302.46, Len:250.81, NSE:-0.05, Rural:0.00, Estado:1.00, N:1>, 'TUC': <Mat:250.61, Len:347.53, NSE:-0.83, Rural:0.50, Estado:1.00, N:2>, 'PBA': <Mat:250.56, Len:340.07, NSE:-0.14, Rural:0.00, Estado:1.00, N:5>, 'LRI': <Mat:250.95, Len:323.74, NSE:-1.19, Rural:0.00, Estado:1.00, N:1>, 'MIS': <Mat:250.34, Len:373.42, NSE:1.17, Rural:0.00, Estado:1.00, N:1>}")
        
        #los resúmenes coinciden con los de resumen_provincia
        for provincia in p.provincias:
            self.assertEqual(p.resumenes_pais()[provincia], p.resumen_provincia(provincia))
        
        #Puntajes altos
        p:Pais=Pais("Aprender2023_curado_v13.csv")
        #funciona para evitar errores se deja como comentario, porque el orden cambia
        #self.assertEqual(p.resumenes_pais(), "{'MIS': <Mat:711.41, Len:596.11, NSE:-1.70, Rural:0.50, Estado:1.00, N:2>, 'TUC': <Mat:666.07, Len:700.14, NSE:1.09, Rural:0.00, Estado:0.00, N:1>, 'CBA': <Mat:661.41, Len:693.82, NSE:0.73, Rural:0.20, Estado:0.40, N:5>, 'SJU': <Mat:567.73, Len:700.20, NSE:1.09, Rural:0.00, Estado:1.00, N:1>, 'CAB': <Mat:601.62, Len:700.41, NSE:0.70, Rural:0.00, Estado:1.00, N:1>, 'NEU': <Mat:700.38, Len:640.61, NSE:0.89, Rural:0.00, Estado:0.00, N:1>, 'SFE': <Mat:670.43, Len:672.65, NSE:0.83, Rural:0.67, Estado:0.67, N:3>, 'PBA': <Mat:624.22, Len:692.56, NSE:0.80, Rural:0.00, Estado:0.33, N:6>}")
        #los resúmenes coinciden con los de resumen_provincia
        for provincia in p.provincias:
            self.assertEqual(p.resumenes_pais()[provincia], p.resumen_provincia(provincia))
            
    def test_resumenes_eq_pais_mismos_puntajes(self):
        #En este dataset todos los estudiantes tienen los mismos puntajes y proporciones (distintas provincias)
        p:Pais=Pais("Aprender2023_curado_v15.csv")
        #vemos un resumen random
        r_provincia_mza:Resumen=p.resumenes_pais()["MZA"]
        self.assertEqual(r_provincia_mza.cantidad, 1)
        self.assertAlmostEqual(r_provincia_mza.promedio_matematica, 694.93115)
        self.assertAlmostEqual(r_provincia_mza.promedio_lengua, 700.53345)
        self.assertAlmostEqual(r_provincia_mza.promedio_nse, 0.61757135)
        self.assertAlmostEqual(r_provincia_mza.proporcion_ambito_rural, 0.0)
        self.assertAlmostEqual(r_provincia_mza.proporcion_sector_estatal, 0.0)
        # sus datos son iguales a mza 
        r_provincia_rne:Resumen=p.resumenes_pais()["RNE"]
        #Entonces deberian ser iguales
        self.assertTrue(r_provincia_mza==r_provincia_rne)
        #representacion
        #funciona para evitar errores se deja como comentario, porque el orden cambia
        #self.assertEqual(str(p.resumenes_pais()),"{'MZA': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'SJU': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'TDF': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'LPA': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'STA': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'RNE': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'JJY': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'CAB': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'CRR': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'TUC': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'CAT': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'LRI': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'MIS': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'SFE': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'SDE': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'ETR': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'CBA': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'PBA': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'CHA': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>, 'SCZ': <Mat:694.93, Len:700.53, NSE:0.62, Rural:0.00, Estado:0.00, N:1>}")
        
        #los resúmenes coinciden con los de resumen_provincia
        for provincia in p.provincias:
            self.assertEqual(p.resumenes_pais()[provincia], p.resumen_provincia(provincia))
            
    ##### Tests de estudiantes en intervalo            
    def test_estudiantes_en_intervalo_cumplen_intervalo(self):
        # el dataset tiene las provincias {"MZA", "TUC", "JJY", "PBA"}
        p:Pais=Pais("Aprender2023_curado_v1.csv")
        self.assertEqual(p.tamano(), 20)
        self.assertEqual(p.estudiantes_en_intervalo("mat", 100, 800, {"MZA", "TUC", "JJY", "PBA"}),20)
        self.assertEqual(p.estudiantes_en_intervalo("len", 100, 800, {"MZA", "TUC", "JJY", "PBA"}),20)
        self.assertEqual(p.estudiantes_en_intervalo("nse", -2.0, 2.0, {"MZA", "TUC", "JJY", "PBA"}),20)
        
        self.assertEqual(p.estudiantes_en_intervalo("mat", 100, 800, {"MZA"}),4)        
        self.assertEqual(p.estudiantes_en_intervalo("mat", 100, 800, {"TUC"}),5)
        self.assertEqual(p.estudiantes_en_intervalo("mat", 100, 800, {"JJY"}),4)
        self.assertEqual(p.estudiantes_en_intervalo("mat", 100, 800, {"PBA"}),7)
        
        self.assertEqual(p.estudiantes_en_intervalo("len", 100, 800, {"MZA"}),4)
        self.assertEqual(p.estudiantes_en_intervalo("len", 100, 800, {"TUC"}),5)
        self.assertEqual(p.estudiantes_en_intervalo("len", 100, 800, {"JJY"}),4)
        self.assertEqual(p.estudiantes_en_intervalo("len", 100, 800, {"PBA"}),7)
        
        self.assertEqual(p.estudiantes_en_intervalo("nse", -2.0, 2.0, {"MZA"}),4)
        self.assertEqual(p.estudiantes_en_intervalo("nse", -2.0, 2.0, {"TUC"}),5)
        self.assertEqual(p.estudiantes_en_intervalo("nse", -2.0, 2.0, {"JJY"}),4)
        self.assertEqual(p.estudiantes_en_intervalo("nse", -2.0, 2.0, {"PBA"}),7)
        
        
    def test_estudiantes_en_intervalo_no_cumplen_intervalo(self):
        #Ningun estudiante cumple con el intervalo
        #usamos el dataset de estudiantes puntajes bajos
        p:Pais=Pais("Aprender2023_curado_v14.csv")
        self.assertEqual(p.tamano(), 13)
        self.assertEqual(p.provincias, {'CHA', 'MIS', 'LRI', 'SDE', 'CRR', 'TUC', 'PBA', 'CHU'})
        self.assertEqual(p.estudiantes_en_intervalo("mat", 800, 900, {'CHA', 'MIS', 'LRI', 'SDE', 'CRR', 'TUC', 'PBA', 'CHU'}),0)
        self.assertEqual(p.estudiantes_en_intervalo("len", 800, 900, {'CHA', 'MIS', 'LRI', 'SDE', 'CRR', 'TUC', 'PBA', 'CHU'}),0)
        self.assertEqual(p.estudiantes_en_intervalo("nse", 1.9, 2.0, {'CHA', 'MIS', 'LRI', 'SDE', 'CRR', 'TUC', 'PBA', 'CHU'}),0)
        
        #usamos el dataset de estudiantes puntajes altos
        p:Pais=Pais("Aprender2023_curado_v13.csv")
        self.assertEqual(p.tamano(), 20)
        self.assertEqual(p.provincias, {'MIS', 'TUC', 'CBA', 'SJU', 'CAB', 'NEU', 'SFE', 'PBA'})
        self.assertEqual(p.estudiantes_en_intervalo("mat", 100, 200, {'MIS', 'TUC', 'CBA', 'SJU', 'CAB', 'NEU', 'SFE', 'PBA'}),0)
        self.assertEqual(p.estudiantes_en_intervalo("len", 100, 200, {'MIS', 'TUC', 'CBA', 'SJU', 'CAB', 'NEU', 'SFE', 'PBA'}),0)
        self.assertEqual(p.estudiantes_en_intervalo("nse", -2.0, -1.9, {'MIS', 'TUC', 'CBA', 'SJU', 'CAB', 'NEU', 'SFE', 'PBA'}),0)
   
    def test_estudiantes_en_intervalo_un_solo_estudiante_cumple(self):
        #en el dataset solo hay un estudiante que cumple con la condicion
        p:Pais=Pais("Aprender2023_curado_v6.csv")
        self.assertEqual(p.tamano(), 20)
        self.assertEqual(p.provincias, {'PBA'})
        self.assertEqual(p.estudiantes_en_intervalo("mat", 660, 900,{'PBA'}),1)
        self.assertEqual(p.estudiantes_en_intervalo("len", 710, 900, {'PBA'}),1)
        self.assertEqual(p.estudiantes_en_intervalo("nse", 1.4, 2.0, {'PBA'}),1)
        # que coincidencia ese estudiante es el primero
        e:Estudiante=p.estudiantes[0]
        self.assertEqual(e.puntaje_lengua,714.43982)
        self.assertEqual(e.puntaje_nse,1.4225767)
        self.assertEqual(e.puntaje_matematica, 660.72998)
        
    def test_estudiantes_en_intervalo_rozan_el_intervalo_cumplen(self):
        p:Pais=Pais("Aprender2023_curado_v8.csv")
        self.assertEqual(p.tamano(), 16)
        self.assertEqual(p.provincias, {'PBA'})
        self.assertEqual(p.estudiantes_en_intervalo("mat", 300, 351,{'PBA'}),13)
        self.assertEqual(p.estudiantes_en_intervalo("len", 300, 400, {'PBA'}),15)
        self.assertEqual(p.estudiantes_en_intervalo("nse", -1.4, 1.8, {'PBA'}),13)
        
    def test_estudiantes_en_intervalo_rozan_el_intervalo_no_cumplen(self):
        p:Pais=Pais("Aprender2023_curado_v8.csv")
        self.assertEqual(p.tamano(), 16)
        self.assertEqual(p.provincias, {'PBA'})
        self.assertEqual(p.estudiantes_en_intervalo("mat", 250, 299,{'PBA'}),0)
        self.assertEqual(p.estudiantes_en_intervalo("len", 400, 450, {'PBA'}),0)
        self.assertEqual(p.estudiantes_en_intervalo("nse", 1.7, 1.8, {'PBA'}),0)
    
    ##### Tests de exportar por provincias
    def test_exportar_por_provincias_funcionamiento(self):
        #Debe exportar correctamente segun las provincias que ingreso
        #provincias {"MZA", "TUC", "JJY", "PBA"}
        p:Pais=Pais("Aprender2023_curado_v1.csv")
        p.exportar_por_provincias("resumen_dataset_v1.csv", {"MZA", "TUC", "JJY", "PBA"})
        f = open("resumen_dataset_v1.csv", encoding="utf-8")
        lector = csv.DictReader(f)
        
        #comparamos los resumenes del archivo creado con los que tien el objeto p
        provincias_en_archivo:set[str] = set()
        for fila in lector:
            provincia:str=fila["provincia"]
            provincias_en_archivo.add(provincia)
            resumen:Resumen = p.resumen_provincia(provincia)
            self.assertEqual(int(fila["cantidad"]), resumen.cantidad)
            self.assertAlmostEqual(float(fila["promedio_matematica"]), resumen.promedio_matematica)
            self.assertAlmostEqual(float(fila["promedio_lengua"]), resumen.promedio_lengua)
            self.assertAlmostEqual(float(fila["promedio_nse"]), resumen.promedio_nse)
            self.assertAlmostEqual(float(fila["proporcion_ambito_rural"]), resumen.proporcion_ambito_rural)
            self.assertAlmostEqual(float(fila["proporcion_sector_estatal"]), resumen.proporcion_sector_estatal)
    
        f.close()
        self.assertEqual(provincias_en_archivo, p.provincias)
        
        
    def test_exportar_por_provincias_una_provincia(self):
        #Debe exportar resumen de una sola provincia
        # solo provincia {"MZA"}
        p:Pais=Pais("Aprender2023_curado_v5.csv")
        p.exportar_por_provincias("resumen_dataset_v5.csv", {"MZA"})
        f = open("resumen_dataset_v5.csv", encoding="utf-8")
        lector = csv.DictReader(f)
    
        provincias_en_archivo:set[str] = set()
        #comparamos los resumenes del archivo creado con los que tien el objeto p
        for fila in lector:
            provincia:str=fila["provincia"]
            provincias_en_archivo.add(provincia)
            resumen:Resumen = p.resumen_provincia(provincia)
            self.assertEqual(int(fila["cantidad"]), resumen.cantidad)
            self.assertAlmostEqual(float(fila["promedio_matematica"]), resumen.promedio_matematica)
            self.assertAlmostEqual(float(fila["promedio_lengua"]), resumen.promedio_lengua)
            self.assertAlmostEqual(float(fila["promedio_nse"]), resumen.promedio_nse)
            self.assertAlmostEqual(float(fila["proporcion_ambito_rural"]), resumen.proporcion_ambito_rural)
            self.assertAlmostEqual(float(fila["proporcion_sector_estatal"]), resumen.proporcion_sector_estatal)
    
        f.close()
        self.assertEqual(len(provincias_en_archivo), len(p.provincias))
        self.assertEqual(provincias_en_archivo, p.provincias)
              
    def test_exportar_por_provincias_todas_las_provincias(self):
        p:Pais=Pais("Aprender2023_curado_v4.csv")
        p.exportar_por_provincias("resumen_dataset_v4.csv", {"MZA","MIS", "NEU", "CHU","FOR", "SLU","LRI","TDF","LPA","CBA","SCZ","SJU","STA","RNE",
                                        "PBA","JJY","ETR","CHA","CRR","CAB","CAT","TUC","SDE","SFE"})
        f = open("resumen_dataset_v4.csv", encoding="utf-8")
        lector = csv.DictReader(f)
    
        provincias_en_archivo:set[str] = set()
        #comparamos los resumenes del archivo creado con los que tien el objeto p
        for fila in lector:
            provincia:str=fila["provincia"]
            provincias_en_archivo.add(provincia)
            resumen:Resumen = p.resumen_provincia(provincia)
            self.assertEqual(int(fila["cantidad"]), resumen.cantidad)
            self.assertAlmostEqual(float(fila["promedio_matematica"]), resumen.promedio_matematica)
            self.assertAlmostEqual(float(fila["promedio_lengua"]), resumen.promedio_lengua)
            self.assertAlmostEqual(float(fila["promedio_nse"]), resumen.promedio_nse)
            self.assertAlmostEqual(float(fila["proporcion_ambito_rural"]), resumen.proporcion_ambito_rural)
            self.assertAlmostEqual(float(fila["proporcion_sector_estatal"]), resumen.proporcion_sector_estatal)
    
    
        f.close()
        self.assertEqual(provincias_en_archivo, p.provincias)
        
        
    def test_exportar_por_provincias_unico_estudiante(self):
        #unico estudiante de provincia CAT
        p:Pais=Pais("Aprender2023_curado_v9.csv")
        p.exportar_por_provincias("resumen_dataset_v9.csv", {"CAT"})
        
        f = open("resumen_dataset_v9.csv", encoding="utf-8")
        lector = csv.DictReader(f)
    
        provincias_en_archivo:set[str] = set()
        #comparamos los resumenes del archivo creado con los que tien el objeto p
        for fila in lector:
            provincia:str=fila["provincia"]
            provincias_en_archivo.add(provincia)
            resumen:Resumen = p.resumen_provincia(provincia)
            self.assertEqual(int(fila["cantidad"]), resumen.cantidad)
            self.assertAlmostEqual(float(fila["promedio_matematica"]), resumen.promedio_matematica)
            self.assertAlmostEqual(float(fila["promedio_lengua"]), resumen.promedio_lengua)
            self.assertAlmostEqual(float(fila["promedio_nse"]), resumen.promedio_nse)
            self.assertAlmostEqual(float(fila["proporcion_ambito_rural"]), resumen.proporcion_ambito_rural)
            self.assertAlmostEqual(float(fila["proporcion_sector_estatal"]), resumen.proporcion_sector_estatal)
    
    
        f.close()
        self.assertEqual(provincias_en_archivo, p.provincias)
        

    def test_exportar_por_provincias_puntajes_variados(self):
        #Puntajes que son bajos, altos
        #unica provinica PBA
        #Puntajes altos
        p:Pais=Pais("Aprender2023_curado_v7.csv")
        p.exportar_por_provincias("resumen_dataset_v7.csv", {"PBA"})
        f = open("resumen_dataset_v7.csv", encoding="utf-8")
        lector = csv.DictReader(f)
    
        provincias_en_archivo:set[str] = set()
        #comparamos los resumenes del archivo creado con los que tien el objeto p
        for fila in lector:
            provincia:str=fila["provincia"]
            provincias_en_archivo.add(provincia)
            resumen:Resumen = p.resumen_provincia(provincia)
            self.assertEqual(int(fila["cantidad"]), resumen.cantidad)
            self.assertAlmostEqual(float(fila["promedio_matematica"]), resumen.promedio_matematica)
            self.assertAlmostEqual(float(fila["promedio_lengua"]), resumen.promedio_lengua)
            self.assertAlmostEqual(float(fila["promedio_nse"]), resumen.promedio_nse)
            self.assertAlmostEqual(float(fila["proporcion_ambito_rural"]), resumen.proporcion_ambito_rural)
            self.assertAlmostEqual(float(fila["proporcion_sector_estatal"]), resumen.proporcion_sector_estatal)
    
    
        f.close()
        self.assertEqual(provincias_en_archivo, p.provincias)
        
        #Puntajes bajos
        p:Pais=Pais("Aprender2023_curado_v8.csv")
        p.exportar_por_provincias("resumen_dataset_v8.csv", {"PBA"})
        f = open("resumen_dataset_v8.csv", encoding="utf-8")
        lector = csv.DictReader(f)
    
        provincias_en_archivo:set[str] = set()
        for fila in lector:
            provincia:str=fila["provincia"]
            provincias_en_archivo.add(provincia)
            resumen:Resumen = p.resumen_provincia(provincia)
            self.assertEqual(int(fila["cantidad"]), resumen.cantidad)
            self.assertAlmostEqual(float(fila["promedio_matematica"]), resumen.promedio_matematica)
            self.assertAlmostEqual(float(fila["promedio_lengua"]), resumen.promedio_lengua)
            self.assertAlmostEqual(float(fila["promedio_nse"]), resumen.promedio_nse)
            self.assertAlmostEqual(float(fila["proporcion_ambito_rural"]), resumen.proporcion_ambito_rural)
            self.assertAlmostEqual(float(fila["proporcion_sector_estatal"]), resumen.proporcion_sector_estatal)
    
    
        f.close()
        self.assertEqual(provincias_en_archivo, p.provincias)
        
    
    def test_exportar_por_provincias_dataset_vacio(self):
        p:Pais=Pais("Aprender2023_curado_v3.csv")
        p.exportar_por_provincias("resumen_dataset_v3.csv", {})
        f = open("resumen_dataset_v3.csv", encoding="utf-8")
        lector = csv.DictReader(f)
    
        provincias_en_archivo:set[str] = set()
        #comparamos los resumenes del archivo creado con los que tien el objeto p
        for fila in lector:
            provincia:str=fila["provincia"]
            provincias_en_archivo.add(provincia)
            resumen:Resumen = p.resumen_provincia(provincia)
            self.assertEqual(int(fila["cantidad"]), resumen.cantidad)
            self.assertAlmostEqual(float(fila["promedio_matematica"]), resumen.promedio_matematica)
            self.assertAlmostEqual(float(fila["promedio_lengua"]), resumen.promedio_lengua)
            self.assertAlmostEqual(float(fila["promedio_nse"]), resumen.promedio_nse)
            self.assertAlmostEqual(float(fila["proporcion_ambito_rural"]), resumen.proporcion_ambito_rural)
            self.assertAlmostEqual(float(fila["proporcion_sector_estatal"]), resumen.proporcion_sector_estatal)
    
    
        f.close()
        self.assertEqual(provincias_en_archivo, p.provincias)
    
    def test_exportar_por_provincias_mismos_atributos(self):
        #solo tiene provincia PBA
        p:Pais=Pais("Aprender2023_curado_v11.csv")
        p.exportar_por_provincias("resumen_dataset_v11.csv", {"PBA"})
        f = open("resumen_dataset_v11.csv", encoding="utf-8")
        lector = csv.DictReader(f)
    
        provincias_en_archivo:set[str] = set()
        #comparamos los resumenes del archivo creado con los que tien el objeto p
        for fila in lector:
            provincia:str=fila["provincia"]
            provincias_en_archivo.add(provincia)
            resumen:Resumen = p.resumen_provincia(provincia)
            self.assertEqual(int(fila["cantidad"]), resumen.cantidad)
            self.assertAlmostEqual(float(fila["promedio_matematica"]), resumen.promedio_matematica)
            self.assertAlmostEqual(float(fila["promedio_lengua"]), resumen.promedio_lengua)
            self.assertAlmostEqual(float(fila["promedio_nse"]), resumen.promedio_nse)
            self.assertAlmostEqual(float(fila["proporcion_ambito_rural"]), resumen.proporcion_ambito_rural)
            self.assertAlmostEqual(float(fila["proporcion_sector_estatal"]), resumen.proporcion_sector_estatal)
    
    
        f.close()
        self.assertEqual(provincias_en_archivo, p.provincias)
        
        
        
        
####################################################################

unittest.main()
