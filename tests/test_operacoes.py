from calc.operacoes import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(5, 2) == 3

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_zero():
    import pytest
    with pytest.raises(ValueError):
        dividir(10, 0)
