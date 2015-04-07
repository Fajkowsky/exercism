conversion = dict(zip("GCTA", "CGAU"))


def to_rna(dna):
    return ''.join((conversion[item] for item in dna))