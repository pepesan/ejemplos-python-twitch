from xml.dom.minidom import ProcessingInstruction

if __name__ == '__main__':
    print("Ejemplos de variables")
    print("Booleanos")
    # Declaración e inicilización de variable
    # boolean: True, False, None
    booleana = True
    # imprimir por pantalla variable
    print(booleana)

    print("Números Enteros")
    # Declaración de variable entera
    # enteros: numero naturales, positivos o negativos
    entero = 2
    # imprimir por pantalla variable
    print(entero)
    # cambiamos el valor de una variable
    entero = 3
    # imprimir por pantalla variable
    print(entero)
    # Definimos otra variable entera
    numero = 2
    # imprimir por pantalla variable
    print(numero)

    print("Números flotantes")
    # Declaración de variables de coma flotante
    flotante = +1.23
    # imprimir por pantalla variable
    print(flotante)
    # valor negativo
    flotante = -1.23
    # imprimir por pantalla variable
    print(flotante)
    # casting de entero a flotante
    entero = 2
    flotante = float(entero)
    # imprimir por pantalla variable
    print(flotante)
    # casting de flotante a entero
    entero = int(flotante)
    print(entero)

    # Números complejos
    # Ref: https://es.wikipedia.org/wiki/N%C3%BAmero_complejo
    print("Números complejos")
    # definimos parte real y parte imaginaria
    # i = raiz cuadrada de -1
    # usado en cálculos matemáticos complejos
    # z = r + b*i
    complejo = complex(2, 1)
    print(complejo)


