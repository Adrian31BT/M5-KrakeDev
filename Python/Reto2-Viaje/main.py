from validacion import validar_velocidad
def main():
    print("Bienvenido a Kraketravels")
    pais = {
        1: "Ecuador",
        2: "Colombia",
        3: "Peru"
    }
    zona = { 
        1: "urbana",
        2: "rural",
        3: "perimetral"
    }   

    while True:
        print("Seleccione un país:")
        for key, value in pais.items():
            print(f"{key}: {value}")
        try:
            codigo_pais = int(input("Ingrese el código del país: "))
            if codigo_pais in pais:
                break 
            else:
                print("Código de país inválido. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

    while True:
        print("Seleccione una zona:")
        for key, value in zona.items():
            print(f"{key}: {value}")
        try:
            codigo_zona = int(input("Ingrese el código de la zona: "))
            if codigo_zona in zona:
                break  
            else:
                print("Código de zona inválido. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

    print("Viaja a", pais[codigo_pais], "en zona", zona[codigo_zona])
    velocidad = float(input("Ingrese velocidad del automovil en km/h: "))

    mensaje = validar_velocidad(codigo_pais, codigo_zona, velocidad)
    print(mensaje)

if __name__ == "__main__":
    main()