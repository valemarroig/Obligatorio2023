class Auto:
    def __init__(self, modelo, año, score, num_auto):
        self._modelo = modelo
        self._año = año
        self._score = score
        self._num_auto= num_auto

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
    
    @property
    def num_auto(self):
        return self._num_auto

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
        
    @num_auto.setter
    def num_auto(self, nuevo_num_auto):
        self._num_auto = nuevo_num_auto