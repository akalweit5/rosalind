def hamm(s: str, t: str) -> int:
    s_list = list(s)
    t_list = list(t)
    differences = 0
    assert len(s) == len(t)

    for i in range(len(s_list)):
        if s_list[i] != t_list[i]:
            differences += 1

    return differences
