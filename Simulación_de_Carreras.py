from datetime import datetime
from Entities.Piloto import Piloto
from Entities.Mecanico import Mecanico
from Entities.DirectorEquipo import DirectorEquipo
from Entities.Auto import Auto
from Entities.Equipo import Equipo
from Exceptions.InformaciónInválida import InformacionInvalida
import random

import re

class SimulacionDeCarrera:
    # para hacer pruebas: seleccionar y ctrl+/ para descomentar
    piloto1 = Piloto(id="12345678", nombre="Piloto1", fecha_nacimiento="01/01/1990", nacionalidad="Nacionalidad1", salario=50000, score=85, num_auto=1, puntaje_campeonato=0, lesionado=False, esReserva=False)
    piloto2 = Piloto(id="23456789", nombre="Piloto2", fecha_nacimiento="02/02/1991", nacionalidad="Nacionalidad2", salario=55000, score=78, num_auto=2, puntaje_campeonato=0, lesionado=False, esReserva=False)
    piloto3 = Piloto(id="34567890", nombre="Piloto3", fecha_nacimiento="03/03/1992", nacionalidad="Nacionalidad3", salario=60000, score=92, num_auto=3, puntaje_campeonato=0, lesionado=False, esReserva=True)
    piloto4 = Piloto(id="45678901", nombre="Piloto4", fecha_nacimiento="04/04/1993", nacionalidad="Nacionalidad4", salario=65000, score=88, num_auto=4, puntaje_campeonato=0, lesionado=False, esReserva=False)
    piloto5 = Piloto(id="56789012", nombre="Piloto5", fecha_nacimiento="05/05/1994", nacionalidad="Nacionalidad5", salario=70000, score=75, num_auto=5, puntaje_campeonato=0, lesionado=False, esReserva=False)
    piloto6 = Piloto(id="67890123", nombre="Piloto6", fecha_nacimiento="06/06/1995", nacionalidad="Nacionalidad6", salario=75000, score=95, num_auto=6, puntaje_campeonato=0, lesionado=False, esReserva=True)
    mecanico1 = Mecanico(id="12345678", nombre="Mecanico1", fecha_nacimiento="01/01/1990", nacionalidad="Nacionalidad1", salario=50000, score=85)
    mecanico2 = Mecanico(id="23456789", nombre="Mecanico2", fecha_nacimiento="02/02/1991", nacionalidad="Nacionalidad2", salario=55000, score=78)
    mecanico3 = Mecanico(id="34567890", nombre="Mecanico3", fecha_nacimiento="03/03/1992", nacionalidad="Nacionalidad3", salario=60000, score=92)
    mecanico4 = Mecanico(id="45678901", nombre="Mecanico4", fecha_nacimiento="04/04/1993", nacionalidad="Nacionalidad4", salario=65000, score=88)
    mecanico5 = Mecanico(id="56789012", nombre="Mecanico5", fecha_nacimiento="05/05/1994", nacionalidad="Nacionalidad5", salario=70000, score=75)
    mecanico6 = Mecanico(id="67890123", nombre="Mecanico6", fecha_nacimiento="06/06/1995", nacionalidad="Nacionalidad6", salario=75000, score=91)
    mecanico7 = Mecanico(id="78901234", nombre="Mecanico7", fecha_nacimiento="07/07/1996", nacionalidad="Nacionalidad7", salario=80000, score=83)
    mecanico8 = Mecanico(id="89012345", nombre="Mecanico8", fecha_nacimiento="08/08/1997", nacionalidad="Nacionalidad8", salario=85000, score=79)
    mecanico9 = Mecanico(id="90123456", nombre="Mecanico9", fecha_nacimiento="09/09/1998", nacionalidad="Nacionalidad9", salario=90000, score=94)
    mecanico10 = Mecanico(id="01234567", nombre="Mecanico10", fecha_nacimiento="10/10/1999", nacionalidad="Nacionalidad10", salario=95000, score=87)
    mecanico11 = Mecanico(id="12345000", nombre="Mecanico11", fecha_nacimiento="11/11/2000", nacionalidad="Nacionalidad11", salario=100000, score=89)
    mecanico12 = Mecanico(id="23456000", nombre="Mecanico12", fecha_nacimiento="12/12/2001", nacionalidad="Nacionalidad12", salario=105000, score=82)
    mecanico13 = Mecanico(id="34567000", nombre="Mecanico13", fecha_nacimiento="13/01/2002", nacionalidad="Nacionalidad13", salario=110000, score=90)
    mecanico14 = Mecanico(id="45678000", nombre="Mecanico14", fecha_nacimiento="14/02/2003", nacionalidad="Nacionalidad14", salario=115000, score=93)
    mecanico15 = Mecanico(id="56789000", nombre="Mecanico15", fecha_nacimiento="15/03/2004", nacionalidad="Nacionalidad15", salario=120000, score=86)
    mecanico16 = Mecanico(id="67890000", nombre="Mecanico16", fecha_nacimiento="16/04/2005", nacionalidad="Nacionalidad16", salario=125000, score=84)
    director_equipo1 = DirectorEquipo(id="12345678", nombre="Director1", fecha_nacimiento="01/01/1980", nacionalidad="Nacionalidad1", salario=150000)
    director_equipo2 = DirectorEquipo(id="23456789", nombre="Director2", fecha_nacimiento="02/02/1981", nacionalidad="Nacionalidad2", salario=160000)
    auto1 = Auto(modelo="Modelo1", año=2020, score=90, num_auto=1)
    auto2 = Auto(modelo="Modelo2", año=2021, score=85, num_auto=2)
    auto3 = Auto(modelo="Modelo3", año=2010, score=95, num_auto=3)
    auto4 = Auto(modelo="Modelo4", año=2011, score=70, num_auto=4)
    auto5 = Auto(modelo="Modelo5", año=2012, score=50, num_auto=5)
    auto6 = Auto(modelo="Modelo6", año=2013, score=40, num_auto=6)
    pilotos = [piloto1, piloto2, piloto3, piloto4, piloto5, piloto6]
    mecanicos = [mecanico1, mecanico2, mecanico3, mecanico4, mecanico5, mecanico6, mecanico7, mecanico8, mecanico9, mecanico10, mecanico11, mecanico12, mecanico13, mecanico14, mecanico15, mecanico16]
    autos = [auto1, auto2, auto3, auto4, auto5, auto6]
    
    pilotos = []
    pilotosReserva =[]
    mecanicos = []
    directores  = []
    autos = []
    equipos = []
    
    def menu_principal(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Alta de empleado")
            print("2. Alta de auto")
            print("3. Alta de equipo")
            print("4. Simular carrera")
            print("5. Realizar consultas")
            print("6. Finalizar programa")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.alta_empleado()
            elif opcion == "2":
                self.alta_auto()
            elif opcion == "3":
                self.alta_equipo()
            elif opcion == "4":
                self.simular_carrera()
            elif opcion == "5":
                self.realizar_consultas()
            elif opcion == "6":
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def alta_auto(self): #OK
        while True:
            try:
                print("\n--- Alta de Auto ---")    
                modelo = input("Ingrese modelo: ") #validar que no se repita el modelo (o mismo modelo y año al mismo tiempo)
                if not modelo.strip():
                    raise InformacionInvalida(400, "Dato ingresado incorrecto. El modelo no puede estar vacío.")
                
                anio = input("Ingrese año: ")
                if not self.validar_anio(anio):
                    raise InformacionInvalida(400, "El año ingresado no es válido.")
                
                score = input("Ingrese score: ")
                if not self.validar_num_entero_1_99(score):
                    raise InformacionInvalida(400, "Dato ingresado incorrecto. Score no puede estar vacío y debe ser un número entero en rango 1-99.")
                
                num_auto = input("Ingrese numero de auto: ")
                if not self.validar_num_entero_1_99(num_auto):
                    raise InformacionInvalida(400, "Dato ingresado incorrecto. Numero de auto no puede estar vacío y debe ser un número entero en rango 1-99.")
                
                autoCreado = Auto(modelo,anio, score, num_auto)
                self.autos.append(autoCreado)
                print(f"Auto {modelo}, {anio} dado de alta con éxito.")
                break
            
            except InformacionInvalida as e:
                print(f"Error: {e}")
                print("Por favor, ingrese la información nuevamente.")
                input ("Presionar Enter para volver al menú principal.")
                break

    def alta_equipo(self):
        print("\n--- Alta de Equipo ---")
                
        if len(self.autos) < 1:
            print("No hay autos disponibles para el equipo, agregue otro!")
            return
        
        if len(self.pilotos) < 2:
            print("No hay pilotos disponibles para el equipo, agregue otro!")
            return
        
        if len(self.pilotosReserva) < 1:
            print("No hay pilotos de reserva disponibles, agregue otro")
            return

        if len(self.mecanicos) < 8:
            print("No hay mecanicos disponibles, se necesitan 8 y hay: " + str(len(self.mecanicos)))
            return
        
        if len(self.directores) < 1:
            print("No hay directores disponibles, agregue otro")
            return
        
        nombre_equipo = input("Ingrese nombre del equipo: ")
        if not self.validar_texto(nombre_equipo):
            raise InformacionInvalida(400, "Dato ingresado incorrecto. Nombre de equipo no puede estar vacío y solo debe contener letras y espacios.")
                  
               
        # Seleccion de piloto
        print("Pilotos titulares:", [p.cedula for p in self.pilotos])

        pilotos_equipo = []
        for i in range(2):
            cedula_piloto_titular = input(f"Ingrese cedula del piloto titular {i + 1}: ")
            if cedula_piloto_titular not in [p.cedula for p in self.pilotos]:
                print("La cédula no corresponde a un piloto disponible.")
                return
            piloto_titular = next(p for p in self.pilotos if p.cedula == cedula_piloto_titular)
            pilotos_equipo.append(piloto_titular)
        
        print("Pilotos de reserva:", [p.cedula for p in self.pilotos_reserva])
        
        cedula_piloto_reserva = input("Ingrese cedula del piloto de reserva: ")
        if cedula_piloto_reserva not in [p.cedula for p in self.pilotos_reserva]:
            print("La cédula no corresponde a un piloto de reserva disponible.")
            return
        piloto_reserva = next(p for p in self.pilotos_reserva if p.cedula == cedula_piloto_reserva)
        pilotos_equipo.append(piloto_reserva)
        
        print("Directores:", [d.cedula for d in self.directores])
        
        idDir = input("Ingrese cedula del Director de equipo: ")
        if idDir not in [d.cedula for d in self.directores]:
            print("La cédula no corresponde a un director disponible.")
            return
        director_equipo = next(d for d in self.directores if d.cedula == idDir)
          
        print("Mecánicos:", [m.cedula for m in self.mecanicos])
        
        mecanicos_equipo = []
        for i in range(8):
            cedula_mecanico = input(f"Ingrese cedula del mecánico {i + 1}: ")
            if cedula_mecanico not in [m.cedula for m in self.mecanicos]:
                print("La cédula no corresponde a un mecánico disponible.")
                return
            mecanico = next(m for m in self.mecanicos if m.cedula == cedula_mecanico)
            mecanicos_equipo.append(mecanico)

        print("Equipo dado de alta con éxito.")
        
        # Falta> si encuentro algo y hago append, removerlo de la lista original (esto es para que un piloto no sea parte de dos equipos por lo menos)
        # Falta bucar auto por modelo y agregarlo al equipo
        autos_equipo = []
        for i in range(8):
            matricula_auto = input(f"Ingrese matricula del auto {i + 1}: ")
            if matricula_auto not in [m.matricula for m in self.autos]:
                print("La matricula no corresponde a un auto disponible.")
                return
            auto = next(m for m in self.autos if m.matricula == matricula_auto)
            autos_equipo.append(auto)
        # Falta tomar todos los datos elegidos y hacer append a la lista de equipos con un nuevo equipo generado (en base a los parametros)
        
        director_equipo = []
        cedula_director = input(f"Ingrese cedula del director {i + 1}: ")
        if cedula_director not in [m.cedula for m in self.directores]:
                print("La cédula no corresponde a un director disponible.")
                return
        director = next(m for m in self.directores if m.cedula == cedula_director)
        director_equipo.append(director)
        
        
        nuevo_equipo = Equipo(nombre_equipo, [auto], pilotos_equipo, [piloto_reserva], mecanicos_equipo, director_equipo)
        self.equipos.append(nuevo_equipo)   

     
     
    def simular_carrera(self):
        for piloto in self.pilotos:
                if random.random() < 0.1:  # 10% de probabilidad de lesión
                    piloto.lesionado = True
                if random.random() < 0.2:  # 20% de probabilidad de abandono
                    piloto.lesionado = True
                if random.random() < 0.3:  # 30% de probabilidad de error en pits
                 #   if auto.num_auto == piloto.num_auto():
                    piloto.recibir_penalidad_pits()
                if random.random() < 0.15:  # 15% de probabilidad de penalidad por norma
                    piloto.recibir_penalidad_norma()

        # Calcular score final para cada piloto
        for piloto in self.pilotos:
            for auto in self.autos:
                if auto.num_auto == piloto.num_auto:
                    piloto.calcular_score_final(auto.score)

        # Ordenar los pilotos por score_final de manera descendente
        self.pilotos.sort(key=lambda x: x.puntaje_campeonato, reverse=True)

        # Adjudicar puntos a los pilotos
        puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
        for i, piloto in enumerate(self.pilotos):
            piloto.asignar_puntaje(puntos[i])

        # Imprimir los puntajes de todos los pilotos
        for piloto in self.pilotos:
        #    print(f"Piloto {piloto.nombre}: Puntaje Campeonato = {piloto.puntaje_campeonato}")

            print(piloto._nacionalidad)
     
     
        
        
        
        
    def validar_anio(self, anio):
        try:
            anioIngresado = int(anio)
            anioActual = datetime.now().year
            if 0 <= anioIngresado <= anioActual:
                return True
        except ValueError:
            return False

    def validar_fecha(self, date_string):
        try:
            # Parse the input string as a date
            date_object = datetime.strptime(date_string, '%d/%m/%Y')
            return True
        except ValueError:
            return False
    
    def validar_id(self, id):
        es_id_valido = False
        if id.isdigit() and len(id) == 8:
            es_id_valido = True
        return es_id_valido  
        
    def validar_texto(self, texto):
        es_texto = False
        patron = re.compile(r'^[a-zA-Z\s]+$')
        if patron.match(texto) and texto.strip():
            es_texto = True
        return es_texto
        
    def validar_numero_positivo(self, valor):
        es_numero_positivo = False
        if valor.isdigit():
            numero = float(valor)
            if numero >= 0:
                es_numero_positivo = True
        return es_numero_positivo
    
    def validar_num_entero_1_99(self, valor):
        es_entero_1_99 = False
        if valor.isdigit():
            numero = int(valor)
            if 1<= numero <= 99:
                es_entero_1_99 = True
        return es_entero_1_99

    def alta_empleado(self):
        while True:
            try:
                print("\n--- Alta de Empleado ---")

                cedula = input("Ingrese cédula: ")  #validar que no se repita la cedula
                if not self.validar_id(cedula):  
                    raise InformacionInvalida(400, "Dato ingresado incorrecto. La cédula debe contener 8 dígitos numéricos.")
                    
                nombre = input("Ingrese nombre: ")
                if not self.validar_texto(nombre):
                    raise InformacionInvalida(400, "Dato ingresado incorrecto. Nombre no puede estar vacío y solo debe contener letras y espacios.")
                
                fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
                if not self.validar_fecha(fecha_nacimiento):
                    raise InformacionInvalida(400, "Dato ingresado incorrecto. Fecha no puede estar vacía y debe tener el formato incorrecto.")
                
                nacionalidad = input("Ingrese nacionalidad: ")
                if not self.validar_texto(nacionalidad):
                    raise InformacionInvalida(400, "Dato ingresado incorrecto. Nacionalidad no puede estar vacía y solo debe contener letras y espacios.")
                    
                salario = input("Ingrese salario: ")
                if not self.validar_numero_positivo(salario):
                    raise InformacionInvalida(400, "Dato ingresado incorrecto. Salario no puede estar vacío y debe ser un número positivo.")

                # Validar el cargo
                cargos_validos = ["1", "2", "3", "4"]
                print("Cargos disponibles:")
                print("1. Piloto")
                print("2. Piloto de reserva")
                print("3. Mecánico")
                print("4. Director de equipo")

                cargo = input("Ingrese el número del cargo: ")
                if cargo not in cargos_validos:
                    raise InformacionInvalida(400, "Cargo no válido. Ingrese una de las opciones presentadas.")    
                
                if cargo == "1":    
                    pilotoCreado = self.crearPiloto(cedula, nombre, fecha_nacimiento, nacionalidad, salario,  False)
                    self.pilotos.append(pilotoCreado)
                elif cargo == "2":
                    pilotoReservaCreado = self.crearPiloto(cedula, nombre, fecha_nacimiento, nacionalidad, salario, True)
                    self.pilotosReserva.append(pilotoReservaCreado)
                elif cargo == "3":
                    mecanicoCreado = self.crearMecanico(cedula, nombre, fecha_nacimiento, nacionalidad, salario)
                    self.mecanicos.append(mecanicoCreado)
                else:
                    directorCreado = self.crearDirector(cedula, nombre, fecha_nacimiento, nacionalidad, salario)
                    self.directores.append(directorCreado) 

                print(f"Empleado {nombre} dado de alta con éxito.")
                break
            
            except InformacionInvalida as e:
                print(f"Error: {e}")
                print("Por favor, ingrese la información nuevamente.")
                input ("Presionar Enter para volver al menú principal.")
                break


    def crearDirector(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario):
        return DirectorEquipo(cedula, nombre, fecha_nacimiento, nacionalidad, salario)

    def crearMecanico(self,cedula, nombre, fecha_nacimiento, nacionalidad, salario):
        score = input("Ingresar score: ")
        if not self.validar_num_entero_1_99(score):
            raise InformacionInvalida(400, "Dato ingresado incorrecto. Score no puede estar vacío y debe ser un número entero en rango 1-99.")
        
        return Mecanico(cedula, nombre, fecha_nacimiento, nacionalidad, salario, score)

    def crearPiloto(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, esReserva):
        score = input("Ingresar score: ")
        if not self.validar_num_entero_1_99(score):
            raise InformacionInvalida(400, "Dato ingresado incorrecto. Score no puede estar vacío y debe ser un número entero en rango 1-99.")
        
        num_auto = input("Ingrese número de auto: ")
        if not self.validar_num_entero_1_99(num_auto):
            raise InformacionInvalida(400, "Dato ingresado incorrecto. Número de auto no puede estar vacío y debe ser un número entero en rango 1-99.")

        return Piloto(cedula,nombre,fecha_nacimiento,nacionalidad,salario,score, num_auto, 0, False, esReserva)  


if __name__ == "__main__":
    programa = SimulacionDeCarrera()
    programa.menu_principal()
