import random
import string
from const import *
import numpy as np
from utils import longest_common_subseqence as lcs

__all__ = ['parser']


def numbers(process, string):
    for idx, c in enumerate(string):
        if process[idx] == None and c in "'1234567890":
            process[idx] = '0'
    return process


def upper_alpha(process, string):
    for idx, c in enumerate(string):
        if process[idx] == None and c in "ABCDEFGHIJKLMNOPWRSTUVWXYZ":
            process[idx] = '1'
    return process


def lower_alpha(process, string):
    for idx, c in enumerate(string):
        if process[idx] == None and c in "abcdefghijklmnopqrstuvwxyz":
            process[idx] = '2'
    return process


def alpha(process, string):
    for idx, c in enumerate(string):
        if process[idx] == None and c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ":
            process[idx] = '3'
    return process


def upper_hexdigit(process, string):
    for idx, c in enumerate(string):
        if process[idx] == None and c in "0123456789ABCDEF":
            process[idx] = '4'
    return process


def lower_hexdigit(process, string):
    for idx, c in enumerate(string):
        if process[idx] == None and c in "0123456789abcdef":
            process[idx] = '5'
    return process


WORD = string.ascii_letters + string.digits + '_'


def words(process, string):
    for idx, c in enumerate(string):
        if process[idx] == None and c in WORD:
            process[idx] = '6'
    return process


SPACE = '\x0c\n\r\t\x0b\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u200a\u2028\u2029\u202f\u205f\u3000\ufeff'


def space(process, string):
    for idx, c in enumerate(string):
        if process[idx] == None and c in SPACE:
            process[idx] = '7'
    return process


def space_only(process, string):
    for idx, c in enumerate(string):
        if process[idx] == None and c == ' ':
            process[idx] = '8'
    return process


def anything(process, string):
    for idx in range(len(process)):
        if process[idx] == None:
            process[idx] = '9'
    return process


def escape(process, string):
    for idx, c in enumerate(string):
        if process[idx] == None and c in ESCAPE:
            process[idx] = 'a'
    return process


def symbol(process, string):
    for idx, c in enumerate(string):
        if process[idx] == None and c in SYMBOL:
            process[idx] = 'b'
    return process


def char_range(process, string):
    data_set = WORD[:-1]+SYMBOL+ESCAPE
    for idx, c in enumerate(string):
        if process[idx] == None and c in data_set:
            process[idx] = 'c'
    return process


def char_or(process, string):
    for idx in range(len(process)):
        if process[idx] == None:
            process[idx] = 'd'
    return process


def string_or(process, string):
    for idx in range(len(process)):
        if process[idx] == None:
            process[idx] = 'e'
    return process

def char_range_letter(process, string):
    data_set = WORD[:-1]
    for idx, c in enumerate(string):
        if process[idx] == None and c in data_set:
            process[idx] = 'c'
    return process

__gene = {
    # 跟 Rule 有關的
    0x0: numbers,           # \d           numbers
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
    0xd: char_or,           # [???]          char or
    0xe: string_or,         # (??|???|?)     string or
    0xf: char_range_letter,    # [?-??-?]       range for only A-Z a-z 0-9
}


def encoder(columns, order):
    """
    把字串重新歸類，照 __gene dictionary 做事。
    ABC -> 5 5 5
    """
    output = []
    process = [[None] * len(c) for c in columns]
    for idx, c in enumerate(columns):
        for i in order:
            process[idx] = __gene[i](process[idx], c)
    return process


def type_counter(columns):
    """
    化簡，算數量。
    [['e', 'e', 'e', 'e', 'e'], ['e', 'e'], ['e', 'e', 'e', 'e']] -> [[('e', 5)], [('e', 2)], [('e', 4)]]
    """
    output = []
    for column in columns:
        out = []
        cur = None
        count = 0
        for i in column:
            if i != cur:
                out.append((cur, count)) if cur != None else None
                cur = i
                count = 0
            count += 1
        out.append((cur, count)) if cur != None else None
        output.append(out)
    return output


