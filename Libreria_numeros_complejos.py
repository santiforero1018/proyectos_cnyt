"""Libreria de operaciones basicas con numeros complejos

"""

import math


def suma_matricesc(matrizc1, matrizc2):
    """suma de dos matricves complejas

    :param matrizc1: matriz de numeros complejos
    :type matrizc1: list
    :param matrizc2: matriz de numeros complejos
    :type matrizc2: matriz de numeros complejos
    :return: suma de las matrices
    :rtype: list
    """
    if len(matrizc1) == len(matrizc2) and len(matrizc1[0]) == len(matrizc2[0]):
        line = [(0, 0)] * len(matrizc1[0])
        matriz_r = [line] * len(matrizc1)
        for j in range(len(matrizc1)):
            for k in range(len(matrizc1[0])):
                matriz_r[j][k] = suma_complejos(matrizc1[j][k], matrizc2[j][k])

    return matriz_r


def multi_escalar(complex_num, complex_v):
    """ multiplicacion por un escalar

    :param complex_num: un numero complejo
    :typecomplex_num: tuple
    :param complex_v: vector complejo
    :type complex_v: list
    :return: vector resultante
    :rtype list
    """
    r_vector = [(0, 0)] * len(complex_v)
    for x in range(len(complex_v)):
        r_vector[x] = multiplicacion_complejos(complex_num, complex_v[x])

    return r_vector


def inverse_vectorcx(vectorc):
    """ inverso aditivo de un vector complejo

    :param vectorc: vector de numeros complejos
    :return: inverso aditivo del vector ingresado
    :rtype: list
    """
    inverse_v = [(0, 0)] * len(vectorc)
    for x in range(len(vectorc)):
        inverse_v[x] = multiplicacion_complejos((-1, 0), vectorc[x])

    return inverse_v


def suma_vectorescpx(vectorc_1, vectorc_2):
    """ suma de dos vectores complejos

    :param vectorc_1: vector complejo
    :param vectorc_2: vector complejo
    :return: vector suma
    :rtype: list
    """
    if len(vectorc_1) == len(vectorc_2):
        svector = [(0, 0)] * len(vectorc_1)
        for x in range(len(vectorc_1)):
            svector[x] = (suma_complejos(vectorc_1[x], vectorc_2[x]))

    return svector


def potencia_polar(polar1, num):
    """potencia de un numero complejo en representación polar

    :param polar1: numero complejo en representacion polar
    :type polar1: tuple
    :param num: exponente
    :return: potencia del numero complejo
    :rtype: tuple
    """
    potencia_complejo = (round(polar1[0] ** num, 2), round(num * polar1[1], 2))

    return potencia_complejo


def division_polar(polar1, polar2):
    """division de dos numeros complejos en representacion polar

        :param polar1: numero complejo en representacion polar
        :type polar1: tuple
        :param polar2: numero complejo en representacion polar
        :type polar2: tuple
        :return: division entre los numeros complejos en representación polar
        :rtype: tuple
        """
    complejo_polar = (round(polar1[0] / polar2[0], 2), round(polar1[1] - polar2[1], 2))

    return complejo_polar


def multiplicacion_polar(polar1, polar2):
    """multiplicación de dos numeros complejos en representacion polar

    :param polar1: numero complejo en representacion polar
    :type polar1: tuple
    :param polar2: numero complejo en representacion polar
    :type polar2: tuple
    :return: producto entre los numeros complejos en representación polar
    :rtype: tuple
    """
    complejo_polar = (round(polar1[0] * polar2[0], 2), round(polar1[1] + polar2[1], 2))

    return complejo_polar


def rep_cartesiana(par):
    """representa un numero complejo en representanción cartesiana
    
    :param par: representacion polar de un numero complejo
    :type par: tuple
    :return: representación cartesiana de un nnumero complejo
    :rtype: tuple
    """
    complejo = (round(par[0] * math.cos(par[1]), 2), round(par[0] * math.sin(par[1]), 2))

    return complejo


