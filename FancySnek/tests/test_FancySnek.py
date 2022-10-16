from Snek.FancySnek import FancySnek, fancy_snek


def test_FancySnek():
    snek = FancySnek()

    assert snek.get_snek() == fancy_snek
