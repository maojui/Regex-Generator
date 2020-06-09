import random
import string
from const import *
import numpy as np
from utils import longest_common_subseqence as lcs

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

def alpha(process, string):
    for idx,c in enumerate(string):
        if process[idx] == None and c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ" :
            process[idx] = '3'
    return process

def upper_hexdigit(process, string):
    for idx,c in enumerate(string):
        if process[idx] == None and c in "0123456789ABCDEF" :
            process[idx] = '4'
    return process

def lower_hexdigit(process, string):
    for idx,c in enumerate(string):
        if process[idx] == None and c in "0123456789abcdef" :
            process[idx] = '5'
    return process

WORD = string.ascii_letters + string.digits + '_'
def words(process, string):
    for idx,c in enumerate(string):
        if process[idx] == None and c in WORD :
            process[idx] = '6'
    return process

SPACE = '\x0c\n\r\t\x0b\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u200a\u2028\u2029\u202f\u205f\u3000\ufeff'
def space(process, string):
    for idx,c in enumerate(string):
        if process[idx] == None and c in SPACE :
            process[idx] = '7'
    return process

def space_only(process, string):
    for idx,c in enumerate(string):
        if process[idx] == None and c == ' ' :
            process[idx] = '8'
    return process

def anything(process, string) :
    for idx in range(len(process)) :
        if process[idx] == None:
            process[idx] = '9'
    return process

def escape(process, string) :
    for idx,c in enumerate(string):
        if process[idx] == None and c in ESCAPE:
            process[idx] = 'a'
    return process

def symbol(process, string) :
    for idx,c in enumerate(string):
        if process[idx] == None and c in SYMBOL:
            process[idx] = 'b'
    return process


def char_range(process, string) :
    raise NotImplementedError("Nothing Here.")
    return process


def char_or(process, string) :
    for idx in range(len(process)) :
        if process[idx] == None:
            process[idx] = 'd'
    return process

def string_or(process, string) :
    for idx in range(len(process)) :
        if process[idx] == None:
            process[idx] = 'e'
    return process

def char_string_or(process, string) :
    for idx in range(len(process)) :
        if process[idx] == None:
            process[idx] = 'f'
    return process

