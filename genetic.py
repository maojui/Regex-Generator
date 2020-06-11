import random


def mutation(p):
    return p[::-1]


def crossover(p1, p2, mask=None):
    """
    Partially Mapped Crossover
    """
    mask = [random.randint(0, 1)
            for i in range(len(p1))] if mask == None else mask
    gene = [None for i in range(len(p1))]
    for idx, b in enumerate(mask):
        gene[idx] = p1[idx] if b == 1 else None
    p1_al = set(gene)  # parent1 already
    for idx, b in enumerate(mask):
        if b != 1:
            continue
        if p2[idx] in p1_al:
            continue
        p1idx = idx
        p2v = p2[idx]
        while True:
            p2idx = p2.index(p1[p1idx])
            if mask[p2idx] == 1:
                p1idx = p2idx
                continue
            if gene[p2idx] == None:
                gene[p2idx] = p2v
            break
    for idx, g in enumerate(gene.copy()):
        if gene[idx] == None:
            gene[idx] = p2[idx]
    return gene
