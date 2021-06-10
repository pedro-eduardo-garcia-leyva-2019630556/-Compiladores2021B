import sys

""" 
    Gramatica:
        A -> aBa
        B -> bAb
        B -> c
"""

string = "ababacababa"
index = 0


def consumir(simbolo):
    global index

    if index >= len(string):
        sys.exit("No pertenece")
    elif string[index] == simbolo:
        index += 1
        return True
    return False


def A():
    if consumir('a'):
        B()
        if not consumir('a'):
            sys.exit("No pertenece")
    else:
        sys.exit("No pertenece")


def B():
    if consumir('b'):
        A()
        if not consumir('b'):
            sys.exit("No pertenece")
    elif not consumir('c'):
        sys.exit("No pertenece")


if __name__ == "__main__":
    A()
    if index == len(string):
        print("Si pertenece")
    else:
        print("No pertenece")
