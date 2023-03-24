from Snek.FancySnek import FancySnek, FANCY_SNEK


def test_FancySnek():
    snek = FancySnek()

    assert snek.get_snek() == FANCY_SNEK
