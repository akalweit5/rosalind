from .hamm import hamm


def test_hamm() -> None:
    attempt = hamm(s="GAGCCTACTAACGGGAT", t="CATCGTAATGACGGCCT")

    answer = 7

    assert attempt == answer