def freq_counter(cnts):
    """
    算 rule 的次數
    """
    std = np.std(cnts)
    avg = np.mean(cnts)
    _min = np.min(cnts)
    _max = np.max(cnts)
    freq = ''
    if _min == 0 and _max == 1:  # 只有一個
        freq = '?'
    elif _max == _min == 1:  # 只有一個
        freq = ''
    elif _max == _min == 0:  # 沒東西
        freq = ''
    elif (_max - _min) < 5:  # 相差在五個以內
        if _max == _min:
            freq = f'{{{_min}}}'
        else:
            freq = f'{{{_min},{_max}}}'
    elif _min == 0 and _max > 1:  # 0 ~ 任意
        freq = '*'
    else:  # 有一個以上
        freq = '+'
    return freq


def space_only_format(strs, cnts):
    cnt = freq_counter(cnts)
    if len(cnt) != 0:
        return f"[ ]{cnt}"
    return ' '


def char_range_format(strs, cnts):

    def getRange(elements, distribute) :
        output = ''
        _min, _max = None, None
        for element in elements :
            if element in distribute :
                idx = distribute.find(element)
                if _min == None or idx < _min : _min = idx
                if _max == None or idx > _max : _max = idx
        if _min != None and _max != None:
            if _min == _max : 
                output += distribute[_min]
            else :
                output += f'{distribute[_min]}-{distribute[_max]}'
        return output
    
    output = ''
    symbols = ''
    elements = set(''.join(strs))
    output += getRange(elements, string.ascii_lowercase)
    output += getRange(elements, string.ascii_uppercase)
    output += getRange(elements, string.digits)
    
    for e in elements:
        if e in SYMBOL :
            symbols += e
    if '-' in output:
        return or_format(symbols, freq_counter(cnts), output)
    else :
        return or_format(output + symbols, freq_counter(cnts))
        

def or_format(output, frequency, rangestr='') :
    if len(output) > 1 or rangestr != '':
        return f"[{rangestr + escape_format(output,True)}]" + frequency
    else :
        return escape_format(output,False) + frequency

def escape_format(str, inside) :
    tmp = ''
    for c in str :
        if inside and c in INESCAPE:
            tmp += '\\' + c
        elif not inside and c in ESCAPE :
            tmp += '\\' + c
        else :
            tmp += c
    return tmp

def char_or_format(strs, cnts):
    output = ''.join(sorted(set(''.join(strs))))
    return or_format(output, freq_counter(cnts))

def string_or_format(strs, cnts):
    setstr = set(strs)
    if len(setstr) > 1:
        return f"({'|'.join(setstr)})"
    elif len(setstr) == 1:
        return list(setstr)[0]
    return ''


regex_table = {
    # 跟 Rule 有關的
    '0': '\d',
    '1': '[A-Z]',
    '2': '[a-z]',
    '3': '[A-Za-z]',
    '4': '[0-9A-F]',
    '5': '[0-9a-f]',
    '6': '\w',
    '7': '\s',
    '9': '.',
    # 跟 value 有關的
    '8': '8',
    'a': 'a',
    'b': 'b',
    'c': 'c',
    'd': 'd',
    'e': 'e',
    'f': 'f',
}


# 處理 value
formatting = {
    '8': space_only_format,
    'a': char_or_format,
    'b': char_or_format,
    'c': char_range_format,
    'd': char_or_format,
    'e': string_or_format,
    'f': char_range_format,
}


