""" Una clase que representa a un Arco en Redes de Petri """

class Arc:
    """ Los arcos pueden tener nombre y 'multiplicidad' (denominación provisoria) """

    def __init__(self, name = "")
        
        self.name = name
        self.multiplicity = 1 # La multiplicidad por defecto será 1

    def update_multiplicity(self, multiplicity: int)
        """ Este método permite modificar la multiplicidad de un arco a un número natural mayor a 0 """
        
        if (multiplicity < 1):
            raise ValueError('The argument multiplicity must have a natural positive value')

        self.multiplicity = multiplicity

    def get_multiplicity(self) -> int:
        """ Obtener el valor de la v.i. multiplicidad """

        return self.multiplicity
