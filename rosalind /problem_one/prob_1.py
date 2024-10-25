def rose_prob1(dna: str) -> None:
    count = {}
    num = ["A", "C", "G", "T"]
    num2 = []
    for let in num:
        if let not in count:
            count[let] = 0
    for letter in dna:
        count[letter] += 1
    return f"{count.get('A')} {count.get('C')} {count.get('G')} {count.get('T')}"
