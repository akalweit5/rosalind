from .prob_2 import prob_2


def test_prob2() -> None:
    attempt = prob_2(
        "GATGGAACTTGACTACGTAAATT",
    )
    answer = "GAUGGAACUUGACUACGUAAAUU"
    assert attempt == answer
