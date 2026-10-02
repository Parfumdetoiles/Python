print("calcular la pendiente de interseccion x y de y de y=2x-2")
print("Ingrese el valor de x")
valorx = float(input())
valory = 2 * valorx - 2
print("El valor de y es: ", valory)
pendiente_uno = 2
print("La pendiente de la recta es: ", pendiente_uno)
print("calcular la pendiente con (m = (y2-y1)/(x2-x1) encuentre la pendiente de la recta que pasa por los puntos (2,2) y (6,10)")
x1 = 2
y1 = 2
x2 = 6
y2 = 10
pendiente_dos = (y2 - y1) / (x2 - x1)
print("La pendiente de la recta es: ", pendiente_dos)
print("calcular la distancia euclidiana entre los puntos (2,2) y (6,10)")
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("La distancia euclidiana entre los puntos es: ", distancia)
print("Pendiente 1:", pendiente_uno)
print("Pendiente 2:", pendiente_dos)