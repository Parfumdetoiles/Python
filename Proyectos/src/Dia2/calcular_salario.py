#Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. ¿Calcular el salario de la persona?
print("Ingresa horas trabajadas en la semana: \n-6 dias = 48 horas \n-5 dias = 40 horas \n-4 dias = 32 horas")
horas = int(input())
print("Ingresa la tarifa por hora:")
tarifa = float(input())
salario = horas*tarifa
print(salario)
