from prob_3 import rose_prob_3


def test_prob1() -> bool:
    attempt = rose_prob_3(
        "AAAACCCGGT",
    )
    answer = "ACCGGGTTTT"
    return attempt == answer
