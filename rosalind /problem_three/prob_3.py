def rose_prob_3(dna: str) -> str:
    list_dna = list(dna)
    for i, char in enumerate(list_dna):
        if char == "A":
            list_dna[i] = "T"
        if char == "T":
            list_dna[i] = "A"
        if char == "C":
            list_dna[i] = "G"
        if char == "G":
            list_dna[i] = "C"
    list_dna.reverse()
    u_dna = "".join(list_dna)
    return u_dna