def format_regex(subsequences, subsequence):
    """
    輸出 Regex
    """
    regex = ''
    tmp = ''
    for i in range(len(subsequences[0])):
        cnts = np.array([len(seq[i]) for seq in subsequences])
        targets = [seq[i] for seq in subsequences]
        if i % 2 == 0 :  # 不一定的
            if len(set(targets)) > 3 or random.randint(0,99) % 2 == 1 : # 有很多不一樣
                _next = '.*'
            elif len(''.join(set(targets))) == 1 : # 只有幾個不一樣
                _next = char_range_format(targets, cnts)
            else:
                _next = f"({'|'.join([t for t in set(targets) if t!= ''])})"
                if '' in targets :
                    _next += '?'
            if sum(cnts) == 0 or (_next.startswith('.') and tmp.startswith('.')):
                tmp = ''
            else :
                tmp = _next
            print("REGEX",tmp)
        else:
            typ = regex_table[subsequence[i//2]]
            if typ in '8abcdef':  # 跟 value 有關的
                tmp = formatting[typ](targets, cnts)
            else:  # 跟 Rule 有關的
                tmp = typ
                tmp += freq_counter(cnts)
        regex += tmp
    return regex


def find_remain(seq, target, cur=[], inc=0, idx=0):
    cur = []
    t_idx = 0
    start = 0
    while t_idx < len(target):
        for i in range(start, len(seq)):
            if seq[i][0] == target[t_idx]:
                t_idx += 1
                cur.append(i+1)
                start = i + 1
                break
    return start


def find_good_sequence(seq, target):
    obj = {}
    for idx, s in enumerate(seq):
        sym = s[0]
        if not sym in obj:
            obj[sym] = []
        obj[sym].append((s[1], idx))
    output = []

    lb = -1  # lower bound
    for i in range(len(target)):
        sym = target[i]
        ub = len(seq) - find_remain(seq[::-1], target[i+1:][::-1])
        selectable = obj[sym]
        # print("BOUND",lb,'~',ub)
        selectable = list(filter(lambda x: ub > x[1] > lb, selectable))
        best = sorted(selectable, key=lambda x: -x[0])[0]
        lb = best[1]
        output.append(lb)

    return output


def parser(column, gene):
    """
    全部搞在一起
    """
    t_column = encoder(column, gene)
    f_columns = type_counter(t_column)
    type_list = [''.join(map(str, [idx for idx, count in col]))
                 for col in f_columns]
    subsequence = lcs(type_list)

    # 轉換完後，如果各位沒有共同的子序列，這段沒有比較的意義，直接退出
    if subsequence == '':
        return '.*', '9'

    seq_count = []
    for ff in f_columns:
        targets = find_good_sequence(ff, subsequence)
        l_count = []
        cnt = 0
        for i in range(0, len(ff)):
            if i in targets:
                if ff[i][0] != '9':
                    l_count.append(cnt)
                    l_count.append(ff[i][1])
                else:
                    # 如果也是 any 就合併進去
                    l_count.append(0)
                    l_count.append(ff[i][1] + cnt)
                cnt = 0
            else:
                cnt += ff[i][1]
        seq_count.append(l_count)
    
    strs = []
    for str_idx, seq_c in enumerate(seq_count):
        idx = 0
        tmp = []
        for cnt in seq_c:
            tmp.append(column[str_idx][idx:idx+cnt])
            idx += cnt
        tmp.append(column[str_idx][idx:])
        strs.append(tmp)

    return format_regex(strs, subsequence), subsequence


if __name__ == "__main__":

    import base64
    import random
    import os

    column = [base64.b64encode(os.urandom(
        random.randint(i, 60))).decode() for i in range(10)]
    # column = ['mjzjod/assign/view.php?id=852596', 'dcspc/?p=9812372', 'mowwwd/assign/view.php?id=851596']
    # column = ['zzne\'w', '$tw', 'k^kab', 'ZZZZ', '0123']

    order = [0xc, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0xa, 0xb, 0xd, 0xe, 0xf]
    # random.shuffle(order)

    t_column = encoder(column, order)

    f_columns = type_counter(t_column)
    type_list = [''.join(map(str, [idx for idx, count in col]))
                 for col in f_columns]
    subsequence = lcs(type_list)

    print(f_columns)
    print(subsequence)
    import time

    seq_count = []
    a = time.time()

    for ff in f_columns:
        targets = find_good_sequence(ff, subsequence)
        l_count = []
        cnt = 0
        for i in range(0, len(ff)):
            if i in targets:
                if ff[i][0] != '9':
                    l_count.append(cnt)
                    l_count.append(ff[i][1])
                else:
                    # 如果也是 any 就合併進去
                    l_count.append(0)
                    l_count.append(ff[i][1] + cnt)
                cnt = 0
            else:
                cnt += ff[i][1]
        seq_count.append(l_count)

    print("seqcount:", len(seq_count[0]))
    print(seq_count)
    b = time.time()
    print("Find Sequence :", b - a)

    strs = []
    for str_idx, seq_c in enumerate(seq_count):
        idx = 0
        tmp = []
        for cnt in seq_c:
            tmp.append(column[str_idx][idx:idx+cnt])
            idx += cnt
        tmp.append(column[str_idx][idx:])
        strs.append(tmp)

    c = time.time()
    print("Transform :", c - b)
    print(format_regex(strs, subsequence))
    d = time.time()
    print("Format :", d - c)

    # .*[0-9a-f]{1,2}.*[0-9a-f]{1,1}.*\d{6,7}