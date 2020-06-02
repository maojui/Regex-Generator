import string
from itertools import permutations
from maker import parser
from utils import common_string

def cs_filter(cs_set) :
    """
    cs_set 是所有字串共有的 substring，
    從 cs_set 中拿出需要的有交集的人之中比較長 (>平均值) 的那幾個當作固定點
    """
    # 列出可能有用的 set 
    cs_set = sorted(cs_set, key=lambda x: -len(x))
    prob = set([cs_set[0]])
    for cs in cs_set:
        for p in prob :
            if cs in p :
                break
        else :
            prob.add(cs)
            continue

    avg = round((sum(map(len,prob))/len(prob))) #? 怪怪

    def rule(x):
        return len(x) >= avg

    return filter(rule ,prob)

def split_str(strings_set, filtered_set) :
    """
    filtered_set 是選過適合當固定點的人
    把已知的部分切出來，分區塊處理
    """
    
    # 列出這些固定 substring 所有排列方式
    filtered_permutation = []
    for i in range(1,len(filtered_set)+1) :
        filtered_permutation.extend(list(permutations(filtered_set, i)))

    print("PERMUTATION: ", filtered_permutation)
    # 嘗試各種排列方式
    splited_result = {}
    for cutter_point in filtered_permutation:
        _pass = []
        for target in strings_set:
            res = []
            for idx, ss in enumerate(cutter_point) :
                tmp = target.partition(ss)
                res.append(tmp[0])
                if tmp[1] == '' :
                    break
                res.append(filtered_set.index(ss))
                target = tmp[2]
            else :
                res.append(target) # 把尾巴加回來
                _pass.append(res)
        else :
            # 砍掉有人不符合的排列方式
            if len(_pass) == len(strings_set) :
                used = sorted(cutter_point, key=lambda x: filtered_set.index(x))
                splited_result[' & '.join(used)] = _pass
            
    return splited_result

def generalizer(arr, filtered_set, gene) :
    target = []
    for i in range(len(arr[0])) :
        print()
        column = [val[i] for val in arr]
        
        print("COLUMN: ", column)
        if i == 0 and len(''.join(column)) == 0 :
            target.append(['^'])
            print("SAVE  :  ['^']", )

        
        elif type(column[0]) == int :
            target.append([filtered_set[column[0]]])
            print(f"SAVE  :  ['{filtered_set[column[0]]}']")


        elif i == len(arr[0])-1 and len(''.join(column)) == 0 :
            target.append(['$'])
            print("SAVE  :  ['$']")

        
        else : 
            
            print(column, gene)
            possible = parser(column, gene)
            print("Generalize  \t: ", possible)
        
        print()

    return target
    

def fitness() :
    # regex 長度 (-) 
    # or 數量
    # 單純度 (.*) ENTROPY
    # 基因分層分數
    # 覆蓋率 (可 generalize 度)
    # Negative
    pass

if __name__ == "__main__":
        
    # target = ['ASHIT', 'ASH1P', 'ASHRIMP', "BSHIP"]

    # target = ['ASHIPEA', 'ASH1PEB', 'ASHRIMPEC', "BSHIPED", "PEBSHI_SHI"]

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
    for i,s in enumerate(filtered_set) :
        print(f"\t{i} = {s}")
    print()
    print("Split by set\t\t: ")
    sr = split_str(target, filtered_set)
    for k,v in sr.items():
        print(f"\t{k}")
        for arr in v :
            print(f"\t\t{arr} ")
        g_res = generalizer(v, filtered_set)
        print('Generalize Result:')
        print('\t', g_res)


