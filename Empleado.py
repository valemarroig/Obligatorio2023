class Empleado:
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
        self._id = id
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento
        self._nacionalidad = nacionalidad
        self._salario = salario

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def get_nacionalidad(self):
        return self._nacionalidad

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario
