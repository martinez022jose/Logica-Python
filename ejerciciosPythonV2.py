"""
Se necesita realizar:
A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.

"""
def eliminarElemento(lista,elemento):
    if elemento in lista:
        lista.remove(elemento)
            
def sumatoria(lista):
    sumTotal = 0
    for i in lista:
        sumTotal+=i
    return sumTotal

def generarListaFiltrada(numero,lista):
    listaNueva = []
    for i in lista:
        if i < numero:
            listaNueva.append(i)
    return listaNueva
    

def generarLista(numeros):
    numero = int(input("Ingrese numeros, se determina como terminado cuando ingrese cero "))
    while numero != 0:
        numeros.append(numero)
        numero = int(input("Ingrese numeros, se determina como terminado cuando ingrese cero "))


def imprimirLista(lista):
    for i in lista:
        print(i)
"""

#Main::

#A
numeros = []
generarLista(numeros)
imprimirLista(numeros)

#B

elementoAEliminar = int(input("Ingrese elemento: "))
eliminarElemento(elementoAEliminar,numeros)
imprimirLista(numeros)

#C

sumaTotal = sumatoria(numeros)
print(sumaTotal)

#D

limite = int(input("Ingrese limite de lista: "))
numerosNuevos = generarListaFiltrada(limite,numeros)
imprimirLista(numerosNuevos)
"""

#---------------------------------------------------------------------------------------------------------------------------------------

"""
#Crear un programa en el cual es usuario deba adivinar un numero "x" con una cantidad n de intentos a definir. Se debe informar cual fue el motivo por las cuales perdio. Si gano se debe informar cantidad de veces realizadas y un msj correspondiente
 """

import random

def compararNumero(numero,valorRandom):
    return numero == valorRandom

def imprimirMensaje(limiteDeIntentos,cantidadDeIntentos,valorRandom):
    if limiteDeIntentos > 0:
        print("Adivino el numero, con la cantidad de intento: "+str(cantidadDeIntentos))
    else:
        print("Se llego al limite de intentos posibles, el numero era: "+str(valorRandom))

def darPista(numero,valorRandom):
    if(numero > valorRandom):
        print("El valor es mayor al buscado")
    else:
        print("El valor es menor al buscado")

"""
#Main::

limiteInferior = 0
limiteSuperior = 30       
valorRandom = random.randint(limiteInferior,limiteSuperior)
limiteDeIntentos = 6
cantidadDeIntentos = 1
print(valorRandom)

while limiteDeIntentos > 0:
    numero = int(input("Ingrese numero: "))
    if compararNumero(numero,valorRandom):
        break
    else:
        darPista(numero,valorRandom)
    cantidadDeIntentos+=1
    
    limiteDeIntentos-=1

imprimirMensaje(limiteDeIntentos,cantidadDeIntentos,valorRandom)

"""
#---------------------------------------------------------------------------------------------------------------------------------------

"""
#Crear un programa en el cual es usuario deba adivinar una palabra seteada de antemano con una cantidad n de intentos a definir. Se debe informar cual fue el motivo por las cuales perdio. Si gano se debe informar cantidad de veces realizadas y un msj correspondiente.
Se debe ir formando por pantalla la palabra a medida que vaya ingresando las letras
"""

"""
#Main::

def mostrarCadenaCifrada(letra,cadena,cadenaCifrada):
        for caracter in cadena:
            if caracter in cadenaCifrada:
                print(caracter)
            else:
                print("*")
        print("Elementos ingresados hasta el momento:")
        print(cadenaCifrada)
        print("\n")


def imprimirMensaje(cantidadDeIntentos,limiteDeIntentos,cadena):
    mensaje = ""
    if limiteDeIntentos == 0:
        mensaje = "Se quedo sin intentos posibles, la palabra cifrada era: "+cadena
        print(mensaje)
    else:
        mensaje = "Lograste decifrar la cadena: '"+cadena+"' con la cantidad de intentos: "+ str(cantidadDeIntentos)
        print(mensaje)

def modificarCadena(letra,posicion,cadenaMuestra):
    cadenaMuestra[posicion] = letra
    
def compararCaracter(caracter,cadena):
    if caracter in cadena:
        return True
    return False

def longitudCadena(cadena):
    long = 0
    for i in cadena:
        long+=1
    return long

def contieneTodosLosCaracteres(cadenaCifrada,cadena):
    estado = False
    for caracter in cadena:
        if caracter in cadenaCifrada:
            estado = True
        else: 
            estado = False
            break
    return estado == True

limiteDeIntentos = 6
cantidadDeIntentos = 1


cadena = input("Ingrese palabra a decifrar: ")
cadenaCifrada = []

while limiteDeIntentos > 0:
    letra = input("Ingrese letra: ")
    cadenaCifrada.append(letra)
    if contieneTodosLosCaracteres(cadenaCifrada,cadena):
        break
    else:
        mostrarCadenaCifrada(letra,cadena,cadenaCifrada)
    cantidadDeIntentos+=1
    limiteDeIntentos-=1

imprimirMensaje(cantidadDeIntentos,limiteDeIntentos,cadena)

"""

    
