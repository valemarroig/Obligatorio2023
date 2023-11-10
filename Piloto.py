from Empleado import Empleado

class Piloto(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score, num_auto, puntaje_campeonato, lesionado):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score  # Número entero del 1 al 99 que representa la habilidad del piloto
        self.num_auto = num_auto  # Número de auto asignado al piloto
        self.puntaje_campeonato = puntaje_campeonato  # Puntaje acumulado en el campeonato
        self.lesionado = lesionado  # Booleano que indica si el piloto está lesionado o no

    def __str__(self):
        return f"Piloto: {self.nombre} (ID: {self.id}, Número de Auto: {self.num_auto}, Puntaje: {self.puntaje_campeonato}, Lesionado: {self.lesionado})"

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
    def set_score(self, score):
        return self._score=score

    @property
    def set_num_auto(self, num_auto):
        self._num_auto= num_auto

    @property
    def set_puntaje_campeonato(self,puntaje_campeonato):
        self._puntaje_campeonato=puntaje_campeonato):

    @property
    def set._lesionado(self, lesionado):
        self._lesionado=lesionado

    def __str__(self):
        return f"Piloto: {self.nombre} (ID: {self.id}, Numero de Auto: {self._num_auto}, Puntaje: {self._puntaje_campeonato}, Lesionado: {self._lesionado})"
        
        
    
        
