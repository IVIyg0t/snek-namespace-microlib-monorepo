from Snek.CuteSnek import CuteSnek, cute_snek


def test_CuteSnek():
    """
    Test that the CuteSnek object can be used.

    Args:
    """
    snek = CuteSnek()

    assert snek.get_snek() == cute_snek
