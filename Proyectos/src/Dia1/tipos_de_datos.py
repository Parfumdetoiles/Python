'''
Este comentario esta en varias lineas
'''

print(type("Soy un dato string")) # TIPO STR (cadena de texto)
print(type(67)) # TIPO INT (entero)
print(type(10.5)) # TIPO FLOAT (con decimal)
print(type(True)) # TIPO BOOL (booleano)
print(type(1 + 3j )) # TIPO COMPLEX (número complejo)

nombre = "Yahir"
apellido = "Oramas"
nombreCompleto = "Yahir Oramas"
Pais = "Mexico"
Ciudad = "Juarez"
Edad = 23
Anio= 2026
Casado = False
conChamba, estudiando = False, True
print(len(apellido)) # LONGITUD DE LA CADENA
nOne = 5
nTwo = 4
total = nOne + nTwo # SUMA  
diff = nTwo - nOne # RESTA
product = nOne * nTwo # MULTIPLICACION
division = nOne / nTwo # DIVISION
modulo = nOne % nTwo # MODULO (residuo de la division)
exp = nOne ** nTwo # EXPONENCIACION (nOne elevado a nTwo)
floorDivision = nOne // nTwo # DIVISION DE PISO (division que redondea hacia abajo al entero más cercano)

print("Calculando el area de un circulo")
radio = float(input("Ingresa el radio del circulo: "))
print("El radio del circulo es: ", radio)
pi = 3.1416
areaOfCircle = pi * (radio ** 2)
circumOfCircle = 2 * pi * radio
print("El area del circulo es: ", areaOfCircle)
print("La circunferencia del circulo es: ", circumOfCircle)

nombreTwo = input("Ingresa tu nombre: ")
ApellidoTwo = input("Ingresa tu apellido: ")
Pais = input("Ingresa tu pais: ")
Edad = int(input("Ingresa tu edad: "))

help("keywords") # Muestra todas las palabras reservadas de Python