from Snek.CuteSnek import CuteSnek, cute_snek


def test_CuteSnek():
    snek = CuteSnek()

    assert snek.get_snek() == cute_snek
