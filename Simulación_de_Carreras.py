from datetime import datetime
from Entities.Piloto import Piloto
from Entities.Mecanico import Mecanico
from Entities.DirectorEquipo import DirectorEquipo
from Entities.Empleado import Empleado
from Entities.Auto import Auto
from Entities.Equipo import Equipo
from Exceptions.InformaciónInválida import InformacionInvalida
import re

class SimulacionDeCarrera:
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
        print("\n--- Alta de Auto ---")    
        modelo = input("Ingrese modelo: ")
        ano = int(input("Ingrese año: "))
        score = int(input("Ingrese score: "))
        if (modelo == "" or (score < 0) or ano <= 0):
            raise ValueError("Error en datos ingresados para el auto")
        auto = Auto(modelo,ano, score)
        self.autos.append(auto)
        print(f"Auto {modelo}, {ano} dado de alta con éxito.")

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

        # Agregar el equipo a la lista de equipos
        nuevo_equipo = Equipo(nombre_equipo, [auto], pilotos_equipo, [piloto_reserva], mecanicos_equipo, director_equipo)
        self.lista_equipos.append(nuevo_equipo)

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
        
            

        
        
        
        
        

    def validar_fecha(self, date_string):
        try:
            # Parse the input string as a date
            date_object = datetime.strptime(date_string, '%d/%m/%Y')
            return True
        except ValueError:
            return False
    
    def validar_id(self, id):
        if len(id) == 8:
            return id.isdigit()
        else:
            return False  # Si la longitud no es 8
        
    def validar_texto(self, texto):
    # Patrón regex para validar que el nombre contiene solo letras y espacios
        patron = re.compile(r'^[a-zA-Z\s]+$')
        # Verificar si el nombre coincide con el patrón
        if patron.match(texto):
            return True
        else:
            return False
        
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

                cedula = input("Ingrese cédula: ")
                if not self.validar_id(cedula):  #falta validar que no se repita
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
        score = int(input("Ingrese la habilidad del piloto (del 1-99): "))
        while score > 99 or score < 1:
            print("Score no válido. Intente de nuevo.")
            score = input("Ingrese la habilidad del piloto (del 1-99): ") 
        return Mecanico(cedula,nombre, fecha_nacimiento,nacionalidad, salario, score)

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