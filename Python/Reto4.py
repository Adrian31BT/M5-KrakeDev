datos = []

cantidad = int(input("Cantidad de datos que desea ingresar: "))

for i in range(cantidad):
    dato = input(f"Ingrese el dato {i + 1}: ")

    if dato.isdigit():
        datos.append(int(dato))
    else:
        try:
            dato_float = float(dato)
            datos.append(dato_float)
        except ValueError:
            datos.append(dato)

print(f"Su lista es: {datos}")