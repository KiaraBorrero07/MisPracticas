#PROBLEMA 5
import random

def generar_numeros_aleatorios():
    numeros = [random.randint(0, 100) for _ in range(20)]
    return numeros

def mostrar_lista(lista):
    for numero in lista:
        print(numero, end=' ')
    print()

def ordenar_lista(lista):
    lista.sort()
    return lista