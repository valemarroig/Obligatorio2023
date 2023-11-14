from datetime import datetime
from Entities.Piloto import Piloto
from Entities.Mecanico import Mecanico
from Entities.DirectorEquipo import DirectorEquipo
from Entities.Empleado import Empleado
from Entities.Auto import Auto

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

    def alta_auto(self):
        print("\n--- Alta de Auto ---")    
        modelo = input("Ingrese modelo: ")
        ano = int(input("Ingrese año: "))
        score = int(input("Ingrese score: "))
        if (modelo == "" or (score < 0) or ano <= 0):
            raise ValueError("Error en datos ingresados para el auto")
        auto = Auto(modelo,ano, score)
        self.autos.append(auto)

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
        # Falta tomar todos los datos elegidos y hacer append a la lista de equipos con un nuevo equipo generado (en base a los parametros)
        
            

        
        
        
        
        


    
    def validar_id(self, id):
        if len(id) == 8:
            return id.isdigit()
        else:
            return False  # Si la longitud no es 8

    def alta_empleado(self):
        print("\n--- Alta de Empleado ---")

        cedulaOk = False
        cedula = input("Ingrese cédula: ")

        if not self.validar_id(cedula):
            while not cedulaOk:
                cedula = input("Ingrese cédula: ")
                cedulaOk = self.validar_id(cedula)

        # Inputs sin validacion
        nombre = input("Ingrese nombre: ")
        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
        nacionalidad = input("Ingrese nacionalidad: ")
        salario = float(input("Ingrese salario: "))

        if nacionalidad == "" or not self.validate_date(fecha_nacimiento):
            raise ValueError("Valores incorrectos!")
        
        # Validar el cargo
        cargos_validos = ["1", "2", "3", "4"]
        print("Cargos disponibles:")
        print("1. Piloto")
        print("2. Piloto de reserva")
        print("3. Mecánico")
        print("4. Director de equipo")

        cargo = input("Ingrese el número del cargo: ")
        while cargo not in cargos_validos:
            print("Cargo no válido. Intente de nuevo.")
            cargo = input("Ingrese el número del cargo: ")       
        if cargo == 1:
            pilotoCreado = self.crearPiloto(cedula, nombre, fecha_nacimiento, nacionalidad, salario,  False)
            self.pilotos.append(pilotoCreado)
        elif cargo == 2:
            pilotoReservaCreado = self.crearPiloto(cedula, nombre, fecha_nacimiento, nacionalidad, salario, True)
            self.pilotosReserva.append(pilotoReservaCreado)
        elif cargo == 3:
            mecanicoCreado = self.crearMecanico(cedula, nombre, fecha_nacimiento, nacionalidad, salario)
            self.mecanicos.append(mecanicoCreado)
        else:
            directorCreado = self.crearDirector(cedula, nombre, fecha_nacimiento, nacionalidad, salario)
            self.directores.append(directorCreado) 

        print(f"Empleado {nombre} dado de alta con éxito.")

    def crearDirector(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario):
        return DirectorEquipo(cedula,nombre,fecha_nacimiento,nacionalidad,salario)

    def validate_date(self, date_string):
        try:
            # Parse the input string as a date
            date_object = datetime.strptime(date_string, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def crearMecanico(self,cedula, nombre, fecha_nacimiento, nacionalidad, salario):
        score = int(input("Ingrese la habilidad del piloto (del 1-99): "))
        while score > 99 or score < 1:
            print("Score no válido. Intente de nuevo.")
            score = input("Ingrese la habilidad del piloto (del 1-99): ") 
        return Mecanico(cedula,nombre, fecha_nacimiento,nacionalidad, salario, score)
        

    def crearPiloto(self, cedula, nombre, fecha_nacimiento, nacionalidad, salario, esReserva):
        num_auto = input("Ingrese numero de auto: ")
        fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")  
        nacionalidad = input("Ingrese nacionalidad: ")

        estaLesionadoInput = input("Ingrese si esta lesionado, S= si, otra cosa= no: ")
        estaLesionadoBool = False
        
        if num_auto == "":
            raise ValueError("Falta numero auto")

        if estaLesionadoInput == "S":
            estaLesionadoBool = True

        score = input("Ingrese la habilidad del piloto (del 1-99): ")
        while score > 99 or score < 1:
            print("Score no válido. Intente de nuevo.")
            score = input("Ingrese la habilidad del piloto (del 1-99): ")  
        
        num_auto = input("Ingrese el numero de auto: ")
        while not num_auto.isnumeric():
            print("El numero del auto no es numerico.")
            score = input("Ingrese el numero de auto: ")  

        return Piloto(cedula,nombre,fecha_nacimiento,nacionalidad,salario,score, num_auto, 0,estaLesionadoBool, esReserva)  


if __name__ == "__main__":
    programa = SimulacionDeCarrera()
    programa.menu_principal()