#Problema 6
import operaciones

a = input("Ingrese el primer número: ")
b = input("Ingrese el segundo número: ")

resultado_suma = operaciones.suma(a, b)
print("Suma:", resultado_suma)

resultado_resta = operaciones.resta(a, b)
print("Resta:", resultado_resta)

resultado_producto = operaciones.producto(a, b)
print("Producto:", resultado_producto)

resultado_division = operaciones.division(a, b)
print("División:", resultado_division)