import datetime

nombre_paciente = []
edad_paciente = []
def agregar_nombre(nombre, apellido):
    nombre_paciente.append(f"{nombre} {apellido}")

def agregar_edad(anio_nacimiento):
    anio_actual = datetime.datetime.now().year
    edad = anio_actual- anio_nacimiento
    edad_paciente.append(edad)