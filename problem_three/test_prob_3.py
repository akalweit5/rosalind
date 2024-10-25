from .prob_3 import rose_prob_3


def test_prob1() -> None:
    attempt = rose_prob_3(
        "AAAACCCGGT",
    )
    answer = "ACCGGGTTTT"
    assert attempt == answer
