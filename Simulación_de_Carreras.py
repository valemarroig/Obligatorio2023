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