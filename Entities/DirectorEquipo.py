from .Empleado import Empleado

class DirectorEquipo(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)

    def __str__(self):
        return f"Director de Equipo: {self.nombre} (ID: {self.id})"
