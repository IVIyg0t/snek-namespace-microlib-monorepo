from Snek.FancySnek import FancySnek, fancy_snek


def test_FancySnek():
    """
    Test that the snek object is the correct one.

    Args:
    """
    snek = FancySnek()

    assert snek.get_snek() == fancy_snek
