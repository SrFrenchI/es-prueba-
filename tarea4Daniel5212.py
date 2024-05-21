class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
#daneilsisis 
    def validar_fecha(self):
        if len(str(self.año)) != 4 or self.año < 1900 or self.año > 2100:
            return False

        if self.mes < 1 or self.mes > 12:
            return False
        
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= self.dia <= 31
        elif self.mes in [4, 6, 9, 11]:
            return 1 <= self.dia <= 30
        elif self.mes == 2:
            if self.año % 4 == 0 and (self.año % 100 != 0 or self.año % 400 == 0):
                return 1 <= self.dia <= 29
            else:
                return 1 <= self.dia <= 28
        else:
            return False

daniel=True
while daniel:
        print("\n1. Crear una nueva fecha")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                dia = int(input("Ingrese el día: "))
                mes = int(input("Ingrese el mes: "))
                año = int(input("Ingrese el año: "))

                fecha = Fecha(dia, mes, año)
                if fecha.validar_fecha():
                    print("Fecha válida.")
                else:
                    print("Fecha inválida. Verifique los valores ingresados.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido para el día, mes y año.")
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
