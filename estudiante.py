class Estudiante():
    def __init__(self, provincia:str, puntaje_matematica: float, puntaje_lengua: float, puntaje_nse: float, ambito: str, sector: str):
        ''' Inicializa un estudiante con provincia provincia, puntaje_matematica puntaje_matematica, puntaje_lengua
        puntaje_lengua, puntaje_nse puntaje_nse, ambito ambito, sector sector'''
        self.provincia: str = provincia
        self.puntaje_matematica: float = puntaje_matematica
        self.puntaje_lengua: float = puntaje_lengua
        self.puntaje_nse: float = puntaje_nse
        self.ambito: str = ambito
        self.sector: str = sector


    def __repr__(self) -> str:
        ''' Requiere: self.ambito es un string que toma el valor "Rural" o "Urbano", self.sector es un string que toma el valor
            "Estatal" o "Privado", self.provincia es un string de 3 letras ("MZA","SFE","CHU", etc)
            Devuelve: una representación como string del objeto Estudiante, con el siguiente 
            formato: <Mat:FLOAT, Len:FLOAT, NSE:FLOAT, AMBITO, SECTOR, PROVINCIA>, donde FLOAT son numeros con
            exactamente dos digitos de decimales
        '''
        return f'<Mat:{self.puntaje_matematica:.2f}, Len:{self.puntaje_lengua:.2f}, NSE:{self.puntaje_nse:.2f}, {self.ambito}, {self.sector}, {self.provincia}>'

    def __eq__(self, otro) -> bool:
        ''' 
            Requiere:otro debe ser un objeto de la clase Estudiante
            Devuelve: True si dos objetos Estudiante tienen provincia, ambito y sector iguales y
            los puntajes de matematica, lengua, nse difieren en menos de 0.001, False si no
        '''
        vr:bool=False
        if(self.provincia == otro.provincia and
           (abs(self.puntaje_matematica - otro.puntaje_matematica)<0.001) and
           (abs(self.puntaje_lengua - otro.puntaje_lengua) < 0.001)and
           (abs(self.puntaje_nse - otro.puntaje_nse) <0.001)and
           self.ambito == otro.ambito and
           self.sector == otro.sector):
            vr=True
        return vr
