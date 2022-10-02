import math # Importar librerias 
import time
import math as ma

def linea():
    print("-" * 25)
linea()

x = float(input("Escriba un número: ")) # Preguntar por los números
n = float(input("Escriba otro número: "))


linea()
print("\n\n")
while True: # Bucle while para ejecutar la calculadora
    
    linea()
    
    time.sleep(1.25)

    print("Elija una opción:") # Que operaciones hay para hacer
    print("1 para cambiar números")
    print("+ para sumar")

    time.sleep(.5)
    print("- para restar")
    print("* para multiplicar")

    time.sleep(.5)
    print("/ para dividir")
    print("% para resto división")

    time.sleep(.5)
    print("** para Xⁿ")
    print("rz para la raíz de X con índice N")

    time.sleep(.5)
    print("log para logaritmo de X en base N")
    print("pc para el X" + "%" + " de N")
    print("'X' para cerrar")

    linea()

    operadores = input("¿Tu opción? ") # Preguntar sobre la operación elegida
    print("\n\n")
    
    if operadores == "1": # Cambiar números
        x = float(input("Introduce tu primer número: ") )
        n = float(input("Introduce tu segundo número: ") )
    
    elif operadores == "+": # Sumar
        print (x+n)
        time.sleep(.25)
    
    elif operadores == "-": # Restar 
        print(x-n)
        time.sleep(.25)
    
    elif operadores == "*": # Multiplicar
        print(x*n)
        time.sleep(.25)
    
    elif operadores == "/": # División
        if n == 0: # Si el divisor es 0 el resultado es inderteminado
            print("No se puede dividir por 0")
            time.sleep(.25)
        else: # Si el divisor no es 0, hacer la división
            print(x/n)
            time.sleep(.25)        
    elif operadores == "%": # Módulo, calcula el resto de la división
        if n == 0: # Si el divisor es 0 el resultado es inderteminado
            print("No se puede dividir por 0")
            time.sleep(.25)
        else: # Si el divisor no es 0, hacer la división
            print(x%n)
            time.sleep(.25)
    
    elif operadores == "**": # X elevado a N
        print(x**n)
        time.sleep(.25)
    
    elif operadores == "rz": # Raíces de cualquier índice
        if x == -1 and n == 2: # Raíz cuadrada de menos uno
            print("La raíz cuadrada de -1 es '𝓲' la unidad imaginaria")
            time.sleep(.25)

        elif x < 0 and n == 2: # Raíz cuadrada de cualquier número negativo
            print(str(math.sqrt(abs(x))) + " * 𝓲")
            time.sleep(.25)

        elif x < 0 and n > 2: # Raíces negativas de índice superior a 2
            print("No existe")

        else: # Raíz normal
            print(x**(1/n))
            time.sleep(.25)
    
    elif operadores == "log": # Logaritmos
        if x <= 0 or n <= 0:
            print("Ni el argumento ni la base no puede ser negativo o 0\n")
            x = float(input("Por favor selecione otros números: ") )
            n = float(input("Por favor selecione otros números: ") )
            print("\n\n")
            time.sleep(.25)

        elif n == 1:
           print("1")

        else:
            lg = ma.log(x,n) # X es la base, N el argumento
            print(lg) #n^y=x
            time.sleep(.25)   
    
    elif operadores == "pc": # X% de N
        print((x*n)/100)
        time.sleep(.25)
    
    elif operadores == "X" or operadores == "x": # Cerrar la calculadora
        break

    else: # Si nada de lo de arriba es verdad, entonces el opereador esta mal
        print("Operador incorrecto")
        
# Tlt
