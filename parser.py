import re
from const import *
from maker import parser
from evalute import *
from utils import common_string, cs_compress
from itertools import permutations

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
    cs_permutation = []
    for i in range(len(filtered_set), 0, -1):
        cs_permutation.extend(list(permutations(filtered_set, i)))

    # 嘗試各種排列方式
    for per in cs_permutation :
        _const = None
        reg = f"({'|'.join(per)})"
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
        print("---NOTHING FIXED STRING TO SPLIT---")
        return strings_set

def generalizer(arr, filtered_set, gene, positive=[], negative=[]):
    target = []
    value = 0
    for i in range(len(arr[0])):
        column = [val[i] for val in arr]

        # 如果大家開頭都沒東西
        if i == 0 and len(''.join(column)) == 0:
            target.append('^')

        # 如果那列是有對應的 Common string
        elif type(column[0]) == int:
            s = ''
            for c in list(filtered_set[column[0]]):
                if c in ESCAPE:
                    s += "\\" + c
                else:
                    s += c
            target.append(s)

        # 如果大家在最後面都沒東西
        elif i == len(arr[0])-1 and len(''.join(column)) == 0:
            target.append('$')

        # 其他區塊，另外 Parse，這裡要放基因
        else:
            possible, seq = parser(column, gene)
            # print('COLUMN', column)
            # print('POSSIBLE', possible)
            seq = fitness(possible, seq, positive, negative)
            target.append(possible)
            # print(column, "->", possible)
            value += seq
        
        print(target)

    return target, value


if __name__ == "__main__":

    import random
    target = ['ASHIPEA', 'ASH1PEB', 'ASHRIMPEC', "BSHIPED", "PEBSHI_SHI"]

    gene = [0, 1, 2, 3, 4, 5, 6, 11, 0xe]
    random.shuffle(gene)

    cs_set = common_string(target)
    # ['PE', 'SH', 'S', 'E', 'H', 'P']
    cs_set = list(cs_compress(cs_set))
    # ['PE', 'SH']
    print("\nCommon string set : \n\t", list(cs_set))


    filtered_set = list(cs_filter(cs_set))
    print("\nFilter set : ")
    for i, s in enumerate(filtered_set):
        print(f"\t{i} = {s}")

    split_str = split_fixed(target, filtered_set)
    print("\nSplit by set : ")
    for i in range(len(filtered_set)):
        print(f"\t{target[i]} -> {split_str[i]}")

    g_res, fitness = generalizer(split_str, filtered_set, gene, target)
    
    print('Generalize Result:')
    print('\t', ''.join(g_res))
    print('fitness:', fitness)
