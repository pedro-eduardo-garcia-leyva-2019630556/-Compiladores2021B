from afn import Afn


class PlantillasThompson:
    """ Clase que construye AFNs a partir de las plantillas de Thompson """

    def __init__(self):
        self.afn = Afn()

    def simbolo_alfabeto(self, simbolo):
        """ Plantilla para cualquier simbolo del alfabeto y la cadena vacia epsilon"""
        self.afn.estados.append("q0")
        self.afn.transiciones["q0"] = {
            simbolo: ["q1"]
        }
        self.afn.estados.append("q1")
        self.afn.transiciones["q1"] = {}
        self.afn.edo_final = self.afn.estados[-1]
        self.afn.transiciones[self.afn.edo_final] = {}

        return self.afn

    def concatenacion(self, afnA, afnB):
        """ Plantilla para la concatenacion de dos regex """

        check_afnA = True

        for estado in range(len(afnA.estados) + len(afnB.estados) - 1):
            edo_actual = f"q{estado}"

            if edo_actual == afnA.edo_final:
                check_afnA = False

            if check_afnA:
                self.afn.transiciones[edo_actual] = afnA.transiciones[edo_actual]
            else:
                estadoB = f"q{estado - len(afnA.estados) + 1}"

                for simbolo, edos_sig in afnB.transiciones[estadoB].items():
                    nuevos_edos_sig = [
                        f"q{int(edo[1:])+len(afnA.estados)-1}" for edo in edos_sig]
                    self.afn.transiciones[edo_actual] = {
                        simbolo: nuevos_edos_sig}

            self.afn.estados.append(edo_actual)

        self.afn.edo_final = self.afn.estados[-1]
        self.afn.transiciones[self.afn.edo_final] = {}

        return self.afn

    def union(self, afnA, afnB):
        """ Plantilla para la union de dos regex"""
        unionA = True
        self.afn.estados.append("q0")
        estados_totales = len(afnA.estados) + len(afnB.estados) + 1
        self.afn.edo_final = f"q{estados_totales}"
        self.afn.transiciones["q0"] = {"E": ["q1"]}

        for estado in range(1, estados_totales):
            edo_actual = f"q{estado}"

            if estado > len(afnA.estados):
                unionA = False

            if unionA:
                estadoA = f"q{estado - 1}"
                self.afn.estados.append(edo_actual)
                if estadoA == afnA.edo_final:
                    self.afn.transiciones[edo_actual] = {
                        "E": [self.afn.edo_final]
                    }
                else:
                    for simbolo, edos_sig in afnA.transiciones[estadoA].items():
                        nuevos_edos_sig = [
                            f"q{int(edo[1:])+1}" for edo in edos_sig]
                        self.afn.transiciones[edo_actual] = {
                            simbolo: nuevos_edos_sig
                        }
            else:
                self.afn.estados.append(edo_actual)
                estadoB = estado - len(afnA.estados) - 1

                if estado == estados_totales - 1:
                    self.afn.transiciones[edo_actual] = {
                        "E": [self.afn.edo_final]
                    }

                else:
                    if estado == len(afnA.estados) + 1:
                        self.afn.transiciones["q0"]["E"].append(edo_actual)

                    for simbolo, edos_sig in afnB.transiciones[f"q{estadoB}"].items():
                        nuevos_edos_sig = [
                            f"q{int(edo[1:])+len(afnA.estados)+1}" for edo in edos_sig]
                        self.afn.transiciones[edo_actual] = {
                            simbolo: nuevos_edos_sig
                        }

        self.afn.estados.append(self.afn.edo_final)
        self.afn.transiciones[self.afn.edo_final] = {}
        return self.afn

    def cierre(self, afnA):
        """ Plantilla para la operacion * """
        estados_totales = len(afnA.estados) + 1
        self.afn.estados.append("q0")
        self.afn.edo_final = f"q{estados_totales}"
        self.afn.transiciones["q0"] = {"E": ["q1", self.afn.edo_final]}

        for estado in range(1, estados_totales):
            edo_actual = f"q{estado}"
            estadoA = f"q{estado - 1}"

            self.afn.estados.append(edo_actual)

            if estadoA == afnA.edo_final:
                self.afn.transiciones[edo_actual] = {
                    "E": ["q1", self.afn.edo_final]
                }
            else:
                for simbolo, edos_sig in afnA.transiciones[estadoA].items():
                    nuevos_edos_sig = [
                        f"q{int(edo[1:]) + 1}" for edo in edos_sig]

                    self.afn.transiciones[edo_actual] = {
                        simbolo: nuevos_edos_sig
                    }

        self.afn.transiciones[self.afn.edo_final] = {}
        self.afn.estados.append(self.afn.edo_final)

        return self.afn
