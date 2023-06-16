#PROBLEMA 1
def calcular_porcentaje(fraccion):
    try:
        x, y = map(int, fraccion.split('/'))
        
        if x < 0 or y <= 0 or x < y:
            raise ValueError
        
        porcentaje = (x / y) * 100
        
        if porcentaje < 1:
            return 'E'
        elif porcentaje > 99:
            return 'F'
        else:
            return str(round(porcentaje)) + '%'
    
    except (ValueError, ZeroDivisionError):
        return "Error: Ingresa una fraccion valida."

def main():
    while True:
        fraccion = input("Ingresa una fraccion en el formato X/Y: ")
        resultado = calcular_porcentaje(fraccion)
        print("Cantidad de combustible en el tanque:", resultado)
        continuar = input("¿Deseas ingresar otra fracción? (s/n): ")
        if continuar.lower() != 's':
            break


if __name__ == '__main__':
    main()


#PROBLEMA 2
def obtener_calificaciones():
    while True:
        calificaciones_str = input("Introduce las calificaciones separadas por comas: ")
        try:
            calificaciones_list = calificaciones_str.split(',')
            calificaciones_int = [int(calificacion) for calificacion in calificaciones_list]
            return calificaciones_int
        except ValueError:
            print("Error: Los valores ingresados no son calificaciones validas. Intentalo de nuevo.")


calificaciones = obtener_calificaciones()
print("Calificaciones son:", calificaciones)

#PROBLEMA 3
def triangulo_pascal(n):
    if n <= 0:
        print("El numero de filas debe ser mayor que cero.")
        return

    # Inicializar la primera fila con 1
    fila_actual = [1]
    print(fila_actual)

    for _ in range(n - 1):
        # Generar la fila que sigue a partir de la anterior fila
        nueva_fila = [1]

        for i in range(1, len(fila_actual)):
            nuevo_valor = fila_actual[i - 1] + fila_actual[i]
            nueva_fila.append(nuevo_valor)

        nueva_fila.append(1)
        print(nueva_fila)

        fila_actual = nueva_fila


n = int(input("Introduce el número de filas del triángulo de Pascal que deseas imprimir: "))
triangulo_pascal(n)



#PROBLEMA 4
def longitud_ultima_palabra(string):
    # Eliminar los espacios en blanco al principio y al final del string
    string = string.strip()

    # Dividir el string en palabras separadas por espacios en blanco
    palabras = string.split()

    # Para verificar si hay palabras en el string
    if len(palabras) == 0:
        return 0

    # Para obtener la última palabra y retornar su longitud
    ultima_palabra = palabras[-1]
    return len(ultima_palabra)


string = input("Introduce un string: ")
longitud = longitud_ultima_palabra(string)
print("La longitud de la última palabra es:", longitud)

#PROBLEMA 5
import script_main

# Generar números aleatorios
numeros_aleatorios = script_main.generar_numeros_aleatorios()

# Para mostrar la lista obtenida por pantalla
print("Lista generada:")
script_main.mostrar_lista(numeros_aleatorios)

# Ordenación los valores de la lista
numeros_ordenados = script_main.ordenar_lista(numeros_aleatorios)

# Para mostrar la lista ordenada por pantalla
print("Lista ordenada:")
script_main.mostrar_lista(numeros_ordenados)




