import types
import string
from const import *

numbers             = lambda x: x in DIGIT
upper_alpha         = lambda x: x in UPPER
lower_alpha         = lambda x: x in LOWER
alpha               = lambda x: x in LETTERS
upper_hexdigit      = lambda x: x in UPPER_HEXDIGIT
lower_hexdigit      = lambda x: x in LOWER_HEXDIGIT
words               = lambda x: x in WORD
space               = lambda x: x in SPACE
space_only          = lambda x: x in ' '
escape              = lambda x: x in ESCAPE
symbol              = lambda x: x in SYMBOL
char_range          = lambda x: x in CHAR_RANGE
char_range_letter   = lambda x: x in CHAR_RANGE_WITH_SYMBOLS
anything            = lambda x: True
char_or             = lambda x: True
string_or           = lambda x: True

__gene = {
    # 跟 Rule 有關的
    0x0: numbers,           # \d              numbers
    0x1: upper_alpha,       # [A-Z]           upper alpha
    0x2: lower_alpha,       # [a-z]           lower alpha
    0x3: alpha,             # [A-Za-z]        alpha
    0x4: upper_hexdigit,    # [0-9A-F]        upper hexdigits
    0x5: lower_hexdigit,    # [0-9a-f]        lower hexdigits
    0x6: words,             # \w              words
    0x7: space,             # \s              space like
    0x8: space_only,        # [ ]             space only
    0x9: anything,          # .               anything

    # 跟 value 有關的
    0xa: escape,            # [{}^$.|*+?]    escape
    0xb: symbol,            # [SYMBOLS]      symbol
    0xc: char_range,        # [?-??-?]       range for A-Z a-z 0-9 and symbols
    0xd: char_range_letter, # [?-??-?]       range for only A-Z a-z 0-9
    0xe: char_or,           # [???]          char or
    0xf: string_or,         # (??|???|?)     string or
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
            if process[i][idx] != None or not __gene[gene ^ 0x80](columns[i][idx]):
                break
        else :
            for i in range(len(process)) : 
                process[i][idx] = sym
    return process

def substitute(process, string, gene, sym):
    for idx, c in enumerate(string):
        if process[idx] == None and __gene[gene](c):
            process[idx] = sym
    return process

def encoder(columns, order):
    """
    把字串重新歸類，照 __gene dictionary 做事。
    ABC -> 5 5 5
    """
    output = []
    process = [[None] * len(c) for c in columns]
    for idx, row in enumerate(columns):
        for gene in order :
            if not None in process[idx] : break
            if gene in __gene  :
                process[idx] = substitute(process[idx], row, gene, INDEX_TABLE(gene))
            elif idx == 0:
                process = substitute_col(process, columns, gene, INDEX_TABLE(gene))
    return process

if __name__ == "__main__":
    
    target = ['00000','BBBBBB','ccccc']
    order = [0,1,2,3,4,5,6,7,8,9]
    print(encoder(target,order))