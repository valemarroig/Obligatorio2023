class InformacionInvalida(Exception):
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion