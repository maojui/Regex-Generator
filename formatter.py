from const import *
import numpy as np 
import random

def type_counter(columns):
    """
    化簡，算數量。
    [['e', 'e', 'e', 'e', 'e'], ['e', 'e'], ['e', 'e', 'e', 'e']] 
    => [[('e', 5)], [('e', 2)], [('e', 4)]]
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

def col_char_range_format(strs, cnts):
    reg = ''
    for i in range(max(cnts)) :
        col = []
        col_cnt = []
        for idx, s in enumerate(strs) :
            col.append(s[i:i+1])
            col_cnt.append(len(s[i:i+1]))
        reg += char_or_format(col, col_cnt)
    return reg

def or_format(output, frequency, rangestr='') :
    if len(output) > 1 or rangestr != '':
        return f"[{rangestr + escape_format(output,True)}]" + frequency
    else :
        return escape_format(output,False) + frequency

def escape_format(strs, inside) :
    tmp = ''
    for c in strs :
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
    setstr = set()
    for ss in strs:
        if ss == '' : continue
        setstr.add(escape_format(ss, False))
    if len(setstr) > 1:
        return f"({'|'.join(setstr)})"
    elif len(setstr) == 1:
        return list(setstr)[0]
    return ''

