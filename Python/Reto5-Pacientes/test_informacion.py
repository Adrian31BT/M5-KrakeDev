from informacion import agregar_nombre, agregar_edad, nombre_paciente, edad_paciente    

while True:
    nombre = input("Ingrese el nombre del paciente: ")
    apellido = input("Ingrese el apellido del paciente: ")
    anio_nacimiento = int(input("Ingrese el año de nacimiento del paciente: "))

    agregar_nombre(nombre, apellido)
    agregar_edad(anio_nacimiento)

    respuesta = input("¿Desea añadir otro paciente? (s/n): ")
    if respuesta.lower() == "n":
        break

print("Nombre de los pacientes: ", nombre_paciente)
print("Edad de los pacientes: ", edad_paciente)

edad_mayor = max(edad_paciente)
indice = edad_paciente.index(edad_mayor)
nombre_mayor = nombre_paciente[indice]

print(f"{nombre_mayor} con la edad de {edad_mayor} años es mayor a los demás pacientes.")



