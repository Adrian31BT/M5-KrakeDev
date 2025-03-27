import datetime
from auto import Auto

auto_nuevo = Auto.crear_toyota_actual("Corolla")
print("Test crear_toyota_actual:")
print(f"Marca: {auto_nuevo.marca == 'Toyota'}")
print(f"Modelo: {auto_nuevo.modelo == 'Corolla'}")
print(f"Año: {auto_nuevo.año == datetime.datetime.now().year}")
print(f"Kilometraje: {auto_nuevo.kilometraje == 0}")

auto1 = Auto("Toyota", "Corolla", 2020, 50000)
auto2 = Auto("Honda", "Civic", 2019, 50000)
auto3 = Auto("Nissan", "Sentra", 2021, 30000)
print("\nTest comparar_kilometraje:")
print(f"Mismo kilometraje (auto1 y auto2): {Auto.comparar_kilometraje(auto1, auto2)}")
print(f"Distinto kilometraje (auto1 y auto3): {not Auto.comparar_kilometraje(auto1, auto3)}")

año_actual = datetime.datetime.now().year
print("\nTest es_año_valido:")
print(f"Año válido (2000): {Auto.es_año_valido(2000)}")
print(f"Año válido (año actual): {Auto.es_año_valido(año_actual)}")
print(f"Año inválido (1800): {not Auto.es_año_valido(1800)}")
print(f"Año inválido (año futuro): {not Auto.es_año_valido(año_actual + 1)}")

auto1 = Auto("Toyota", "Corolla", 2020)
auto2 = Auto("Honda", "Civic", 2019)
auto3 = Auto("Nissan", "Sentra", 2021)
lista_autos = [auto1, auto2, auto3]
antiguedad_promedio = Auto.calcular_antiguedad_promedio(lista_autos)
año_actual = datetime.datetime.now().year
antiguedad_esperada = ((año_actual - 2020) + (año_actual - 2019) + (año_actual - 2021)) / 3
print("\nTest calcular_antiguedad_promedio:")
print(f"Antigüedad promedio: {antiguedad_promedio == antiguedad_esperada}")
print(f"Lista vacía: {Auto.calcular_antiguedad_promedio([]) == 0}")