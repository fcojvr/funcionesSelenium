import pytest

@pytest.mark.validar
def test_validar_():
    nom1="Franco"
    nom2="Fran"

    assert nom1==nom2, "No son iguales test no paso"
    