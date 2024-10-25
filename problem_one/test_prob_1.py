from .prob_1 import rose_prob1


def test_prob1() -> None:
    attempt = rose_prob1(
        "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC",
    )
    answer = "20 12 17 21"

    assert attempt == answer
