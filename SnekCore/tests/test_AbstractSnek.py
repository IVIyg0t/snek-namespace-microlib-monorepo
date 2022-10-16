from Snek.SnekCore import Snek


def test_AbstractSnek():
    """
    Test that Snek object can be safely retrieved from the abstract Snek object.

    Args:
    """
    snek = Snek()
    assert snek.get_snek() is None
