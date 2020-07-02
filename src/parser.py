import re
import random
import hashlib
from .const import *
from .evalute import *
from .decoder import transform_column
from .utils import escape_format
from .utils import common_string, cs_compress, debug_print
from itertools import combinations

def cs_filter(cs_set):
    length = 1
    while True :
        cs_set = set(filter(lambda x : len(x) >= length, cs_set))
        if len(cs_set) < 10 :
            break
        length += 1
    return cs_set

def split_fixed(strings_set, filtered_set):
    """
    `filtered_set` 是選過適合當固定點的人。\\
    把已知的部分切出來，分區塊處理
    """
    # 列出這些固定 substring 所有排列方式
    cs_combination = []
    for i in range(len(filtered_set), 0, -1):
        _next_combination = list(combinations(filtered_set, i))
        random.shuffle(_next_combination)
        cs_combination.extend(_next_combination)

    # 嘗試各種排列方式
    for per in cs_combination :
        _const = None
        reg = str(f"({'|'.join([escape_format(p) for p in per])})")
        output_set = []
        for ss in strings_set :
            const = '&'.join([ hashlib.md5(find.group().encode()).hexdigest() for find in re.finditer(reg, ss)])
            if _const == None :
                _const = const # init
            if _const != None and const != _const :
                break

            # 把找到的固定點取代成 Index
            tmp = re.split(reg, ss)
            output = []
            for s in tmp :
                if s in per :
                    output.append(filtered_set.index(s))
                else :
                    output.append(s)
            output_set.append(output)
        else :
            return output_set
    else :
        debug_print("---NO FIXED STRING TO SPLIT---", [])
        return [ [strs] for strs in strings_set]

def preprocessor(target):

    cs_set = common_string(target)
    cs_set = cs_compress(cs_set)
    filtered_set = list(cs_filter(cs_set))
    split_str = split_fixed(target, filtered_set)
    # if DEBUG:
    debug_print("common_string", cs_set)
    debug_print("cs_filter", filtered_set)
    debug_print("split_fixed", split_str)

    return split_str, filtered_set

def parser(arr, filtered_set, gene, positive=[], negative=[]):
    output = []
    value = 0
    for i in range(len(arr[0])):
        column = [val[i] for val in arr]

        # 如果大家開頭都沒東西
        if i == 0 and len(''.join(column)) == 0:
            output.append('^')

        # 如果大家在最後面都沒東西
        elif i == len(arr[0])-1 and len(''.join(column)) == 0:
            output.append('$')

        # 如果那列是有對應的 Common string
        elif type(column[0]) == int:
            value += 500
            output.append(escape_format(filtered_set[column[0]]))

        # 其他區塊，另外 Parse，這裡要放基因
        else:
            possible, seq = transform_column(column, gene)
            seq = fitness(possible, seq, positive, negative)
            output.append(possible)
            value += seq
    # print(output)
    return output, value
