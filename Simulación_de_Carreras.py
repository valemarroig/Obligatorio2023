from Entities.Piloto import Piloto
from Entities.Mecanico import Mecanico
from Entities.DirectorEquipo import DirectorEquipo
from Entities.Empleado import Empleado
from Entities.Auto import Auto

def Simulacion_de_Carreras():
  
    # Crear empleados
    piloto1 = Piloto(id="12345678", nombre="Piloto1", fecha_nacimiento="01/01/1990", nacionalidad="Nacionalidad1", salario=50000, score=85, num_auto=1, puntaje_campeonato=0, lesionado=False)
    piloto2 = Piloto(id="23456789", nombre="Piloto2", fecha_nacimiento="02/02/1995", nacionalidad="Nacionalidad2", salario=45000, score=78, num_auto=2, puntaje_campeonato=0, lesionado=False)
    piloto_reserva = Piloto(id="34567890", nombre="PilotoReserva", fecha_nacimiento="03/03/1985", nacionalidad="Nacionalidad3", salario=40000, score=80, num_auto=3, puntaje_campeonato=0, lesionado=False)

    mecanico1 = Mecanico(id="45678901", nombre="Mecanico1", fecha_nacimiento="04/04/1992", nacionalidad="Nacionalidad4", salario=40000, score=75)
    mecanico2 = Mecanico(id="56789012", nombre="Mecanico2", fecha_nacimiento="05/05/1988", nacionalidad="Nacionalidad5", salario=35000, score=70)

    director_equipo1 = DirectorEquipo(id="67890123", nombre="Director1", fecha_nacimiento="06/06/1980", nacionalidad="Nacionalidad6", salario=80000)

    # Crear autos
    auto1 = Auto(modelo="Modelo1", año=2023, score=90)

    # Crear equipo y asociar empleados y auto
    equipo1 = Equipo(nombre="Equipo1", modelo_auto=auto1)
    equipo1.asociar_empleado(piloto1)
    equipo1.asociar_empleado(piloto2)
    equipo1.asociar_empleado(piloto_reserva)
    equipo1.asociar_empleado(mecanico1)
    equipo1.asociar_empleado(mecanico2)
    equipo1.asociar_empleado(director_equipo1)

    # Simular carrera
    pilotos_lesionados = []  # Lista vacía, ningún piloto lesionado
    pilotos_abandonan = [2]  # Piloto2 abandona
    pilotos_error_pits = []  # Ningún piloto comete error en pits
    pilotos_penalidad = []  # Ningún piloto recibe penalidad

    equipo1.simular_carrera(pilotos_lesionados, pilotos_abandonan, pilotos_error_pits, pilotos_penalidad)

if __name__ == "__main__":
