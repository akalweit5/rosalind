def fib(n: int, k: int, count: int = 1, curr_pairs: int = 1, prev_pair: int = 1):
    if count == n - 1:
        return curr_pairs
    next_pairs = prev_pair * k + curr_pairs

    return fib(n, k, count=count + 1, curr_pairs=next_pairs, prev_pair=curr_pairs)
