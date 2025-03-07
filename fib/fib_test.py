from .fib_problem import fib


def test_prob1() -> None:
    attempt = fib(n=5, k=3)
    answer = 19

    assert attempt == answer