def rep_polar(par):
    """representa un numero complejo en una representacion polar

    :param par: representacion cartesiana de un numero complejo
    :type par: tuple
    :return: representacion polar de un numero complejo
    :rtype: tuple
    """
    p = modulo_complejos(par)
    ang = round(math.atan(par[1] / par[0]), 2)
    result = (p, ang)

    return result


def conjugado_complejos(par):
    """ realiza el conjugado de un numero complejo

    :param par: representacion de un numero complejo en coordenadas cartesianas
    :type par: tuple
    :return: el numero complejo conjugado
    :rtype: tuple
    """
    new_b = par[1] * -1
    new_par = (par[0], new_b)

    return new_par


def modulo_complejos(par):
    """ Realiza el conjugado de un numero complejo

    :param par: representación de un numero complejo en coordenadas cartesianas
    :type par: tuple
    :return: un entero valor del modulo de un numero complejo
    :rtype: int
    """
    modulo = (par[0] ** 2 + par[1] ** 2)

    return round(math.sqrt(modulo), 2)


def division_complejos(par1, par2):
    """

    :param par1: representación de un numero complejo en coordenadas cartesianas
    :type par1: tuple
    :param par2: representación de un numero complejo en coordenadas cartesianas
    :type par2: tuple
    :return: una lista como representación de el numero complejo resultante de la division
    :rtype: tuple
    """
    d = (par2[0] ** 2 + par2[1] ** 2)
    x = (par1[0] * par2[0] + par1[1] * par2[1]) / d
    y = (par2[0] * par1[1] - par1[0] * par2[1]) / d
    result = (round(x, 2), round(y, 2))

    return result


def resta_complejos(par1, par2):
    """Resta de dos numeros complejos

    :param par1: representación de un numero complejo en coordenadas cartesianas
    :type par1: tuple
    :param par2: representación de un numero complejo en coordenadas cartesianas
    :type par2: tuple
    :return: una lista como representación de el numero complejo resultante de la resta
    :rtype: tuple
    """
    result = (par1[0] - par2[0], par1[1] - par2[1])

    return result


def suma_complejos(par1, par2):
    """Suma dos numeros complejos

    :param par1: representación de un numero complejo en coordenadas cartesianas
    :type par1: tuple
    :param par2: representación de un numero complejo en coordenadas cartesianas
    :type par2: tuple
    :return: una lista como representación de el numero complejo resultante de la suma
    :rtype: tuple
    """
    result = (par1[0] + par2[0], par1[1] + par2[1])

    return result


def multiplicacion_complejos(par1, par2):
    """Multiplicacion de dos numeros complejos

    :param par1: representación de un numero complejo en coordenadas cartesianas
    :type par1: tuple
    :param par2: representación de un numero complejo en coordenadas cartesianas
    :type par2: tuple
    :return: una lista como representación de el numero complejo resultante de la multiplicacion
    :rtype: tuple
    """
    result = (round((par1[0] * par2[0]) - (par1[1] * par2[1]), 2), round((par1[0] * par2[1]) + (par1[1] * par2[0]), 2))

    return result


if __name__ == '__main__':
    v = [(2, 3.5), (8.9, 5), (4, 9.2), (6, 2.3)]
    w = [(2.3, 6), (7.4, 8), (3, 3.8), (4, 2.5)]
    complex_n = (4, -3.7)
    matrixc = [[(4, 2), (5, 4.6), (2.3, 5.7)], [(4.3, 5.7), (2, 6.2), (4, 6.8)]]
    matrixc1 = [[(3, 7.1), (9, 10), (5, 3.5)], [(13, 15), (4, 16), (4, 12)]]
#    print(v)
#    print(w)
#    print('suma de los vectores')
#    print(suma_vectorescpx(v, w))
#    print('inverso del vector')
#    print(inverse_vectorcx(v))
#    print('multipliacion por un escalar')
#    print(multi_escalar(complex_n, w))
    print(suma_matricesc(matrixc, matrixc1))
