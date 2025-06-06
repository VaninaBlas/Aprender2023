from resumen import Resumen
# from typing import cast
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

        for fila in csv.DictReader(open(self.archivo_csv)):
            # Asumiendo que cada fila es un objeto Estudiante
            self.provincias.add(fila["provincia"])
        pass
   
    def tamano(self) -> int:
        ''' devuelve la cantidad de lineas del archivo CSV '''
        return len(open(self.archivo_csv).readlines()) # no estoy seguro si es O(1) creo que si

    def resumen_provincia(self, provincia: str) -> Resumen:
        ''' completar docstring '''
        cantidad:int = 0
        promedio_matematica:float = 0.0
        promedio_lengua:float = 0.0
        promedio_nse:float = 0.0
        proporcion_ambito_rural:float = 0.0
        proporcion_sector_estatal:float = 0.0
        for fila in csv.DictReader(open(self.archivo_csv)):
            if fila["provincia"] == provincia:
                cantidad += 1
                promedio_matematica += float(fila["mpuntaje"])
                promedio_lengua += float(fila["lpuntaje"])
                promedio_nse += float(fila["NSE_puntaje"])
                if fila["ambito"] == "Rural":
                    proporcion_ambito_rural += 1
                if fila["sector"] == "Estatal":
                    proporcion_sector_estatal += 1
        promedio_matematica = promedio_matematica / cantidad if cantidad > 0 else 0.0
        promedio_lengua = promedio_lengua / cantidad if cantidad > 0 else 0.0
        promedio_nse = (promedio_nse / cantidad) if cantidad > 0 else 0.0
        if(proporcion_ambito_rural == cantidad):
            proporcion_ambito_rural = 1.0
        elif proporcion_ambito_rural != 0.0 and cantidad != 0.0:
            proporcion_ambito_rural = proporcion_ambito_rural / cantidad
        if(proporcion_sector_estatal == cantidad):
            proporcion_sector_estatal = 1.0
        elif proporcion_sector_estatal != 0.0 and cantidad != 0.0:
            proporcion_sector_estatal = proporcion_sector_estatal / cantidad if cantidad > 0 else 0.0
        return Resumen(cantidad, promedio_matematica, promedio_lengua, promedio_nse, proporcion_ambito_rural, proporcion_sector_estatal)
    
    def resumenes_pais(self) -> dict[str, Resumen]:
        ''' completar docstring '''
        provincias: dict[str, Resumen] = {}
        for fila in csv.DictReader(open(self.archivo_csv)):
            provincia = fila["provincia"]
            if provincia not in provincias:
                provincias[provincia] = Resumen(0, 0.0, 0.0, 0.0, 0.0, 0.0)
            provincias[provincia].cantidad += 1
            provincias[provincia].promedio_matematica += float(fila["mpuntaje"])
            provincias[provincia].promedio_lengua += float(fila["lpuntaje"])
            provincias[provincia].promedio_nse += float(fila["NSE_puntaje"])
            if fila["ambito"] == "Rural":
                provincias[provincia].proporcion_ambito_rural += 1
            if fila["sector"] == "Estatal":
                provincias[provincia].proporcion_sector_estatal += 1
        for provincia in provincias.values():
            if provincia.cantidad > 0:
                provincia.promedio_matematica /= provincia.cantidad
                provincia.promedio_lengua /= provincia.cantidad
                provincia.promedio_nse /= provincia.cantidad
                if provincia.proporcion_ambito_rural > 0:
                    provincia.proporcion_ambito_rural /= provincia.cantidad
                if provincia.proporcion_sector_estatal > 0:
                    provincia.proporcion_sector_estatal /= provincia.cantidad
        return provincias    
    def estudiantes_en_intervalo(self, categoria: str, x: float, y: float, provincias: str) -> int:
        ''' completar docstring '''
        # p >= x and p < y while provincias == p and
        alum: int = 0
        for fila in csv.DictReader(open(self.archivo_csv)):
            if fila["provincia"] == provincias:
                if categoria == "mat":
                    if float(fila["mpuntaje"]) >= x and float(fila["mpuntaje"]) < y:
                        alum += 1
                elif categoria == "len":
                    if float(fila["lpuntaje"]) >= x and float(fila["lpuntaje"]) < y:
                        alum += 1
                elif categoria == "nse":
                    if float(fila['NSE_nivel']) >= x and float(fila['NSE_nivel']) < y:
                        alum += 1
        return alum
   
    def exportar_por_provincias(self, archivo_csv: str, provincias: list[str]) -> None:
        ''' completar docstring '''
        with open(archivo_csv, 'w', newline='') as csvfile:
            fieldnames = ['provincia', 'mpuntaje', 'lpuntaje', 'NSE_puntaje', 'ambito', 'sector']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for fila in csv.DictReader(open(self.archivo_csv)):
                if fila["provincia"] in provincias:
                    writer.writerow({
                        'provincia': fila['provincia'],
                        'mpuntaje': fila['mpuntaje'],
                        'lpuntaje': fila['lpuntaje'],
                        'NSE_puntaje': fila['NSE_puntaje'],
                        'ambito': fila['ambito'],
                        'sector': fila['sector']
                    })
        pass
print(Pais("Aprender2023_curado.csv").tamano())