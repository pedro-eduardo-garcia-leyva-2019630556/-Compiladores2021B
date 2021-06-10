
class PrecedenciaOperadores:
    """ Clase que recorre y sustituye las sub_regex de una regex con un No. de operacion con base en la precedencia de operadores para expresiones regulares"""

    def __init__(self):
        self.operaciones = []

    def parentesis(self, regex):
        """ Se revisa si hay alguna sub_regex dentro de parentesis de la regex original y se agrega a la lista ordenada de operaciones"""
        stack_index = []
        stack_parentesis = []
        sub_regex = []
        i = 0
        while(True):
            if(i >= len(regex)):
                break
            if regex[i] == '(':
                stack_parentesis.append('(')
                stack_index.append(i+1)
            elif regex[i] == ')' and stack_parentesis[-1] == '(':
                top = stack_index[-1]

                # Se agrega la sub_regex a la lista
                sub_regex.append(regex[top: i])

                # Se comprueba si la sub_regex esta al inicio de la regex

                if top == 1:
                    regex = str(len(sub_regex) - 1) + regex[i+1:]
                else:
                    regex = regex[:top-1] + \
                        str(len(sub_regex) - 1) + regex[i+1:]

                # Se reinicia la busqueda
                stack_index.pop()
                stack_parentesis.pop()
                i = -1
            i += 1

        # Se revisan todas las operaciones de las sub_regex encontradas anteriormente
        for op in range(len(sub_regex)):
            self.operaciones.append([])  # sub_regex[op]
            self.cierre(sub_regex[op], op)

        self.cierre(regex, -1)
        return self.operaciones

    def cierre(self, regex, sub_regex):
        """ Se buscan operaciones * en la regex que se recibe y se agrega a la lista ordenada de operaciones"""
        i = 0

        while(True):

            if i >= len(regex):
                break

            if regex[i] == '*':

                if sub_regex != -1:  # Si es una sub_regex
                    self.operaciones[sub_regex].append(
                        regex[i-1:i+1])  # regex*
                    regex = regex[:i-1] + \
                        str(len(self.operaciones[sub_regex]) - 1) + regex[i+1:]

                else:
                    self.operaciones.append(regex[i-1:i+1])  # append(symbol*)
                    regex = regex[:i-1] + \
                        str(len(self.operaciones) - 1) + regex[i+1:]

                    # regex =  regex_#op_regex

                i = -1
            i += 1

        self.concatenacion(regex, sub_regex)

    def concatenacion(self, regex, sub_regex=-1):
        """ Se realizan todas las posibles concatenaciones de la regex en el orden correcto """

        i = 0
        while(True):
            # Debe haber por lo menos 2 simbolos
            if len(regex) < 2 or i >= len(regex) - 1:
                break

            if regex[i] != '|' and regex[i+1] != "|":
                if sub_regex != -1:  # Si es una sub_regex
                    self.operaciones[sub_regex].append(regex[i:i+2])

                    regex = regex[:i] + \
                        str(len(self.operaciones[sub_regex]) - 1) + regex[i+2:]
                    # inicio_regex + No.Op + final_regex
                else:
                    self.operaciones.append(regex[i:i+2])

                    regex = regex[:i] + \
                        str(len(self.operaciones) - 1) + regex[i+2:]
                i = -1
            i += 1

        self.union(regex, sub_regex)

    def union(self, regex, sub_regex=-1):
        """ Se sustituyen todas las uniones de la regex por su correspondiente No. de operacion y se agregan a la lista ordenada de operaciones"""
        i = 0

        while True:
            if i >= len(regex) - 2:
                break
            if regex[i] != "|" and regex[i+1] == "|":
                if sub_regex != -1:  # Si es una sub_regex
                    self.operaciones[sub_regex].append(regex[i:i+3])
                    regex = str(
                        len(self.operaciones[sub_regex]) - 1) + regex[i+3:]
                else:
                    self.operaciones.append(regex[i:i+3])
                    regex = str(len(self.operaciones) - 1) + regex[i+3:]

                i = -1
            i += 1
