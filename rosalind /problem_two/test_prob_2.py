from prob_2 import rose_prob_2


def test_prob1() -> bool:
    attempt = rose_prob_2(
        "GATGGAACTTGACTACGTAAATTC",
    )
    answer = "GAUGGAACUUGACUACGUAAAU"
    return attempt == answer
