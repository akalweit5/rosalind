from .motif import motif


def test_motif() -> None:
    attempt = motif(s="GATATATGCATATACTT", t="ATAT")

    answer = "2 4 10"

    assert attempt == answer
