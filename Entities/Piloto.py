from .Empleado import Empleado
from .Auto import Auto


class Piloto(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score, num_auto, puntaje_campeonato, lesionado, esReserva):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score  # Número entero del 1 al 99 que representa la habilidad del piloto
        self.num_auto = num_auto  # Número de auto asignado al piloto
        self.puntaje_campeonato = puntaje_campeonato  # Puntaje acumulado en el campeonato
        self.lesionado = lesionado  # Booleano que indica si el piloto está lesionado o nos
        self.esReserva = esReserva
        self.errores_en_pits = 0
        self.penalidad_infringir_norma = 0
        
    def __str__(self):
        return f"Piloto: {super().nombre} (ID: {super().id}, Número de Auto: {self.num_auto}, Puntaje: {self.puntaje_campeonato}, Lesionado: {self.lesionado})"

    @property
    def get_score(self):
        return self._score

    @property
    def get_num_auto(self):
        return self._num_auto

    @property
    def get_puntaje_campeonato(self):
        return self._puntaje_campeonato
    
    @property
    def get_lesionado(self):
        return self._lesionado

    @property
    def set_score(self, nuevo_score):
        self._score = nuevo_score

    @property
    def set_num_auto(self, nuevo_num_auto):
        self._num_auto= nuevo_num_auto

    @property
    def set_puntaje_campeonato(self, nuevo_puntaje_campeonato):
        self._puntaje_campeonato=nuevo_puntaje_campeonato

    @property
    def set_lesionado(self, nuevo_lesionado):
        self._lesionado=nuevo_lesionado
        
        
    def calcular_score_final(self, score_auto):
        if self.lesionado:
            self.puntaje_campeonato = 0
        else:
            self.puntaje_campeonato = (score_auto + self.score-5 * self.errores_en_pits - 8 * self.penalidad_infringir_norma)

    def recibir_penalidad_pits(self):
        self.errores_en_pits += 1

    def recibir_penalidad_norma(self):
        self.penalidad_infringir_norma += 1

    def asignar_puntaje(self,score_final):
        self.puntaje_campeonato += score_final
        
        
    
        
