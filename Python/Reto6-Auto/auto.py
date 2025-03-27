import datetime

class Auto:
    def __init__(self, marca, modelo, año, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Kilometraje: {self.kilometraje}")

    def actualizar_kilometraje(self, kilometraje):
        if kilometraje >= self.kilometraje:
            self.kilometraje = kilometraje
            print("Kilometraje actualizado correctamente.")
        else:
            print("No se puede reducir el kilometraje.")
    
    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
            print(f"Viaje de {kilometros} km realizado. Kilometraje actual: {self.kilometraje}")
        else:
            print("La cantidad de kilómetros debe ser positiva.")

    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya déjame descansar por favor!")

    @classmethod
    def crear_toyota_actual(cls, modelo):
        año_actual = datetime.datetime.now().year
        return cls("Toyota", modelo, año_actual)

    @staticmethod
    def comparar_kilometraje(auto1, auto2):
        return auto1.kilometraje == auto2.kilometraje

    @staticmethod
    def es_año_valido(año):
        año_actual = datetime.datetime.now().year
        return 1900 <= año <= año_actual

    @classmethod
    def calcular_antiguedad_promedio(cls, lista_autos):
        if not lista_autos:
            return 0
        año_actual = datetime.datetime.now().year
        total_antiguedad = sum(año_actual - auto.año for auto in lista_autos)
        return total_antiguedad / len(lista_autos)