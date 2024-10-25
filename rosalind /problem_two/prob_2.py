def prob_2(dna:str)-> str: 
    list_dna = list(dna)
    for i, char in enumerate(list_dna): 
        if char == 'T':
            list_dna[i] = "U"
    u_dna = "".join(list_dna)
    return u_dna