__gene = {
    # 跟 Rule 有關的
    0x0   : numbers,             #  [0-9]           numbers
    0x1   : upper_alpha,         #  [A-Z]           upper alpha
    0x2   : lower_alpha,         #  [a-z]           lower alpha
    0x3   : alpha,               #  [A-Za-z]        alpha
    0x4   : upper_hexdigit,      #  [0-9A-F]        upper hexdigits
    0x5   : lower_hexdigit,      #  [0-9a-f]        lower hexdigits
    0x6   : words,               #  \w              words
    0x7   : space,               #  \s              space like
    0x8   : space_only,          #  [ ]             space only 
    0x9   : anything,            #  .               anything

    # 跟 value 有關的
    0xa   : escape,              #  [{}^$.|*+?]    escape
    0xb   : symbol,              #  [SYMBOLS]      symbol 
    0xc   : char_range,          #  [?-?^?]        range                
    0xd   : char_or,             #  [???]          char or              
    0xe   : string_or,           #  (??|???|?)     string or            
    0xf   : char_string_or,      #  ([???]|[???])  char & string or 
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

def find_sequence(seq, target, cur=[], inc=0, idx=0) :
    cur = []
    ctr = 0
    start = 0
    t_idx = 0
    while t_idx < len(target) :
        for i in range(start, len(seq)) :
            if seq[i][0] == target[t_idx] :
                t_idx += 1
                ctr += seq[i][1]
                cur.append(i+1)
                start = i + 1
                break
                
    return cur, ctr
    pass

# 算 rule 的次數
def freq_counter(cnts) :
    std = np.std(cnts)
    avg = np.mean(cnts)
    _min = np.min(cnts)
    _max = np.max(cnts)
    freq = ''
    if _min == 0 and _max == 1 : # 只有一個
        freq = '?'
    elif _max == _min == 1 : # 只有一個
        freq = ''
    elif _max == _min == 0 : # 沒東西
        freq = ''
    elif (_max - _min) < 5 : # 相差在五個以內
        if _max == _min :
            freq = f'{{{_min}}}'
        else :
            freq = f'{{{_min},{_max}}}'
    elif _min == 0 and _max > 1: # 0 ~ 任意
        freq = '*'
    else :  # 有一個以上
        freq = '+'
    return freq



def space_only_format(strs, cnts):
    cnt = freq_counter(cnts)
    if len(cnt) != 0 :
        return f"[ ]{cnt}"
    return ' '

def escape_format(strs, cnts):
    return f"[{''.join(sorted(set(''.join(strs))))}]" + freq_counter(cnts)

def symbol_format(strs, cnts):
    return f"[{''.join(sorted(set(''.join(strs))))}]" + freq_counter(cnts)

def char_range_format(strs, cnts):
    raise NotImplementedError("XD")

def char_or_format(strs, cnts):
    return f"[{''.join(sorted(set(''.join(strs))))}]" + freq_counter(cnts)

def char_string_or_format(strs, cnts):
    ss = []
    for s in strs :
        ss.append(f"[{''.join(sorted(set(s)))}]")
    return f"({'|'.join(set(ss))})" + freq_counter(cnts)

def string_or_format(strs, cnts):
    setstr = set(strs)
    if len(setstr) > 1 :
        return f"({'|'.join(setstr)})"
    elif len(setstr) == 1 :
        return list(setstr)[0]
    return ''

regex_table = {
    # 跟 Rule 有關的
    '0' : '\d',
    '1' : '[A-Z]', 
    '2' : '[a-z]', 
    '3' : '[A-Za-z]', 
    '4' : '[0-9A-F]', 
    '5' : '[0-9a-f]', 
    '6' :  '\w',
    '7' :  '\s',
    '9' :  '.',
    # 跟 value 有關的
    '8' :  '8',
    'a' :  'a',
    'b' :  'b',
    'c' :  'c',
    'd' :  'd',
    'e' :  'e',
    'f' :  'f',
}


# 處理 value
formatting = {
    '8': space_only_format,
    'a': escape_format,
    'b': symbol_format,
    'c': char_range_format,
    'd': char_or_format,
    'e': string_or_format,
    'f': char_string_or_format,
}

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
            typ = regex_table[subsequence[i//2]]
            if typ in '8abcdef' : # 跟 value 有關的
                tmp = formatting[typ](targets, cnts)
            else : # 跟 Rule 有關的
                tmp = typ
                tmp += freq_counter(cnts)
        regex += tmp
    return regex

# 全部搞在一起
def parser(column, gene):

    t_column = encoder(column, gene)
    f_columns = type_counter(t_column)
    type_list = [''.join(map(str, [idx for idx, count in col])) for col in f_columns]
    subsequence = lcs(type_list)
    
    # 轉換完後，如果各位沒有共同的子序列，這段沒有比較的意義，直接退出
    if subsequence == '' :
        return '.*'

    seq_count = []
    for ff in f_columns :
        if len(subsequence) < 10 :
            targets, cnt = find_most_sequence(ff, subsequence)
        else :
            targets, cnt = find_sequence(ff, subsequence)
        l_count = []
        cnt = 0
        for i in range(1, len(ff)+1) :
            if i in targets :
                if ff[i-1][0] != '9':
                    l_count.append(cnt)
                    l_count.append(ff[i-1][1])
                else : 
                    # 如果也是 any 就合併進去
                    l_count.append(0)
                    l_count.append(ff[i-1][1] + cnt)
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
    
    return format_regex(strs, subsequence), subsequence

if __name__ == "__main__":

    # column = ['mjzjod/assign/view.php?id=852596', 'dcspc/?p=9812372', 'mowwwd/assign/view.php?id=851596']
    column = ['zznew', 'tw', 'kkab']
    
    order   = [0,1,2,3,4,5,6,7,8,9,0xa,0xb,0xd,0xe,0xf]
    random.shuffle(order) 

    t_column = encoder(column,order)

    f_columns = type_counter(t_column)
    type_list = [''.join(map(str, [idx for idx, count in col])) for col in f_columns]
    subsequence = lcs(type_list)

    seq_count = []
    for ff in f_columns :
        if len(subsequence) < 10 :
            targets, cnt = find_most_sequence(ff, subsequence)
        else :
            targets, cnt = find_sequence(ff, subsequence)
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

