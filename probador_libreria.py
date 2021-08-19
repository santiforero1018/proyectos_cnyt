""" Probador de libreria de operaciones con numeros complejos imaginarios

"""

import Libreria_numeros_complejos as nc


def conv_float(lista):
    """ convierte los elementos de una lista de numeros en tipo entero

    :param lista: una lista de numeros en tipo str
    :type lista: list
    :return: lista con numeros enteros
    :rtype: list
    """
    for i in range(len(lista)):
        lista[i] = float(lista[i])

    return lista


def main():
    """ Funcion principal

    :return: None
    """
    print("Hola usuario, este es un programa que realiza operaciones con numeros complejos usando una libreria"
          "de operaciones basicas con numeros complejos, por favor, seguir las instrucciones para el buen"
          "funcionamiento del programa \n")
    print("se puede representar un numero complejo de la forma a+b*i de manera cartesiana como [a,b], donde a es "
          "la parte real y b un numero real completando la parte imaginaria del numero complejo.\n")
    par_complejo1 = input("ingrese un numero complejo,de la forma a,b: ").split(",")
    par_complejo2 = input("ingrese un numero complejo, de la forma a,b: ").split(",")
    par_complejo1 = conv_float(par_complejo1)
    par_complejo2 = conv_float(par_complejo2)
    print(par_complejo1, par_complejo2)
    print()
    print("elija la operacion que desee realizar con numeros complejos\n")
    operador = "0"
    while operador != "A":
        operador = input("Digite +,-,*,/ para realizar una operacion basica con numeros complejos, Digite A"
                         "para finalizar las operaciones: ")
        if operador == "+":
            resultado = nc.suma_complejos(par_complejo1, par_complejo2)
            print("El resultado de la suma de los numeros complejos es: ", resultado, "\n")
        elif operador == "-":
            resultado = nc.resta_complejos(par_complejo1, par_complejo2)
            print("El resultado de la resta de los numeros complejos es: ", resultado, "\n")
        elif operador == "*":
            resultado = nc.multiplicacion_complejos(par_complejo1, par_complejo2)
            print("El resultado de la multiplicación de los numeros complejos es: ", resultado, "\n")
        elif operador == "/":
            resultado = nc.division_complejos(par_complejo1, par_complejo2)
            resultado[0], resultado[1] = round(resultado[0], 2), round(resultado[1], 2)
            print("El resultado de la división de los numeros complejos es: ", resultado, "\n")
        else:
            break
    desision = input("ingrese 1, 2 o r para saber el modulo de el numero complejo 1, 2 o el resultante de la operacion"
                     "anterior")
    if desision == "1":
        modulo_result = nc.modulo_complejos(par_complejo1)
        modulo_result = round(modulo_result, 2)
        print("el modulo del numero complejo (1) es: ", modulo_result)
    elif desision == "2":
        modulo_result = nc.modulo_complejos(par_complejo2)
        modulo_result = round(modulo_result, 2)
        print("el modulo del numero complejo (2) es: ", modulo_result)
    else:
        modulo_result = nc.modulo_complejos(resultado)
        modulo_result = round(modulo_result, 2)
        print("el modulo del numero complejo resultado es: ", modulo_result)
    decision = input("ingrese 1, 2 o r para saber el conjugado de numero complejo 1, 2 o el resultante de la operacion"
                     "anterior")
    if decision == "1":
        conjugado = nc.conjugado_complejos(par_complejo1)
        print("El conjugado del numero complejo (1) es: ", conjugado)
    elif decision == "2":
        conjugado = nc.conjugado_complejos(par_complejo2)
        print("El conjugado del numero complejo (2) es: ", conjugado)
    else:
        conjugado = nc.conjugado_complejos(resultado)
        print("EL conjugado del numero complejo resultado es: ", conjugado)
        print("El conjugado del numero complejo (2) es: ", conjugado)
    print()
    print("OPERACIONES CON NUMEROS COMPLEJOS EN REPRESENTACION POLAR\n")
    print("La representacion polar de los numeros complejos ingresados son: ")
    par_complejo1p = nc.rep_polar(par_complejo1)
    par_complejo2p = nc.rep_polar(par_complejo2)
    par_complejo1p[0], par_complejo1p[1] = round(par_complejo1p[0], 2), round(par_complejo1p[1], 2)
    par_complejo2p[0], par_complejo2p[1] = round(par_complejo2p[0], 2), round(par_complejo2p[1], 2)
    print(par_complejo1p, "y", par_complejo2p)
    producto_polar = nc.multiplicacion_polar(par_complejo1p, par_complejo2p)
    producto_polar[0], producto_polar[1] = round(producto_polar[0], 2), round(producto_polar[1], 2)
    print("la multiplicacion entre los dos numeros complejos en representacion polar es: ", producto_polar)
    division_po = nc.division_polar(par_complejo1p, par_complejo2p)
    division_po[0], division_po[1] = round(division_po[0], 2), round(division_po[1], 2)
    print("la division entre dos numeros complejos en representacion polar es: ", division_po)
    print()
    exponente = int(input("Para realizar la potencia de un numero complejo en representacion polar, digite el "
                          "exponente: "))
    numero_c = int(input("digite 1 o 2, para sacar la potencia del numero complejo correspondiente"))
    if numero_c == 1:
        potencia = nc.potencia_polar(par_complejo1p, exponente)
        potencia[0], potencia[1] = round(potencia[0], 2), round(potencia[1], 2)
        print("la potencia del numero complejo en representacion polar es: ", potencia)
    else:
        potencia = nc.potencia_polar(par_complejo2p, exponente)
        print("La potencia del numero complejo en representacion polar es: ", potencia)
    potencia_cart = nc.rep_cartesiana(potencia)
    potencia_cart[0], potencia_cart[1] = round(potencia_cart[0], 2), round(potencia_cart[1], 2)
    print("Y la representacion cartesiana de la potencia es: ", potencia_cart)
    print()
    opcion = input("¿Desea ejecutar el programa otra vez?, digite y o n")
    if opcion == "y":
        main()
    else:
        print("hasta aqui la prueba de la libreria.")


main()
