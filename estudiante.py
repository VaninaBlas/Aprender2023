# from typing import Literal 

''' definimos tipos necesarios para class Estudiante,
 el tipo de ambito que es o "urbano" o "rurral"
  y el tipo de sector que es "estatal" o "privado"
  '''
# type ambitoType = Literal['urbano', 'rural']
# type sectorType = Literal["estatal", "privado"]
class Estudiante(object):
    def __init__(self, provincia:str, puntaje_matematica: float, puntaje_lengua: float, puntaje_nse: float, ambito: str, sector: str):
        ''' clase que representa un estudiante con sus datos de provincia, puntajes y ambito/sector '''
        if ambito not in ['urbano', 'rural']:
            raise ValueError("El ambito debe ser 'urbano' o 'rural'")
        if sector not in ['estatal', 'privado']:
            raise ValueError("El sector debe ser 'estatal' o 'privado'")
        self.provincia: str = provincia
        self.puntaje_matematica: float = puntaje_matematica
        self.puntaje_lengua: float = puntaje_lengua
        self.puntaje_nse: float = puntaje_nse
        self.ambito: str = ambito
        self.sector: str = sector
        pass

# <Mat:FLOAT, Len:FLOAT, NSE:FLOAT, AMBITO, SECTOR, PROVINCIA>
    def __repr__(self) -> str:
        ''' metodo que devuelve una representacion del objeto Estudiante '''
        return f'<Mat: {round(self.puntaje_matematica, 2)}, Len: {round(self.puntaje_lengua, 2)}, NSE: {round(self.puntaje_nse, 2)}, AMBITO: {self.ambito}, SECTOR: {self.sector}, PROVINCIA: {self.provincia}>'

    def __eq__(self, otro: object) -> bool:
        ''' compara dos objetos Estudiante para ver si son iguales
            dos estudiantes son iguales si tienen la misma provincia, puntajes, ambito y sector'''
        if not isinstance(otro, Estudiante):
            return False
        if(self.provincia == otro.provincia and
           self.puntaje_matematica == otro.puntaje_matematica and
           self.puntaje_lengua == otro.puntaje_lengua and
           self.puntaje_nse == otro.puntaje_nse and
           self.ambito == otro.ambito and
           self.sector == otro.sector):
            return True
        return False

