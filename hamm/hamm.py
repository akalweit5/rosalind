def hamm(s: str, t: str) -> int:
    differences = 0
    assert len(s) == len(t)

    for i in range(len(s)):
        if s[i] != t[i]:
            differences += 1

    return differences
