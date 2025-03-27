from menu import menu_restaurante

def operacion(opcion):
    if opcion == 1:
        while True:
            plato = input("Ingrese el nombre del plato a añadir: ")
            menu_restaurante.append(plato)
            respuesta = input("¿Desea añadir otro plato al menú? (s/n): ")
            if respuesta.lower() == "n":
                break
        return "Se han añadido nuevos platos al menú."
    elif opcion == 2:
        plato = input("Ingrese el nombre del plato a buscar: ")
        if buscar_plato(plato):
            return f"'{plato}' se encuentra en el menú."
        else:
            return f"'{plato}' no se encuentra en el menú."
    elif opcion == 3:
        plato = input("Ingrese el nombre del plato a eliminar: ")
        if buscar_plato(plato):
            for item in menu_restaurante:
                if item.lower() == plato.lower():
                    menu_restaurante.remove(item)
                    break
            return f"'{plato}' ha sido eliminado del menú."
        else:
            return f"'{plato}' no se encuentra en el menú."
    elif opcion == 4:
        return menu_restaurante

def buscar_plato(plato):
    for item in menu_restaurante:
        if item.lower() == plato.lower():
            return True
    return False