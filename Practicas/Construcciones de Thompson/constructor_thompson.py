from plantillas_thomson import PlantillasThompson


class ConstructorThompson:
    """ Construye un AFN por cada operacion en la lista de operaciones y regresa el 
        AFN resultante de todas las operaciones """

    def __init__(self, operaciones, construcciones_simbolos):
        self.construcciones = construcciones_simbolos
        self.operaciones = operaciones

    def obtener_ref_simbolo(self, simbolo, operacion, operaciones):
        """ Obtiene la key del diccionario a la que se refiere el simbolo de entrada """
        if simbolo.isdigit():
            ref = operaciones[int(simbolo)]
        else:
            ref = operacion[0]

        return ref

    def obtener_afn(self, referencia):
        """ Busca el AFN en el diccionario de las construcciones y lo retorna """
        if isinstance(referencia, list):
            afn = self.construcciones[referencia[-1]]
        else:
            afn = self.construcciones[referencia]

        return afn

    def referencia_simbolo_en_construcciones(self, simbolo, operacion):
        """ Obtiene la key del diccionario a la que se refiere el simbolo de entrada """
        if simbolo.isdigit():
            try:
                referencia = operacion[int(simbolo)]
            except:
                referencia = self.operaciones[int(simbolo)]
        else:
            referencia = simbolo
        return referencia

    def obtener_AFN_resultante(self):
        """ Realiza todas las operaciones de la lista de operaciones """
        for operacion in self.operaciones:

            if isinstance(operacion, list):
                # Si la operacion se compone de 2 o mas operaciones, se hace el afn para cada subregex y se agrega al diccionario de construcciones.

                for sub_op in operacion:
                    self.get_afn(sub_op, operacion)

            else:
                if "*" in operacion:
                    # Se agrega el afn de la operacion cierre de la regex  al diccionario de construcciones

                    simbolo = operacion[:-1]    # symbolo*

                    ref = self.obtener_ref_simbolo(
                        simbolo, operacion, self.operaciones)

                    afn_to_star = self.obtener_afn(ref)

                    self.construcciones[operacion] = PlantillasThompson().cierre(
                        afn_to_star)

                elif "|" in operacion:
                    # Se agrega el afn de la operacion union de la regex  al diccionario de construcciones

                    simboloA = operacion[0]
                    simboloB = operacion[2]

                    refA = self.referencia_simbolo_en_construcciones(
                        simboloA, self.operaciones)
                    refB = self.referencia_simbolo_en_construcciones(
                        simboloB, self.operaciones)

                    afnA = self.construcciones[refA]
                    afnB = self.construcciones[refB]

                    self.construcciones[operacion] = PlantillasThompson().union(
                        afnA, afnB)

                else:
                    # Se agrega el afn de la operacion concatenacion de la regex  al diccionario de construcciones

                    simboloA = operacion[0]
                    simboloB = operacion[1]

                    refA = self.referencia_simbolo_en_construcciones(
                        simboloA, self.operaciones)
                    refB = self.referencia_simbolo_en_construcciones(
                        simboloB, self.operaciones)

                    afnA = self.obtener_afn(refA)
                    afnB = self.obtener_afn(refB)

                    self.construcciones[operacion] = PlantillasThompson(
                    ).concatenacion(afnA, afnB)

        return list(self.construcciones.values())[-1]

    def get_afn(self, sub_op, operacion):

        if "*" in sub_op:
            simbolo = sub_op[:-1]  # regex *

            ref = self.obtener_ref_simbolo(
                simbolo, sub_op, operacion)

            afn = self.construcciones[ref]

            self.construcciones[sub_op] = PlantillasThompson().cierre(afn)

        elif "|" in sub_op:
            index_union = sub_op.find("|")

            simboloA = sub_op[:index_union]
            simboloB = sub_op[index_union + 1:]

            refA = self.referencia_simbolo_en_construcciones(
                simboloA, operacion)
            refB = self.referencia_simbolo_en_construcciones(
                simboloB, operacion)

            afnA = self.obtener_afn(refA)
            afnB = self.obtener_afn(refB)

            self.construcciones[sub_op] = PlantillasThompson().union(
                afnA, afnB)

        elif len(sub_op) > 1:

            simboloA = sub_op[0]
            simboloB = sub_op[1]

            refA = self.referencia_simbolo_en_construcciones(
                simboloA, operacion)
            refB = self.referencia_simbolo_en_construcciones(
                simboloB, operacion)

            afnA = self.obtener_afn(refA)
            afnB = self.obtener_afn(refB)

            self.construcciones[sub_op] = PlantillasThompson(
            ).concatenacion(afnA, afnB)
