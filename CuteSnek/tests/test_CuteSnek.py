from Snek.CuteSnek import CuteSnek, CUTE_SNEK


def test_CuteSnek():
    snek = CuteSnek()

    assert snek.get_snek() == CUTE_SNEK
