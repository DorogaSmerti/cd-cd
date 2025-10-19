from app import add

def test_add():
    assert add(1, 6) == 7
    assert add(4, 6) == 10
    assert add(1, 3) == 4