from Snek.SnekCore import SimpleSnek

def test_SimpleSnek():
    snek = SimpleSnek()
    
    assert type(snek.get_snek()) == str