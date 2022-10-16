from Snek.SnekCore import SimpleSnek

def test_SimpleSnek():
    """
    Test the SimpleSnek class.

    Args:
    """
    snek = SimpleSnek()
    
    assert type(snek.get_snek()) == str