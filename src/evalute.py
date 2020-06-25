import re
from .const import INDEX_TABLE

__all__ = ['fitness']

score_table = {
    INDEX_TABLE(0x0) : 10,
    INDEX_TABLE(0x1) : 26,
    INDEX_TABLE(0x2) : 26,
    INDEX_TABLE(0x3) : 52,
    INDEX_TABLE(0x4) : 16,
    INDEX_TABLE(0x5) : 16,
    INDEX_TABLE(0x6) : 72,
    INDEX_TABLE(0x7) : 5,
    INDEX_TABLE(0x8) : 1,
    INDEX_TABLE(0x9) : 100,
    INDEX_TABLE(0xa) : 20,
    INDEX_TABLE(0xb) : 20,
    INDEX_TABLE(0xc) : 100,
    INDEX_TABLE(0xd) : 100,
    INDEX_TABLE(0xe) : 100,
    INDEX_TABLE(0xf) : 100,
    INDEX_TABLE(0x10) : 20,
    INDEX_TABLE(0x11) : 30,
    INDEX_TABLE(0x12) : 30,
    INDEX_TABLE(0x13) : 30,
    INDEX_TABLE(0x14) : 30,
}

def fitness(regex, seq, positive, negative=[]):
    # init
    score = 1000

    # 可以 Match
    for t in positive:
        if not re.search(regex, t):
            print(regex, t)
            return -1e9

    # 不可以 Match
    for t in negative:
        if re.search(regex, t):
            return -1e9

    # regex 長度 (-)
    score -= 3 * len(regex)
    if len(regex) > 100 :
        score *= 0.9
        score = int(score)
    
    # or 數量
    if '|' in regex and regex.count('|') < 5:
        score += 30 
    else : 
        score -= 10 *regex.count('|')

    # 覆蓋率 (可 generalize 度)
    # 基因分層分數
    for g in set(seq):
        score -= score_table[INDEX_TABLE(ord(g) & 0x7f)]

    # 單純度 
    score -= 10 * len(set(seq))
    score -= 10 * len(seq)

    # .* or .+
    score -= 20 * (regex.count('.*') + regex.count('.+'))

    return score


