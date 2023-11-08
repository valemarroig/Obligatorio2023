class Mecanico(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score  # Número entero del 1 al 99 que representa la habilidad del mecánico

    def __str__(self):
        return f"Mecánico: {self.nombre} (ID: {self.id}, Score: {self.score})"

  # Getter y Setter específico para Mecanico
    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score


