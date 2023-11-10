class Auto:
    def __init__(self, modelo, año, score):
        self._modelo = modelo
        self._año = año
        self._score = score

    # Getters
    @property
    def modelo(self):
        return self._modelo

    @property
    def año(self):
        return self._año

    @property
    def score(self):
        return self._score

    # Setters
    @modelo.setter
    def modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    @año.setter
    def año(self, nuevo_año):
        self._año = nuevo_año

    @score.setter
    def score(self, nuevo_score):
        self._score = nuevo_score