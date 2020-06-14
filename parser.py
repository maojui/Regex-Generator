import string
from const import *
from maker import parser
from evalute import *
from utils import common_string
from itertools import permutations


def cs_filter(cs_set):
    """
    `cs_set` 是所有字串共有的 substring 的集合。\\
    從 `cs_set` 中拿出有交集的部分，再把比較長 (>平均值) 的那幾個當作固定點

    For example: `['ht', 'htt', 'http', 'https', 'abcde'] -> ['https', 'abcde']`
    """
    # 列出可能有用的 set
    cs_set = filter(lambda x: len(x) > 5, cs_set)
    cs_set = sorted(cs_set, key=lambda x: -len(x))

    if len(cs_set) > 0:
        prob = [cs_set[0]]
        for cs in cs_set:
            for p in prob:
                if cs in p:
                    break
            else:
                prob.append(cs)
                continue

        avg = round((sum(map(len, prob))/len(prob)))  # ? 怪怪

        def rule(x):
            return len(x) >= avg or len(x) > 5
        return filter(rule, prob)
    else:
        return []


def split_fixed(strings_set, filtered_set):
    """
    `filtered_set` 是選過適合當固定點的人。\\
    把已知的部分切出來，分區塊處理
    """

    # 列出這些固定 substring 所有排列方式
    filtered_permutation = []
    for i in range(len(filtered_set), 0, -1):
        filtered_permutation.extend(list(permutations(filtered_set, i)))

    # 嘗試各種排列方式
    splited_result = {}
    for cutter_point in filtered_permutation:
        _pass = []
        for target in strings_set:
            res = []
            for idx, ss in enumerate(cutter_point):
                tmp = target.partition(ss)
                res.append(tmp[0])
                if tmp[1] == '':
                    break
                res.append(filtered_set.index(ss))
                target = tmp[2]
            else:
                res.append(target)  # 把尾巴加回來
                _pass.append(res)
        else:
            # 砍掉有人不符合的排列方式
            if len(_pass) == len(strings_set):
                used = cutter_point
                splited_result[' & '.join(used)] = _pass
                return splited_result
    return {None: [[s] for s in strings_set]}


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

    return target, value


if __name__ == "__main__":

    import random
    # target = ['ASHIT', 'ASH1P', 'ASHRIMP', "BSHIP"]

    # target = ['ASHIPEA', 'ASH1PEB', 'ASHRIMPEC', "BSHIPED", "PEBSHI_SHI"]

    gene = [0, 1, 2, 3, 4, 5, 6, 11, 0xe]
    random.shuffle(gene)

    target = [
        # 'https://blog.csdn.net/vitaminc4/article/details/78922612',
        # 'https://transbiz.com.tw/regex-regular-expression-ga-%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%A4%BA%E5%BC%8F/',
        # 'https://AAQQ.nctu.edu.tw/mod/assign/view.php?id=85596',
        # 'https://erqwjeoiqe.nctu.edu.tw/dcspc/?p=3438',
        'https://tw.xxx.zzds.nctu.edu.tw/mjzjod/assign/view.php?id=85596',
        'https://kkab.nctu.edu.tw/dcspc/?p=9872',
        'https://e3new.nctu.edu.tw/mowwwd/assign/view.php?id=85596',
        'https://aadm.nctu.edu.tw/ggmood',
    ]

    cs_set = common_string(target)
    print("Common string set \t: ")
    print("\t", list(cs_set))
    # ['PE', 'SH', 'S', 'E', 'H', 'P']

    print()
    print("Filter set \t\t: ")
    filtered_set = list(cs_filter(cs_set))
    for i, s in enumerate(filtered_set):
        print(f"\t{i} = {s}")
    print()
    print("Split by set\t\t: ")
    sf = split_fixed(target, filtered_set)
    print(sf)
    for k, v in sf.items():
        print(f"\t{k}")
        for arr in v:
            print(f"\t\t{arr} ")
        g_res, fitness = generalizer(v, filtered_set, gene, target)
        print(g_res)
        print('Generalize Result:')
        print('\t', ''.join(g_res))
        print('fitness:', fitness)
