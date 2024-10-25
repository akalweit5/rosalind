from prob_1 import rose_prob1


def test_prob1() -> bool:
    attempt = rose_prob1(
        "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC",
    )
    answer = "20 12 17 21"
    return attempt == answer


test_prob1()
