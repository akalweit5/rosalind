def motif(s: str, t: str, index_list: list = []) -> str:
    idx = s.find(t)
    if idx == -1:
        return " ".join(index_list)

    if str(idx + 1) not in index_list:
        index_list.append(str(idx + 1))
    s = s.replace(s[idx], "*", 1)

    return motif(s, t, index_list)
