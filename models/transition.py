""" Una clase que representa a una Transicion en Redes de Petri """

class Transition:
    """ Esta clase puede tener un nombre de manera opcional """

    def __init__(self, name = ""):
        self.name = name
