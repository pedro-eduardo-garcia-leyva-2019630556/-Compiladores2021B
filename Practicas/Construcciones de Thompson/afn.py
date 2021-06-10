class Afn:
    """ AFN que se usa como base para la creacion de plantillas de Thompson """

    def __init__(self):
        self.estados = []
        self.transiciones = {}
        self.edo_inicial = "q0"
        self.edo_final = "q0"
        self.alfabeto = [simbolo for simbolo in "abcfefghijklmnopqrstuvwzE"]
