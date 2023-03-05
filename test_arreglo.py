from arreglo import menor

def test_menor():
    assert menor([2,5]) == 2
    assert menor([2,2]) == 2
    assert menor([2,1]) == 1
    assert menor([9,1]) == 1
    assert menor([5,7]) == 5