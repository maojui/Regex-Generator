import random
import string
import numpy as np
from utils import longest_common_subseqence as lcs

#    0   [0-9]       numbers
#    1   [A-Z]       upper alpha
#    2   [a-z]       lower alpha
#    3   [0-9A-F]    upper hexdigits
#    4   [0-9a-f]    lower hexdigits
#    5   \w          words
#    6   \s          space
#    7   [ ]
#    8   [.]
#    9   [/]
#   10  [\-+]                   
#   11  .           any char    | -1000000000000
#   12  [?-?^?]     range       | #^
#   13  [???]       char or     | -n
#   14  (??|???|?)  string or   | fitness = -sum(entropy of each string) * n

__all__ = ['parser']

def numbers(process, string):
    for idx,c in enumerate(string):
        if process[idx] == None and c in "'1234567890" :
            process[idx] = '0'
    return process

def upper_alpha(process, string):
    for idx,c in enumerate(string):
        if process[idx] == None and c in "ABCDEFGHIJKLMNOPWRSTUVWXYZ" :
            process[idx] = '1'
    return process

def lower_alpha(process, string):
    for idx,c in enumerate(string):
        if process[idx] == None and c in "abcdefghijklmnopqrstuvwxyz" :
            process[idx] = '2'
    return process

def upper_hexdigit(process, string):
    for idx,c in enumerate(string):
        if process[idx] == None and c in "0123456789ABCDEF" :
            process[idx] = '3'
    return process

def lower_hexdigit(process, string):
    for idx,c in enumerate(string):
        if process[idx] == None and c in "0123456789abcdef" :
            process[idx] = '4'
    return process

WORD = string.ascii_letters + string.digits + '_'
def words(process, string):
    for idx,c in enumerate(string):
        if process[idx] == None and c in WORD :
            process[idx] = '5'
    return process

SPACE = '\x0c\n\r\t\x0b\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u200a\u2028\u2029\u202f\u205f\u3000\ufeff'
def space(process, string):
    for idx,c in enumerate(string):
        if process[idx] == None and c in SPACE :
            process[idx] = '6'
    return process

def anything(process, string) :
    for idx in range(len(process)) :
        if process[idx] == None:
            process[idx] = 'b'
    return process

def string_or(process, string) :
    for idx in range(len(process)) :
        if process[idx] == None:
            process[idx] = 'e'
    return process

__gene = {
    # 跟 Rule 有關的
    0x0   : numbers,
    0x1   : upper_alpha,
    0x2   : lower_alpha,
    0x3   : upper_hexdigit,
    0x4   : lower_hexdigit,
    0x5   : words,
    0x6   : space,
    0xb   : anything,

    # 跟 value 有關的
    0xe   : string_or,
}


def string_or_imple(strs) :
    setstr = set(strs)
    if len(setstr) > 1 :
        return f"({'|'.join(setstr)})"
    elif len(setstr) == 1 :
        return list(setstr)[0]
    return ''

# 處理 value
formatting = {
    'e': string_or_imple
}

regex_table = {
    # 跟 Rule 有關的
    '0' : '\d',
    '1' : '[A-Z]', 
    '2' : '[a-z]', 
    '3' : '[0-9A-F]', 
    '4' : '[0-9a-f]', 
    '5' :  '\w',
    '6' :  '\s',
    '7' :  '',
    '8' :  '',
    '9' :  '',
    'a' :  '',
    'b' :  '.',

    # 跟 value 有關的
    'e' :  'e',
}

# 把字串重新歸類，照 __gene dictionary 做事
# ABC -> 5 5 5
def encoder(columns, order):
    output  = []
    process = [[None] * len(c) for c in columns]
    for idx, c in enumerate(columns) :
        for i in order:
            process[idx] = __gene[i](process[idx], c)
    return process

# 化簡，算數量
# [['e', 'e', 'e', 'e', 'e'], ['e', 'e'], ['e', 'e', 'e', 'e']] -> [[('e', 5)], [('e', 2)], [('e', 4)]]
def type_counter(columns) :
    output = []
    for column in columns :
        out = []
        cur = None
        count = 0
        for i in column :
            if i != cur :
                out.append((cur, count)) if cur != None else None
                cur = i 
                count = 0
            count +=1 
        out.append((cur, count)) if cur != None else None
        output.append(out)
    return output

