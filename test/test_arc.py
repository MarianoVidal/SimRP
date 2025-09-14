""" Módulo de testing para la clase Arc de /models/ """

import pytest

# Importar desde el directorio padre

import sys
sys.path.append('../models')
from arc import Arc

# Tests

def test_instantiation():
    """ Testear que la clase se instancie correctamente """

    test_arc_1 = Arc()
    test_arc_2 = Arc('test')

    assert test_arc_1.name == ''
    assert test_arc_2.name == 'test'

def test_update_multiplicity():
    """ Testear que la función 'update_multiplicity' actúe correctamente """

    test_arc = Arc()
    
    test_arc.update_multiplicity(1)
    assert test_arc.get_multiplicity() == 1

    test_arc.update_multiplicity(10)
    assert test_arc.get_multiplicity() == 10

    with pytest.raises(ValueError) as exc_info:
        test_arc.update_multiplicity(0)
    assert "The argument multiplicity must have a natural positive value" in str(exc_info.value)
