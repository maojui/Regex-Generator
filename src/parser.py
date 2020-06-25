import re
import random
from const import *
from evalute import *
from decoder import transform_column
from utils import escape
from utils import common_string, cs_compress, debug_print
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
        cs_combination.extend(list(combinations(filtered_set, i)))
    random.shuffle(cs_combination)
    # 嘗試各種排列方式
    for per in cs_combination :
        _const = None
        reg = str(f"({'|'.join([escape(p) for p in per])})")
        reg = reg.replace('\\','\\\\')
        output_set = []
        for ss in strings_set :
            const = '&&&&&&&&&&&'.join([find.group() for find in re.finditer(reg, ss)])
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

def parser(targets, gene, positive=[], negative=[]):
    output = []
    value = 0
    arr, filtered_set = preprocessor(targets)
    for i in range(len(arr[0])):
        column = [val[i] for val in arr]

        # 如果大家開頭都沒東西
        if i == 0 and len(''.join(column)) == 0:
            output.append('^')

        # 如果那列是有對應的 Common string
        elif type(column[0]) == int:
            output.append(escape(filtered_set[column[0]]))

        # 如果大家在最後面都沒東西
        elif i == len(arr[0])-1 and len(''.join(column)) == 0:
            output.append('$')

        # 其他區塊，另外 Parse，這裡要放基因
        else:
            possible, seq = transform_column(column, gene)
            seq = fitness(possible, seq, positive, negative)
            output.append(possible)
            value += seq

    return output, value

if __name__ == "__main__":

    import random
    output = ['ASHIAAA', 'ASH1PGB', 'ASHRIMPDC', "BSHIKED"]
    gene = [0x11, 9]
    # random.shuffle(gene)
    split_str, filtered_set = preprocessor(output)
    g_res, fitness = parser(split_str, filtered_set, gene, output)
    print('\nGeneralize Result:')
    print('\t', ''.join(g_res))
    print('fitness:', fitness)