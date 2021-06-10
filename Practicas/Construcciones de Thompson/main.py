""" 
    Programa: Algoritmo de Thompson
    Elaborado por: Pedro Eduardo Garcia Leyva
    Materia : Compiladores
    Grupo: 3CV15
"""


from plantillas_thomson import PlantillasThompson
from precedencia_operadores import PrecedenciaOperadores
from constructor_thompson import ConstructorThompson
import sys


def print_afn(afn, regex, alfabeto):
    """ Imprime los elementos que conforman al AFN de entrada """
    print(f"Conversion de la regex {regex} a AFN\n")
    print(f"Alfabeto: {alfabeto}")
    print(f"Estado Inicial: {afn.edo_inicial}")
    print(f"Estado Final: {afn.edo_final}")
    print(f"Estados: {afn.estados}")
    print(f"Transiciones:\n")

    for estado, transicion in afn.transiciones.items():
        for simbolo, edo_sig in transicion.items():
            for edo in edo_sig:
                print(f"\t({estado},{simbolo}) -> {edo}")


if __name__ == "__main__":

    ejemplos = [
        "a(a|b)*(a(c|b))",
        "E*",
        "a****",
        "(ab|cb*|cb)*",
        "a*b*|cab",
    ]
    print("Ejemplos de regex:")
    [print(f"\t{i+1}. {ejemplos[i]}") for i in range(len(ejemplos))]
    regex = input(
        f"Ingrese una regex o seleccione un ejemplo: \n")

    if regex in [str(n) for n in range(1, 6)]:
        regex = ejemplos[int(regex)-1]

    alfabeto_principal = [simbolo for simbolo in "abcfefghijklmnopqrstuvwzE"]
    alfabeto = set([])
    operadores = ["(", ")", "*", "|"]

    construcciones_simbolos = {}

    for simbolo in regex:
        if simbolo in alfabeto_principal:
            alfabeto.add(simbolo)
            construcciones_simbolos[simbolo] = PlantillasThompson(
            ).simbolo_alfabeto(simbolo)
        elif not simbolo in operadores:
            sys.exit(f"El simbolo {simbolo} no pertenece al alfabeto.")

    operaciones_ordenadas = PrecedenciaOperadores().parentesis(regex)

    construcciones = ConstructorThompson(
        operaciones_ordenadas, construcciones_simbolos)

    # imprime el AFN que representa a toda la regex
    print_afn(construcciones.obtener_AFN_resultante(), regex, alfabeto)
