
class Resumen(object):
    def __init__(self, cantidad: int, promedio_matematica: float, promedio_lengua: float, promedio_nse: float, proporcion_ambito_rural: float, proporcion_sector_estatal: float):
        ''' clase que representa un resumen de estudiantes con sus promedios y proporciones '''
        if proporcion_ambito_rural < 0 or proporcion_ambito_rural > 1:
            raise ValueError("La proporcion de ambito rural debe estar entre 0 y 1")
        if proporcion_sector_estatal < 0 or proporcion_sector_estatal > 1:
            raise ValueError("La proporcion de sector estatal debe estar entre 0 y 1")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser un self.promedio_nseero entero positivo")
        self.cantidad: int = cantidad
        self.promedio_matematica: float = promedio_matematica
        self.promedio_lengua: float = promedio_lengua
        self.promedio_nse: float = promedio_nse
        self.proporcion_ambito_rural: float = proporcion_ambito_rural
        self.proporcion_sector_estatal: float = proporcion_sector_estatal
        pass

# <Mat:FLOAT, Len:FLOAT, NSE:FLOAT, Rural:FLOAT, Estado:FLOAT, N:INT>,
    def __repr__(self) -> str:
        ''' metodo que devuelve una representacion del objeto Resumen '''
        return f'<Mat: {round(self.promedio_matematica, 2)}, Len: {round(self.promedio_lengua, 2)}, NSE: {round(self.promedio_nse, 2)}, Rural: {round(self.proporcion_ambito_rural, 2)}, Estado: {round(self.proporcion_sector_estatal, 2)}, N: {self.cantidad}>'

    def __eq__(self, otro: object) -> bool:
        ''' compara dos objetos Resumen para ver si son iguales
            dos resúmenes son iguales si tienen la misma cantidad, promedios y proporciones '''
        if not isinstance(otro, Resumen):
            return False
        if (self.cantidad == otro.cantidad and
            self.promedio_matematica == otro.promedio_matematica and
            self.promedio_lengua == otro.promedio_lengua and
            self.promedio_nse == otro.promedio_nse and
            self.proporcion_ambito_rural == otro.proporcion_ambito_rural and
            self.proporcion_sector_estatal == otro.proporcion_sector_estatal):
            return True
        return False

