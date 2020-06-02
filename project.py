import random
from parser import *
from maker import *


# target = ['ASHIT', 'ASH1P', 'ASHRIMP', "BSHIP"]

target = ['ASHIPEA', 'ASH1PEB', 'ASHRIMPEC', "BSHIPED", "PEBSHI_SHI"]

# target = [
#     # 'https://blog.csdn.net/vitaminc4/article/details/78922612', 
#     # 'https://transbiz.com.tw/regex-regular-expression-ga-%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%A4%BA%E5%BC%8F/', 
#     # 'https://AAQQ.nctu.edu.tw/mod/assign/view.php?id=85596',
#     # 'https://erqwjeoiqe.nctu.edu.tw/dcspc/?p=3438', 
#     'https://tw.xxx.zzds.nctu.edu.tw/mjzjod/assign/view.php?id=85596', 
#     'https://kkab.nctu.edu.tw/dcspc/?p=9872',
#     'https://e3new.nctu.edu.tw/mowwwd/assign/view.php?id=85596', 
#     'https://aadm.nctu.edu.tw/ggmood',
# ]

cs_set = common_string(target)
# print("Common string set \t: ")
# print("\t", list(cs_set))       
# ['PE', 'SH', 'S', 'E', 'H', 'P']


# print()
# print("Filter set \t\t: ")
filtered_set = list(cs_filter(cs_set))
# for i,s in enumerate(filtered_set) :
#     print(f"\t{i} = {s}")
#  0 = SH
print()
print("Split by set\t\t: ")
sr = split_str(target, filtered_set)
gene   = [0,1,2,3,4,5,6,11,0xe]
random.shuffle(gene) 

for k,v in sr.items():
    print(f"\t{k}")
    for arr in v :
        print(f"\t\t{arr} ")

    g_res = generalizer(v, filtered_set, gene)
    print('Generalize Result:')
    print('\t', g_res)


