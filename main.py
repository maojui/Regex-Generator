
import base64
import os
import random
from parser import *
from maker import *
from genetic import crossover, mutation

testset = {
    1 :['kakbb', 'e3new','aadmm'],
    2 :['ASH1P', 'ASH1P', 'ASHR1P', "BSH1P"],
    3 :['ASHIPEA', 'ASH1PEB', 'ASHRIMPEC', "BSHIPED", "PEBSHI_SHI"],
    4 :[
        "https://kakbb.nctu.edu.tw/dcspc/?p=9872",
        "https://e3new.nctu.edu.tw/mowwwd/assign/view.php?id=85596",
        "https://aadmm.nctu.edu.tw/ggmood",
    ],
    5 :[
        'https://aadmm.nctu.edu.tw/ggmood',
        'https://kakbb.nctu.edu.tw/dcspc/?p=9872',
        'https://erqwjeoiqe.nctu.edu.tw/dcspc/?p=3438',
        'https://AAQQ.nctu.edu.tw/mod/assign/view.php?id=85596',
        'https://tw.nctu.edu.tw/mjzjod/assign/view.php?id=85596',
        'https://e3new.nctu.edu.tw/mowwwd/assign/view.php?id=85596'
    ],
    6 :[
        'https://aadmm.nctu.edu.tw/ggmood',
        'https://kakbb.nctu.edu.tw/dcspc/?p=9872',
        'https://blog.csdn.net/vitaminc4/article/details/78922612',
        'https://AAQQ.nctu.edu.tw/mod/assign/view.php?id=85596',
        'https://tw.nctu.edu.tw/mjzjod/assign/view.php?id=85596',
        'https://e3new.nctu.edu.tw/mowwwd/assign/view.php?id=85596'
    ],
    7 :['maojui0427@gmail.com','maojui0437@gmail.com','maojui0447@gmail.com'],
    8 :['maojui0427@gmail.com','j6e1n1n2y@gmail.com','a5180352@gmail.com','toregenerate@gmail.com'],
    9 :[base64.b64encode(os.urandom(random.randint(10, 64))).decode() for i in range(10)],
    10 :[base64.b64encode(os.urandom(64)).decode() for i in range(10)],
    11 : [ '-'.join([
                ''.join(random.sample(string.ascii_lowercase[3:] + string.digits, k=5)),
                ''.join(random.sample(string.ascii_lowercase + string.digits, k=18)),
                ''.join(random.sample(string.ascii_lowercase + string.digits, k=7))]) for i in range(30)],
    12 : ['.'.join([str(random.randint(0,256)),str(random.randint(0,256)),str(random.randint(0,256)),str(random.randint(0,256))]) for i in range(30)],
    13 : ['#'+ ''.join([hex(random.randint(0,256))[2:].rjust(2,'0') for i in range(3)]).upper() for k in range(30)],
    14 : ['#' + ''.join([hex(random.randint(0,15))[2:] for i in range(3)]).upper() for k in range(30)]
}

import sys
target = testset[int(sys.argv[1])]

POPULATION = 100
GENERATION = 3

DEBUG = True
WARNING = '\033[93m'
NOCOLOR = '\033[0m'
def debug_print(title: str, obj) -> bool:
    if DEBUG:
        print(f"[{WARNING}DEBUG{NOCOLOR}]", title, ":")
        print(obj)
        print()
    return DEBUG

TARGET = 13
print()
print("Target :")
for t in target:
    print('\t', t)
print()

# Preprocess
cs_set = common_string(target)
cs_set = cs_compress(cs_set)
filtered_set = list(cs_filter(cs_set))
split_str = split_fixed(target, filtered_set)

debug_print("common_string", cs_set)
debug_print("cs_filter", filtered_set)
debug_print("split_fixed", split_str)

MAX_FITNESS = -1e9
BEST_GENE = None
BEST_REGEX = ""

result = []
TEST = False
if TEST :

    gene = [15,9]
    g_res, fitness = generalizer(split_str, filtered_set, gene)
    result.append((fitness, ''.join(g_res)))


else :

    i = 1
    pop = [random.sample([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 16)for _ in range(POPULATION)]
    while i <= GENERATION:

        print(f"{i} Generation :")
        for idx, gene in enumerate(pop):
            g_res, fitness = generalizer(split_str, filtered_set, gene)
            debug_print(f"{idx}", gene)
            result.append((fitness, ''.join(g_res)))
            if fitness > MAX_FITNESS:
                MAX_FITNESS = fitness
                BEST_GENE = gene
                BEST_REGEX = ''.join(g_res)

        pop = []
        mutate_best = mutation(BEST_GENE)
        for _ in range(POPULATION):
            pop.append(crossover(BEST_GENE, mutate_best))
        i += 1


for fit, regex in  sorted( set(result),key=lambda x : -x[0] ):
    print(f'{fit}\t\t{regex}')

print(len(set(result)))
# print(f"\t{MAX_FITNESS} : {BEST_REGEX}")