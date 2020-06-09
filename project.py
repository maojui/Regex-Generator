
import random
from parser import *
from maker import *

DEBUG = False

# target = ['ASHIT', 'ASH1P', 'ASHRIMP', "BSHIP"]

target = ['ASHIPEA', 'ASH1PEB', 'ASHRIMPEC', "BSHIPED", "PEBSHI_SHI"]

target = [
#     'https://blog.csdn.net/vitaminc4/article/details/78922612', 
#     'https://transbiz.com.tw/regex-regular-expression-ga-%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%A4%BA%E5%BC%8F/', 
#     'https://AAQQ.nctu.edu.tw/mod/assign/view.php?id=85596',
#     'https://erqwjeoiqe.nctu.edu.tw/dcspc/?p=3438', 
#     'https://tw.nctu.edu.tw/mjzjod/assign/view.php?id=85596', 
    'https://kakbb.nctu.edu.tw/dcspc/?p=9872',
    'https://e3new.nctu.edu.tw/mowwwd/assign/view.php?id=85596', 
    'https://aadmm.nctu.edu.tw/ggmood',
]

# target = [
#     'maojui0427@gmail.com',
#     'maojui0437@gmail.com',
#     'maojui0447@gmail.com',
#     'j6e1n1n2y@gmail.com',
#     'a5180352@gmail.com',
#     'toregenerate@gmail.com'
# ]

import os
import base64
# target = [ base64.b64encode(os.urandom(random.randint(i,64))).decode() for i in range(10)]
# target = [ base64.b64encode(os.urandom(64)).decode() for i in range(10)]

print()
print("Target : ")
for t in target :
    print('\t',t)

cs_set = common_string(target)

if DEBUG : 
    print()
    print("Common string set \t: ")
    print("\t", list(cs_set))       
    print()

filtered_set = list(cs_filter(cs_set))

if DEBUG : 
    print("Filter set \t\t: ")
    for i,s in enumerate(filtered_set) :
        print(f"\t{i} = {s}")
    print()

if DEBUG : 
    print("Split by set\t\t: ")
sr = split_fixed(target, filtered_set)
gene   = [0,1,2,3,4,5,6,7,8,9,0xa,0xb,0xd,0xe,0xf]
random.shuffle(gene)
# gene = [0,5, 9 ,1,2,3,4,5,6,7,8] 


for k,v in sr.items():
    
    if DEBUG :
        print(f"\t{k}")
        for arr in v :
            print(f"\t\t{arr} ")
        print()

    g_res, fitness = generalizer(v, filtered_set, gene)
    
    print()
    print('Generalize Result:')
    print('\t', ''.join(g_res))
    print()
    print('fitness:', fitness)

