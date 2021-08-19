"""Libreria de operaciones basicas con numeros complejos

"""

import math


def potencia_polar(polar1, num):
    """potencia de un numero complejo en representación polar

    :param polar1: numero complejo en representacion polar
    :type polar1: list
    :param num: exponente
    :return: potencia del numero complejo
    :rtype: list
    """
    potencia_complejo = [polar1[0]**num, num * polar1[1]]

    return potencia_complejo


def division_polar(polar1, polar2):
    """division de dos numeros complejos en representacion polar

        :param polar1: numero complejo en representacion polar
        :type polar1: list
        :param polar2: numero complejo en representacion polar
        :type polar2: list
        :return: division entre los numeros complejos en representación polar
        :rtype: list
        """
    complejo_polar = [polar1[0] / polar2[0], polar1[1] - polar2[1]]

    return complejo_polar


def multiplicacion_polar(polar1, polar2):
    """multiplicación de dos numeros complejos en representacion polar

    :param polar1: numero complejo en representacion polar
    :type polar1: list
    :param polar2: numero complejo en representacion polar
    :type polar2: list
    :return: producto entre los numeros complejos en representación polar
    :rtype: list
    """
    complejo_polar = [polar1[0] * polar2[0], polar1[1] + polar2[1]]

    return complejo_polar


def rep_cartesiana(par):
    """representa un numero complejo en representanción cartesiana
    
    :param par: representacion polar de un numero complejo
    :type par: list
    :return: representación cartesiana de un nnumero complejo
    :rtype: list
    """
    complejo = [par[0] * math.cos(par[1]), par[0] * math.sin(par[1])]

    return complejo


def rep_polar(par):
    """representa un numero complejo en una representacion polar

    :param par: representacion cartesiana de un numero complejo
    :type par: list
    :return: representacion polar de un numero complejo
    :rtype: list
    """
    p = modulo_complejos(par)
    ang = math.atan(par[1] / par[0])
    result = [p, ang]

    return result


def conjugado_complejos(par):
    """ realiza el conjugado de un numero complejo

    :param par: representacion de un numero complejo en coordenadas cartesianas
    :type par: list
    :return: el numero complejo conjugado
    :rtype: list
    """
    new_b = par[1] * -1
    new_par = [par[0], new_b]

    return new_par


def modulo_complejos(par):
    """ Realiza el conjugado de un numero complejo

    :param par: representación de un numero complejo en coordenadas cartesianas
    :type par: list
    :return: un entero valor del modulo de un numero complejo
    :rtype: int
    """
    modulo = (par[0] ** 2 + par[1] ** 2)

    return math.sqrt(modulo)


def division_complejos(par1, par2):
    """

    :param par1: representación de un numero complejo en coordenadas cartesianas
    :type par1: list
    :param par2: representación de un numero complejo en coordenadas cartesianas
    :type par2: list
    :return: una lista como representación de el numero complejo resultante de la division
    :rtype: list
    """
    d = (par2[0] ** 2 + par2[1] ** 2)
    x = (par1[0] * par2[0] + par1[1] * par2[1]) / d
    y = (par2[0] * par1[1] - par1[0] * par2[1]) / d
    result = [x, y]

    return result


def resta_complejos(par1, par2):
    """Resta de dos numeros complejos

    :param par1: representación de un numero complejo en coordenadas cartesianas
    :type par1: list
    :param par2: representación de un numero complejo en coordenadas cartesianas
    :type par2: list
    :return: una lista como representación de el numero complejo resultante de la resta
    :rtype: list
    """
    result = [par1[0] - par2[0], par1[1] - par2[1]]

    return result


def suma_complejos(par1, par2):
    """Suma dos numeros complejos

    :param par1: representación de un numero complejo en coordenadas cartesianas
    :type par1: list
    :param par2: representación de un numero complejo en coordenadas cartesianas
    :type par2: list
    :return: una lista como representación de el numero complejo resultante de la suma
    :rtype: list
    """
    result = [par1[0] + par2[0], par1[1] + par2[1]]

    return result


def multiplicacion_complejos(par1, par2):
    """Multiplicacion de dos numeros complejos

    :param par1: representación de un numero complejo en coordenadas cartesianas
    :type par1: list
    :param par2: representación de un numero complejo en coordenadas cartesianas
    :type par2: list
    :return: una lista como representación de el numero complejo resultante de la multiplicacion
    :rtype: list
    """
    result = [(par1[0] * par2[0]) - (par1[1] * par2[1]), (par1[0] * par2[1]) + (par1[1] * par2[0])]

    return result
