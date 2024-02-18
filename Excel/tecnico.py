
def reemplazar_puntos(texto):
    texto_modificado = texto.replace('.', '!¡')
    return texto_modificado

# Ejemplo de uso:
texto_original = "Este es un ejemplo. Reemplazar puntos por signos de exclamación."
texto_modificado = reemplazar_puntos(texto_original)

print(f"Texto original: {texto_original}")
print(f"Texto modificado: {texto_modificado}")

def obtener_pares(lista_numeros):
    numeros_pares = [numero for numero in lista_numeros if numero % 2 == 0]
    return numeros_pares

# Ejemplo de uso:
numeros_originales = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = obtener_pares(numeros_originales)

print(f"Números originales: {numeros_originales}")
print(f"Números pares: {numeros_pares}")