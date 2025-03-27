print("Caluladora de Rectangulo")
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

area = round(base * altura, 2)
perimetro = round(2 * (base + altura), 2)
superficie = round(base * altura, 2) 

print(f"El area del rectangulo es: {area}")
print(f"El perimetro del rectangulo es: {perimetro}")

