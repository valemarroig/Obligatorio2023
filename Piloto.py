class Piloto(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score, num_auto, puntaje_campeonato, lesionado):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score  # Número entero del 1 al 99 que representa la habilidad del piloto
        self.num_auto = num_auto  # Número de auto asignado al piloto
        self.puntaje_campeonato = puntaje_campeonato  # Puntaje acumulado en el campeonato
        self.lesionado = lesionado  # Booleano que indica si el piloto está lesionado o no

    def __str__(self):
        return f"Piloto: {self.nombre} (ID: {self.id}, Número de Auto: {self.num_auto}, Puntaje: {self.puntaje_campeonato}, Lesionado: {self.lesionado})"
