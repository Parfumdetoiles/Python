#Ley de Gravitación Universal de Newton:
#Calcula la fuerza de atracción entre dos cuerpos.
print("Calcula la fuerza de atracción entre dos cuerpos:")
constante_gravitacion_universal = 6.674*10**-11
print("Ingresa la masa del cuerpo 1 (kg)")
masa_uno = float(input())
print("Ingresa la masa del cuerpo 2 (kg)")
masa_dos = float(input())
print("Ingresa la distancia (r): (en metros)")
distancia = float(input())

fuerza = (constante_gravitacion_universal*(masa_uno*masa_dos/(distancia**2)))
print("La fuerza de atraccion entre dos cuerpos es: ", fuerza, "")

