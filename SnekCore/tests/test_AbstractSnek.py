from Snek.SnekCore import Snek


def test_AbstractSnek():
    snek = Snek()
    assert snek.get_snek() is None