# Recursive 的找出最長的序列，看 test.py
def find_most_sequence(seq, target, cur=[], inc=0, idx=0) :
    if target == '' :
        return cur, inc

    cur1 = cur.copy()
    cur2 = cur.copy()
    loc = -1
    val = inc

    for i in range(len(seq)) :
        if seq[i][0] == target[0] :
            loc = i
            val += seq[i][1]
            break
    if loc != -1 :
        # idx += 1
        idx = idx + loc + 1
        # Dont take
        cur1, a = find_most_sequence(seq[loc+1:], target, cur1, inc, idx)
        # Take it
        cur2.append(idx)
        cur2, b = find_most_sequence(seq[loc+1:], target[1:], cur2, val, idx)
        if a >= b:
            return cur1, a
        return cur2, b
    else :
        return [], 0

# 算 rule 的次數
def freq_counter(cnts) :
    std = np.std(cnts)
    avg = np.mean(cnts)
    _min = np.min(cnts)
    _max = np.max(cnts)
    freq = ''
    if (_max - _min) < 5 : # 相差在五個以內
        if _max == _min :
            freq = f'{{{_min}}}'
        else :
            freq = f'{{{_min},{_max}}}'
    else :
        if _max == _min == 1 : # 有一個
            freq = '?'
        elif _min == 0 and _max != 0: # 0 ~ 任意
            freq = '*'
        elif _max == _min == 0 : # 沒東西
            freq = ''
        else :  # 有一個以上
            freq = '+'
    return freq

# 輸出 Regex
def format_regex(subsequences, subsequence):
    regex = ''
    for i in range(len(subsequences[0])) :
        tmp = ''
        cnts = np.array([len(seq[i]) for seq in subsequences])
        targets = [seq[i] for seq in subsequences]
        if i%2 == 0 or tmp == '.': # 不一定的
            tmp = '.*'
            if sum(cnts) == 0 or regex[-2:] == '.*' or regex[-2:] == '.+':
                tmp = ''
        else :
            tmp = regex_table[subsequence[i//2]]
            if tmp in ['e'] : # 跟 value 有關的
                tmp = formatting[tmp](targets)
            else : # 跟 Rule 有關的
                tmp += freq_counter(cnts)
        regex += tmp
    return regex

# 全部搞在一起
def parser(column, gene):

    p_column = encoder(column, gene)
    f_columns = type_counter(p_column)
    type_list = [''.join(map(str, [idx for idx, count in col])) for col in f_columns]
    subsequence = lcs(type_list)
    
    # 轉換完後，如果各位沒有共同的子序列，這段沒有比較的意義，直接退出
    if subsequence == '' :
        return '.*'

    seq_count = []
    for ff in f_columns :
        targets, cnt = find_most_sequence(ff, subsequence)
        l_count = []
        cnt = 0
        for i in range(1, len(ff)+1) :
            if i in targets :
                l_count.append(cnt)
                l_count.append(ff[i-1][1])
                cnt = 0
            else :
                cnt += ff[i-1][1]
        seq_count.append(l_count)
    
    strs = []
    for str_idx, seq_c in enumerate(seq_count) :
        idx = 0
        tmp = [] 
        for cnt in seq_c:
            tmp.append(column[str_idx][idx:idx+cnt])
            idx += cnt
        tmp.append(column[str_idx][idx:])
        strs.append(tmp)
    
    return format_regex(strs, subsequence)




if __name__ == "__main__":

    # column = ['mjzjod/assign/view.php?id=852596', 'dcspc/?p=9812372', 'mowwwd/assign/view.php?id=851596']
    column = ['zznew', 'tw', 'kkab']
    
    order   = [0,1,2,3,4,5,6,0xb,0xe]
    random.shuffle(order) 

    p_column = encoder(column,order)

    f_columns = type_counter(p_column)
    type_list = [''.join(map(str, [idx for idx, count in col])) for col in f_columns]
    subsequence = lcs(type_list)

    seq_count = []
    for ff in f_columns :
        targets, cnt = find_most_sequence(ff, subsequence)
        l_count = []
        cnt = 0
        for i in range(1, len(ff)+1) :
            if i in targets :
                l_count.append(cnt)
                l_count.append(ff[i-1][1])
                cnt = 0
            else :
                cnt += ff[i-1][1]
        seq_count.append(l_count)
    
    strs = []
    for str_idx, seq_c in enumerate(seq_count) :
        idx = 0
        tmp = [] 
        for cnt in seq_c:
            tmp.append(column[str_idx][idx:idx+cnt])
            idx += cnt
        tmp.append(column[str_idx][idx:])
        strs.append(tmp)
    
    print(format_regex(strs, subsequence))

    # .*[0-9a-f]{1,2}.*[0-9a-f]{1,1}.*\d{6,7}

