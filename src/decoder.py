import random
import types
from .const import *
from .genetic import encoder
from .formatter import *
from .utils import longest_common_subseqence as lcs

__all__ = ['transform_column']

regex_table = {
    INDEX_TABLE(0x00) : '\\d',
    INDEX_TABLE(0x01) : '[A-Z]',
    INDEX_TABLE(0x02) : '[a-z]',
    INDEX_TABLE(0x03) : '[A-Za-z]',
    INDEX_TABLE(0x04) : '[0-9A-F]',
    INDEX_TABLE(0x05) : '[0-9a-f]',
    INDEX_TABLE(0x06) : '\\w',
    INDEX_TABLE(0x07) : '\\s',
    INDEX_TABLE(0x08) : space_only_format,
    INDEX_TABLE(0x09) : '.',
    INDEX_TABLE(0x0a) : char_or_format,
    INDEX_TABLE(0x0b) : char_or_format,
    INDEX_TABLE(0x0c) : char_range_format,
    INDEX_TABLE(0x0d) : char_range_format,
    INDEX_TABLE(0x0e) : string_or_format,
    INDEX_TABLE(0x0f) : char_range_format,
    INDEX_TABLE(0x10) : col_char_range_format,
    INDEX_TABLE(0x11) : col_char_range_format,
    INDEX_TABLE(0x12) : col_char_range_format,
    INDEX_TABLE(0x13) : col_char_range_format,
    INDEX_TABLE(0x14) : col_char_range_format,
}

def find_sequence(seq, target):

    # 從後面找，找出 Upper bound，確保 sequence 可以完整找完
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
        selectable = list(filter(lambda x: ub > x[1] > lb, selectable))
        # best = sorted(selectable, key=lambda x: -x[0])[0]
        # lb = best[1]
        lb = random.choice(selectable)[1]
        output.append(lb)

    return output

def decoder(subsequences, subsequence):
    """
    輸出 Regex
    """
    regex = ''
    tmp = ''
    for i in range(len(subsequences[0])):
        cnts = [len(seq[i]) for seq in subsequences]
        targets = [seq[i] for seq in subsequences]
        if i % 2 == 0 :  # 不一定的
            if len(set(targets)) > 3 or random.randint(0,99) % 2 == 1 : # 有很多不一樣
                _next = '.*'
            elif len(''.join(set(targets))) == 1 : # 只有幾個不一樣
                _next = char_range_format(targets, cnts)
            else:
                setstr = set()
                for ss in targets:
                    if ss == '' : continue
                    setstr.add(escape_format(ss, False))
                _next = f"({'|'.join(setstr)})"
                if '' in targets :
                    _next += '?'
            if sum(cnts) == 0 or (_next.startswith('.') and tmp.startswith('.')):
                tmp = ''
            else :
                tmp = _next
        else:
            typ = regex_table[chr(ord(subsequence[i//2]) & 0x7f)]
            if type(typ) == types.FunctionType :
                tmp = typ(targets, cnts)
            else : 
                tmp = typ
                tmp += freq_counter(cnts)
        regex += tmp
    return regex

def transform_column(column, gene):
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
        return '.*', INDEX_TABLE(9)
    seq_count = []
    for ff in f_columns:
        targets = find_sequence(ff, subsequence)
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

    return decoder(strs, subsequence), subsequence
