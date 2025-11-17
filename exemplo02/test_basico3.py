def somar(a,b):
    return a + b

def comprimento(lista):
    return len(lista)

def test_somar():
    assert somar(1,1) == 2
    assert somar(2,2) == 4

def test_comprimento():
    assert comprimento([1, 2, 3, "banana", "maçã", True]) == 6

def test_somar_e_comprimento():
    assert comprimento([1, 2, 3, "banana", "maçã", True]) == 6
    assert somar(2,2) == 4