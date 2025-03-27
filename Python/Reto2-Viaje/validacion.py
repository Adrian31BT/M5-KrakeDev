from accion import operacion
def validar_velocidad(codigo_pais, codigo_zona, velocidad):
    limites_velocidad = {
        1: {
            1: (10, 50),
            2: (51, 70),
            3: (71, 90)
        },
        2: {
            1: (10, 30),
            2: (31, 80),
            3: (81, 100)
        },
        3: {
            1: (10, 40),
            2: (41, 60),
            3: (61, 120)
        }
    }

    min_vel, max_vel = limites_velocidad[codigo_pais][codigo_zona]

    if velocidad < min_vel:
        return f"La velocidad está por debajo del límite mínimo de {max_vel} km/h"
    elif velocidad > max_vel:
        return f"La velocidad supera el límite máximo de {max_vel} km/h"
    else:
        return "La velocidad está dentro de los límites legales."