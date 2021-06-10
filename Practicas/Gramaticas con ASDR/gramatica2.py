import sys

""" 
    Gramatica:
        A->BCDEa
        B->bCD
        B->a
        C->cA
        C->f
        D->d
        E->e
"""

string = "afdea"
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
    B()
    C()
    D()
    E()
    if not consumir('a'):
        sys.exit("No pertenece")

def B():
    if consumir('b'):
        C()
        D()
    elif not consumir('a'):
        sys.exit("No pertenece")

def C():
    if consumir('c'):
        A()
    elif not consumir('f'):
        sys.exit("No pertenece")

def D():
    if not consumir('d'):
        sys.exit("No pertenece")

def E():
    if not consumir('e'):
        sys.exit("No pertenece")

if __name__ == "__main__":
    A()
    if index == len(string):
        print("Si pertenece")
    else:
        print("No pertenece")