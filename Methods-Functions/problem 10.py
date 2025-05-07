# ITERATIVE WAY
def myfunc(x):
    # Crea una cadena de caracteres vacía llamada 'out' para almacenar el resultado.
    out = ''
    
    # Itera a través de los caracteres de la cadena 'x' junto con sus índices usando 'enumerate'.
    for index, letter in enumerate(x):
        
        # Si el índice es par (comienza en 0), convierte la letra a mayúsculas y la agrega a 'out'.
        if index % 2 == 0:
            out += letter.upper()
        else:
            # Si el índice es impar, convierte la letra a minúsculas y la agrega a 'out'.
            out += letter.lower()
    
    # Devuelve la cadena 'out' como resultado.
    return out
print(myfunc("Hello World"))


# RECURSIVE WAY
def myfunc_recursive(x, index=0):
    # Caso base: si hemos llegado al final de la cadena 'x', retornamos una cadena vacía.
    if index >= len(x):
        return ""

    # Convierte la letra en la posición 'index' a mayúscula o minúscula según el índice sea par o impar.
    if index % 2 == 0:
        letter = x[index].upper()
    else:
        letter = x[index].lower()

    # Llama recursivamente a la función para procesar el resto de la cadena y concatena el resultado.
    return letter + myfunc_recursive(x, index + 1)

# Ejemplo de uso:
result = myfunc_recursive("Hola Mundo")
print(result)
