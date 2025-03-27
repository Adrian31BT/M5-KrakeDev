from accion import operacion
def main():
    while True:
        menu_opciones = {
            1 : "Añadir plato al menú",
            2 : "Buscar en el menú",
            3 : "Eliminar plato del menú",
            4 : "Mostrar platos del menú",
            5 : "Salir"
        }
        for key, value in menu_opciones.items():
            print(f"{key}: {value}")

        while True:
            try:
                opcion = int(input("Seleccione una opcion: "))
                if opcion in menu_opciones:
                    break
                else:
                    print("Opcion inválida. Intente de nuevo.")
            except ValueError:
                print("Entrada inválida.")
        
        mensaje = operacion(opcion)
        if isinstance(mensaje, list):
            print("\n--- Menú del Restaurante ---")
            for i, plato in enumerate(mensaje):
                print(f"{i+1}. {plato}")
            print("-----------------------------")
        else:
            print(mensaje)

        if opcion == 5:
            break

if __name__ == "__main__":
    main()