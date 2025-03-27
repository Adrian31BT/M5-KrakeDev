from auto import Auto

mi_auto = Auto("Toyota", "Corolla", 2018)

print("Información inicial del auto:")
mi_auto.mostrar_informacion()
print("\nIniciando el viaje con 5000 kilómetros:")
mi_auto.realizar_viaje(5000)
print("\nIniciando el viaje con 2000 kilómetros:")
mi_auto.realizar_viaje(2000)
print("\nInformación inicial del auto después de los dos viajes:")
mi_auto.mostrar_informacion()
print("\nEstado del auto después del viaje:")
mi_auto.estado_auto()
mi_auto.actualizar_kilometraje(25000)
print("\nInformación actualizada del auto:")
mi_auto.mostrar_informacion()
print("\nEstado del auto después de actualizar el kilometraje:")
mi_auto.estado_auto()
print("\nIntentando reducir el kilometraje:")
mi_auto.actualizar_kilometraje(20000)
print("\nIntentando realizar un viaje con kilómetros negativos:")
mi_auto.realizar_viaje(-1000)


