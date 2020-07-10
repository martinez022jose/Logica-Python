#1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos
def max(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

print(max(2,3))

#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

print(max(-2,-3,-10))

#3- Definir una función que calcule la longitud de una lista o una cadena dada.

def longCadena(cadena):
    cont = 0
    for i in cadena:
        cont+=1
    return cont

print(longCadena("Hola Mundo"))

#4- Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def esVocal(caracter):
    listaDeCaracteres  = ['a','e','i','o','u']
    for i in listaDeCaracteres:
        if caracter == i or caracter.lower() == i:
            return True
        return False

print(esVocal("a"))

#5- Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.

def sumList(lista):
    totalSum = 0
    for i in lista:
        totalSum+=i
    return totalSum

def multList(lista):
    totalMult = 1
    for i in lista:
        totalMult*=i
    return totalMult

print(sumList([2,3,4]))
print(multList([2,3,6]))

#6- Definir una función inversa() que calcule la inversión de una cadena.

def inversa(cadena):
    cadenaInversa = ""
    longitudCadena = longCadena(cadena)
    for i in cadena:
        cadenaInversa+=cadena[longitudCadena-1]
        longitudCadena-=1
    return cadenaInversa

print(inversa("HolaATodos"))

#7- Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas)

def esPalindromo(palabra):
    setPalabra = palabra.lower()
    palabraInvertida = inversa(setPalabra)
    cont = 0
    esPal = True
    for i in setPalabra:
        if i == palabraInvertida[cont]:
            esPal = True
            cont+=1
        else:
            return False
    return esPal

print(esPalindromo("Ala"))

#8- Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

def superposicion(lista1,lista2):
    for i in lista1:
        for j in lista2:
            if i==j:
                return True
    return False

print(superposicion([2,3,4],[2,6,7]))

#9- Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(cantidad,caracter):
    return cantidad*caracter

print(generar_n_caracteres(5,'a'))

#10- Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.

def procedimiento(lista):
    for i in lista:
        cantidadTotal = i*'X'
        print(cantidadTotal)

procedimiento([2,3,7])

#11- Realizar funcion factorial(). Toma un numero y devuelve el factorial de dicho numero

def factorial(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial*numero
        numero-=1
    return factorial

print(factorial(0))

#12- Definir funcion ordanar(). Toma lista de numeros y ordena dicha lista

def ordenar(lista):
    longitudDeCadena = longCadena(lista)
    for i in range(1,longitudDeCadena):
        for j in range(0,longitudDeCadena - i):
            if lista[j] > lista[j+1]:
                k = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = k

def mostrarLista(lista):
    for i in lista:
        print(i)

listaPrueba = [4,2,1,67,-22]
ordenar(listaPrueba)
mostrarLista(listaPrueba)