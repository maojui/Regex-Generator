import random
from .const import *

numbers                 = lambda x: x in DIGIT
upper_alpha             = lambda x: x in UPPER
lower_alpha             = lambda x: x in LOWER
alpha                   = lambda x: x in LETTERS
upper_hexdigit          = lambda x: x in UPPER_HEXDIGIT
lower_hexdigit          = lambda x: x in LOWER_HEXDIGIT
words                   = lambda x: x in WORD
space                   = lambda x: x in SPACE
space_only              = lambda x: x in ' '
escape                  = lambda x: x in ESCAPE
symbol                  = lambda x: x in SYMBOL
char_range              = lambda x: x in CHAR_RANGE
char_range_letter       = lambda x: x in CHAR_RANGE_WITH_SYMBOLS
char_range_col          = lambda x: x in CHAR_RANGE
char_range_letter_col   = lambda x: x in CHAR_RANGE_WITH_SYMBOLS
char_range_digit_col    = lambda x: x in DIGIT
char_range_upper_col    = lambda x: x in UPPER
char_range_lower_col    = lambda x: x in LOWER
anything                = lambda x: True
char_or                 = lambda x: True
string_or               = lambda x: True

genotype = {
    0x00 : numbers,                 # \d                            numbers
    0x01 : upper_alpha,             # [A-Z]                         upper alpha
    0x02 : lower_alpha,             # [a-z]                         lower alpha
    0x03 : alpha,                   # [A-Za-z]                      alpha
    0x04 : upper_hexdigit,          # [0-9A-F]                      upper hexdigits
    0x05 : lower_hexdigit,          # [0-9a-f]                      lower hexdigits
    0x06 : words,                   # \w                            words
    0x07 : space,                   # \s                            space like
    0x08 : space_only,              # [ ]                           space only
    0x09 : anything,                # .                             anything
    0x0a : escape,                  # [{}^$.|*+?]                   escape
    0x0b : symbol,                  # [SYMBOLS]                     symbol
    0x0c : char_range,              # [?-??-?]                      range for A-Z a-z 0-9 and symbols
    0x0d : char_range_letter,       # [?-??-?]                      range for only A-Z a-z 0-9
    0x0e : char_or,                 # [???]                         char or
    0x0f : string_or,               # (??|???|?)                    string or
    0x10 : char_range_col,          # [?-??-?][?-??-?][?-??-?]?     This gene parse letter & symbol column by column
    0x11 : char_range_letter_col,   # [?-??-?][?-??-?][?-??-?]?     This gene parse letter column by column
    0x12 : char_range_digit_col,    # [?-?][?-?][?-?]?              This gene parse digit column by column
    0x13 : char_range_upper_col,    # [?-?][?-?][?-?]?              This gene parse upper column by column
    0x14 : char_range_lower_col,    # [?-?][?-?][?-?]?              This gene parse lower column by column
}

def substitute_col(process, columns, gene, sym) :
    indices = []
    # Find empty col
    for idx in range(min([len(p) for p in process])) :
        for i in range(len(process)) : 
            if process[i][idx] != None :
                break
        else :
            indices.append(idx)
    # Replace those col
    for idx in indices :
        for i in range(len(process)) : 
            if process[i][idx] != None or not genotype[gene ^ 0x80](columns[i][idx]):
                break
        else :
            for i in range(len(process)) : 
                process[i][idx] = sym
    return process

def substitute(process, string, gene, sym):
    for idx, c in enumerate(string):
        if process[idx] == None and genotype[gene](c):
            process[idx] = sym
    return process

def encoder(columns, order):
    """
    把字串重新歸類，照 genotype dictionary 做事。
    ABC -> 5 5 5
    """
    output = []
    process = [[None] * len(c) for c in columns]
    for idx, row in enumerate(columns):
        for gene in order :
            if not None in process[idx] : break
            if gene in genotype  :
                process[idx] = substitute(process[idx], row, gene, INDEX_TABLE(gene))
            elif idx == 0:
                process = substitute_col(process, columns, gene, INDEX_TABLE(gene))
    return process

def mutation(gene):
    idx = random.choice(range(len(gene)))
    gene[idx] ^= 0x80
    return gene

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

def nextGeneration(population, fitness):
    
    min_fitness = min(fitness)
    if min_fitness < 0 :
        fitness = [min_fitness + f for f in fitness]
    prob = [f for f in fitness]
    
    offspring = []
    for _ in range(len(population)//2):
        
        p1, p2 = random.choices(population, weights=prob, k=2)
        
        # clean mutation
        c1 = [ p& 0x7f for p in p1] 
        c2 = [ p& 0x7f for p in p2]
        
        if random.randint(0,100) < 30 : 
            o1 = crossover(c1, c2)
            for i in range(len(p1)) :
                idx1 = o1.index(p1[i]& 0x7f)
                o1[idx1] = p1[i]
        else :
            o1 = p1
        
        if random.randint(0,100) < 30 : 
            o2 = crossover(c2, c1)
            for i in range(len(p1)) :
                idx2 = o2.index(p2[i]& 0x7f)
                o2[idx2] = p2[i]
        else :
            o2 = p2
            
        if random.randint(0,100) < 5 : 
            o1 = mutation(o1)
        if random.randint(0,100) < 7 : 
            o2 = mutation(o2)
        
        offspring.append(o1)
        offspring.append(o2)
    return offspring


if __name__ == "__main__":
    
    target = ['00000','BBBBBB','ccccc']
    order = [0,1,2,3,4,5,6,7,8,9]
    print(encoder(target,order))