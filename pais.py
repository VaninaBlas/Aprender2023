from resumen import Resumen
from estudiante import Estudiante
import csv


class Pais:
    def __init__(self, archivo_csv:str):
        ''' inicializa la clase Pais con el archivo CSV que contiene los datos de los estudiantes '''
        if not archivo_csv.endswith('.csv'):
            raise ValueError("El archivo debe ser un CSV")
        if not archivo_csv:
            raise ValueError("El archivo no puede estar vacío")
        self.archivo_csv = archivo_csv
        self.provincias: set[str] = set()
        self.estudiantes: list[Estudiante] = []
        arch = open(self.archivo_csv)
        for fila in csv.DictReader(arch):
            # Asumiendo que cada fila es un objeto Estudiante
            self.provincias.add(fila["provincia"])
            self.estudiantes.append(Estudiante(
                fila["provincia"],
                float(fila["mpuntaje"]),
                float(fila["lpuntaje"]),
                float(fila["NSE_puntaje"]),
                fila["ambito"],
                fila["sector"]
            ))
        arch.close()
   
    def tamano(self) -> int:
        ''' devuelve la cantidad de lineas del archivo CSV '''
        return len(self.estudiantes)

    def resumen_provincia(self, provincia: str) -> Resumen:
        ''' devuelve un Resumen con los datos de la provincia especificada '''
        cantidad:int = 0 # cantidad de estudiantes
        promedio_matematica:float = 0.00 # inicializamos variable para guardar todas las notas de matematica y luego dividir por la cantidad de estudiantes
        promedio_lengua:float = 0.00 # inicializamos variable para guardar todas las notas de lengua y luego dividir por la cantidad de estudiantes
        promedio_nse:float = 0.00 # inicializamos variable para guardar todas las notas de NSE y luego dividir por la cantidad de estudiantes
        # inicializamos variables para guardar la proporcion de estudiantes en ambito rural y sector estatal
        proporcion_ambito_rural:float = 0.00
        proporcion_sector_estatal:float = 0.00
        archivo = open(self.archivo_csv) # abrimos el archivo CSV
        for fila in csv.DictReader(archivo):
            # nos fijamos si en la fila actual la provincia es la que buscamos
            if fila["provincia"] == provincia:
                # en caso de que si, sumamos 1 a la cantidad de estudiantes
                # y sumamos los puntajes de matematica, lengua y NSE
                cantidad += 1
                promedio_matematica += float(fila["mpuntaje"])
                promedio_lengua += float(fila["lpuntaje"])
                promedio_nse += float(fila["NSE_puntaje"])
                # si el ambito es rural, sumamos 1 a la proporcion de ambito rural
                if fila["ambito"] == "Rural":
                    proporcion_ambito_rural += 1
                # si el sector es estatal, sumamos 1 a la proporcion de sector estatal
                if fila["sector"] == "Estatal":
                    proporcion_sector_estatal += 1
        archivo.close() # cerramos el archivo CSV
        # calculamos los promedios dividiendo la suma de puntajes por la cantidad de estudiantes
        # si la cantidad es 0, el promedio sera 0.00
        promedio_matematica = promedio_matematica / cantidad if cantidad > 0 else 0.00
        promedio_lengua = promedio_lengua / cantidad if cantidad > 0 else 0.00
        promedio_nse = (promedio_nse / cantidad) if cantidad > 0 else 0.00
        if(proporcion_ambito_rural == cantidad and cantidad != 0):
            proporcion_ambito_rural = 1.0
        elif proporcion_ambito_rural != 0.00 and cantidad != 0.00:
            proporcion_ambito_rural = proporcion_ambito_rural / cantidad
        if(proporcion_sector_estatal == cantidad and cantidad != 0):
            proporcion_sector_estatal = 1.0
        elif proporcion_sector_estatal != 0.00 and cantidad != 0.00:
            proporcion_sector_estatal = proporcion_sector_estatal / cantidad if cantidad > 0 else 0.00
        # devolvemos un Resumen con los datos de la provincia
        return Resumen(cantidad, promedio_matematica, promedio_lengua, promedio_nse, proporcion_ambito_rural, proporcion_sector_estatal)
    
    def resumenes_pais(self) -> dict[str, Resumen]:
        ''' devuelve un diccionario con los Resumenes de todas las provincias del pais '''
        provincias: dict[str, Resumen] = {} # diccionario donde la clave es el nombre de la provincia y el valor es un Resumen
        # por cada provincia en el conjunto de provincias, obtenemos su Resumen
        # y lo agregamos al diccionario provincias
        for provincia in self.provincias:
            provincias[provincia] = self.resumen_provincia(provincia)
        return provincias    
    def estudiantes_en_intervalo(self, categoria: str, x: float, y: float, provincias: str) -> int:
        ''' devuelve la cantidad de estudiantes que cumplen con las condiciones: x >= puntaje_categoria < y
        donde categoria puede ser "mat", "len" o "nse" y provincias es el nombre de la provincia '''
        # p >= x and p < y while provincias == p and
        alum: int = 0 # contador de estudiantes que cumplen con las condiciones
        arch = open(self.archivo_csv) # abrimos el archivo CSV
        # leemos el archivo CSV y por cada fila, verificamos si la provincia es la que buscamos
        for fila in csv.DictReader(arch):
            if fila["provincia"] == provincias:
                # si la categoria es "mat", verificamos si el puntaje de matematica esta en el intervalo
                if categoria == "mat":
                    if float(fila["mpuntaje"]) >= x and float(fila["mpuntaje"]) < y:
                        # en caso de que si, sumamos 1 al contador de estudiantes
                        alum += 1
                # si la categoria es "len", verificamos si el puntaje de lengua esta en el intervalo
                elif categoria == "len":
                    if float(fila["lpuntaje"]) >= x and float(fila["lpuntaje"]) < y:
                        # en caso de que si, sumamos 1 al contador de estudiantes
                        alum += 1
                # si la categoria es "nse", verificamos si el puntaje de NSE esta en el intervalo
                elif categoria == "nse":
                    if float(fila['NSE_nivel']) >= x and float(fila['NSE_nivel']) < y:
                        # en caso de que si, sumamos 1 al contador de estudiantes
                        alum += 1
        arch.close() # cerramos el archivo CSV
        # devolvemos el contador de estudiantes que cumplen con las condiciones
        return alum
   
    def exportar_por_provincias(self, archivo_csv: str, provincias: list[str]) -> None:
        ''' exporta los datos de las provincias especificadas a un nuevo archivo CSV '''
        # creamos un nuevo archivo CSV con el nombre especificado
        with open(archivo_csv, 'w', newline='') as csvfile:
            # especificamos los nombres de las columnas que queremos en el archivo CSV
            fieldnames = ['provincia', 'mpuntaje', 'lpuntaje', 'NSE_puntaje', 'ambito', 'sector']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader() # escribimos el encabezado en el archivo CSV

            # por cada estudiante en la lista de estudiantes, verificamos si su provincia esta en la lista de provincias
            for estudiante in self.estudiantes:
                if estudiante.provincia in provincias:
                    # si es asi, escribimos sus datos en el archivo CSV
                    # usamos el metodo writerow del objeto writer para escribir una fila en el archivo CSV
                    writer.writerow({
                        'provincia': estudiante.provincia,
                        'mpuntaje': estudiante.puntaje_matematica,
                        'lpuntaje': estudiante.puntaje_lengua,
                        'NSE_puntaje': estudiante.puntaje_nse,
                        'ambito': estudiante.ambito,
                        'sector': estudiante.sector
                    })