from Snek.SnekCore import AbstractSnek


def test_AbstractSnek():
    snek = AbstractSnek()
    assert snek.get_snek() is None
