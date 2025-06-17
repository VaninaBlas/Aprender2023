from resumen import Resumen
from estudiante import Estudiante

import csv

class Pais:
    def __init__(self, archivo_csv:str):
        '''
        inicializa la clase Pais, cargando los estudiantes y registrando las provincias presentes en el 
        archivo archivo_csv.
        
        Requiere: archivo_csv es el nombre de un archivo en formato CSV,  con muchas columnas pero las que usamos
        son 6: "provincia" (str con 3 letras), mpuntaje (float), lpuntaje (float),  NSE_puntaje (float),
        "ambito" (string donde los strings posibles son "rural" o "urbano"), "sector" (string donde los strings
        posibles son "estatal" o "privado")
        Nota: el archivo no contiene estudiantes con idalumno repetido (cada fila corresponde a un estudiante único).
        '''
        # variables que se usaran en las funciones
        self.provincias: set[str] = set() # guardara las provincias presentes en el archivo_csv
        self.estudiantes:list[Estudiante]=[] # lista de estudiantes cargados
        f=open(archivo_csv, encoding="utf-8") # para abrir el archivo csv en modo lectura
        for linea in csv.DictReader(f): # leemos el archivo, una linea por vez
            #linea es un dict[str, str]
            #vamos a tomar algunas claves del diccionario y guardar sus valores en las variables correspondientes.
            self.provincias.add(linea["provincia"])
            #se crea una instancia del objeto Estudiante, algunos de los valores del dict que originalmente eran strings son convertidos en floats
            estudiante:Estudiante=Estudiante(linea["provincia"],float(linea["mpuntaje"]),float(linea["lpuntaje"]),float(linea["NSE_puntaje"]), linea["ambito"],linea["sector"])
            self.estudiantes.append(estudiante) 
        f.close() # cerrar el archivo
    def tamano(self) -> int:
        ''' 
        Requiere:nada
        Devuelve: la cantidad de estudiantes en el dataset 
        ''' 
        return len(self.estudiantes) #o(1)

    def resumen_provincia(self, provincia: str) -> Resumen:
        ''' 
        Requiere: nada
        Devuelve: un objeto de la clase Resumen, que encapsula ciertas estadísticas para la provincia dada.
        Puede devolver un resumen vacío si no hay estudiantes para esa provincia.
        '''
 
        lista_estudiante_provincia:list[Estudiante]=[] #o(1)
        #recorremos todos los estudiantes, si su provincia coincide con la solicitada, lo agregamos a la lista
        for estudiante in self.estudiantes:  #o(n)
            if estudiante.provincia == provincia: #o(1)
                lista_estudiante_provincia.append(estudiante) #o(1)
                
        return Resumen(lista_estudiante_provincia) #o(1)
    
    def resumenes_pais(self) -> dict[str, Resumen]:
        '''
        Requiere: nada 
        Devuelve: un diccionario donde las claves son las provincias presentes
        en el objeto y los valores son sus resúmenes correspondientes '''
        provincias_con_resumenes: dict[str, Resumen] = {} #o(1)
        #recorremos todas las provincias presentes, y guardamos un resumen de cada una                
        for provincia in self.provincias: #o(p)
            provincias_con_resumenes[provincia] = self.resumen_provincia(provincia) #o(n)
        return provincias_con_resumenes #o(1)
    def estudiantes_en_intervalo(self, categoria: str, x: float, y: float, provincias:set[str]) -> int:
        ''' 
        Requiere: categoria es un string que toma el valor "mat", "len" o "nse". Todas las provincias en el conjunto
        provincias estan presentes en self.provincias. x<y
        Devuelve: la cantidad de estudiantes de las provincias indicadas que tienen un puntaje en 
        matemática, lengua o nivel socioeconómico (según corresponda) mayor o igual que x y menor estricto que y'''
        cantidad_estudiantes: int = 0 #o(1)
        # verificamos que provincias de interes estan presentes en el objeto
        for provincia in self.provincias: #o(p)
            if provincia in provincias: # si la provincia esta entre las indicadas #o(1)
                # si el estudiante es de la provincia actual y su puntaje esta en el intervalo, se cuenta
                for estudiante in self.estudiantes: #o(n)
                    if estudiante.provincia == provincia: #o(1)
                        if categoria == "mat": #o(1)
                            if estudiante.puntaje_matematica >= x and estudiante.puntaje_matematica < y: #o(1)
                                cantidad_estudiantes += 1 #o(1)
                        elif categoria == "len": #o(1)
                            if estudiante.puntaje_lengua >= x and estudiante.puntaje_lengua < y: #o(1)
                                cantidad_estudiantes += 1 #o(1)
                        else: # se refiere a la categoria "nse" #o(1)
                            if estudiante.puntaje_nse >= x and estudiante.puntaje_nse < y: #o(1)
                                cantidad_estudiantes += 1 #o(1)
        return cantidad_estudiantes #o(1)
   
    def exportar_por_provincias(self, archivo_csv: str, provincias: set[str]):
        ''' 
        genera un nuevo archivo con nombre archivo_csv, con una fila por cada una de las provincias indicadas. El 
        archivo debe tener las siguientes columnas: provincia (código de 3 letras),
        cantidad (de estudiantes), promedio_matematica, promedio_lengua, promedio_nse,
        proporcion_ambito_rural, proporcion_sector_estatal. Los valores de las columnas
        corresponden a las estadísticas de interés descriptas en la clase Resumen
        Requiere: Todas las provincias en el conjunto provincias esten presentes en self.provincias.
        '''
        # Abrimos el archivo en modo escritura (se crea si no existe y se sobreescribe si ya existe)
        f=open(archivo_csv, "w")
        #añadimos la primera linea que seran sus columnas
        f.write("provincia,cantidad,promedio_matematica,promedio_lengua,promedio_nse,proporcion_ambito_rural,proporcion_sector_estatal\n")
        # recorremos el conjunto de provincias, y escribimos una linea por cada resumen
        for provincia in provincias:
            resumen=self.resumen_provincia(provincia)
            f.write(provincia+ ","+ str(resumen.cantidad)+","+str(resumen.promedio_matematica)+","+str(resumen.promedio_lengua) + ","+ str(resumen.promedio_nse) +","+str(resumen.proporcion_ambito_rural)+","+str(resumen.proporcion_sector_estatal)+ "\n")
        f.close() #cerramos el archivo

print(Pais("Aprender2023_curado_v4.csv").resumen_provincia("MZA").promedio_nse)