from estudiante import Estudiante
class Resumen():
    def __init__(self, lista_estudiantes:list[Estudiante]):
        ''' 
        Inicializa un resumen con estadisticas calculadas a partir de una lista de estudiantes
        Nota: el atributo "provincia" de los estudiantes no se utiliza en esta clase
        y no requiere que len(lista_estudiantes)>0 para usarlo en casos de test.
        - cantidad: cantidad total de estudiantes en la lista.
        - promedio_matematica: promedio de los puntajes de matemática.
        - promedio_lengua: promedio de los puntajes de lengua.
        - promedio_nse: promedio de los puntajes de nivel socioeconómico.
        - proporcion_ambito_rural: proporción de estudiantes cuyo ámbito es "Rural".
        - proporcion_sector_estatal: proporción de estudiantes cuyo sector es "Estatal".      
        '''

        self.cantidad: int = len(lista_estudiantes)
        self.promedio_matematica:float=0.0
        self.promedio_lengua:float = 0.0
        self.promedio_nse:float = 0.0
        self.proporcion_ambito_rural:float= 0.0
        self.proporcion_sector_estatal:float = 0.0
        # recorremos la lista de estudiantes y acumulamos sus puntajes y conteos segun el ambito y sector
        for estudiante in lista_estudiantes:    
            self.promedio_matematica+= estudiante.puntaje_matematica
            self.promedio_lengua += estudiante.puntaje_lengua
            self.promedio_nse += estudiante.puntaje_nse
            if estudiante.ambito == "Rural":
                self.proporcion_ambito_rural += 1
            if estudiante.sector == "Estatal":
                self.proporcion_sector_estatal += 1
        # si hay al menos un estudiante, calculamos los promedios y proporciones correspondientes
        if(self.cantidad>0):
            self.promedio_matematica=self.promedio_matematica/self.cantidad
            self.promedio_lengua = self.promedio_lengua / self.cantidad 
            self.promedio_nse = (self.promedio_nse / self.cantidad)
            self.proporcion_ambito_rural= self.proporcion_ambito_rural/self.cantidad
            self.proporcion_sector_estatal = self.proporcion_sector_estatal / self.cantidad

    def __repr__(self) -> str:
        ''' 
            Requiere:nada
            Devuelve: una representación como string del objeto Resumen, con el siguiente formato:
            <Mat:FLOAT, Len:FLOAT, NSE:FLOAT, Rural:FLOAT, Estado:FLOAT, N:INT>, donde FLOAT son numeros con
            exactamente dos digitos de decimales y N es un numero entero.
        '''
        return f'<Mat:{self.promedio_matematica:.2f}, Len:{self.promedio_lengua:.2f}, NSE:{self.promedio_nse:.2f}, Rural:{self.proporcion_ambito_rural:.2f}, Estado:{self.proporcion_sector_estatal:.2f}, N:{self.cantidad}>'

    def __eq__(self, otro) -> bool:
        ''' 
            Requiere: otro debe ser un objeto de la clase Resumen
            Devuelve:True si dos objetos Resumen tienen la misma cantidad y sus promedios de matematica, lengua, nse,
            asi como las proporciones de ambito rural y sector estatal, difieren en menos de 0.001, False si no
        '''
        vr:bool=False
        if(self.cantidad == otro.cantidad and
           (abs(self.promedio_matematica - otro.promedio_matematica)<0.001) and
           (abs(self.promedio_lengua - otro.promedio_lengua)<0.001) and
           (abs(self.promedio_nse - otro.promedio_nse)<0.001) and
           (abs(self.proporcion_ambito_rural - otro.proporcion_ambito_rural)<0.001) and
           (abs(self.proporcion_sector_estatal - otro.proporcion_sector_estatal)<0.001)):
            vr=True
        return vr
    

