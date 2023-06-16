def suma(a, b):
    try:
        resultado = float(a) + float(b)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def resta(a, b):
    try:
        resultado = float(a) - float(b)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def producto(a, b):
    try:
        resultado = float(a) * float(b)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def division(a, b):
    try:
        if float(b) == 0:
            return "Error: No es posible dividir entre cero"
        resultado = float(a) / float(b)
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"
