def rose_prob1(dna: str) -> str:
    count = {}
    bases = ["A", "C", "G", "T"]
    for base in bases:
        if base not in count:
            count[base] = 0
    for base in dna:
        if base not in bases:
            continue
        count[base] += 1
    return f"{count.get('A')} {count.get('C')} {count.get('G')} {count.get('T')}"
