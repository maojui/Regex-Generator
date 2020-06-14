
import base64
import os
import random
from parser import *
from maker import *
from genetic import crossover, mutation

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

# target = ['kakbb', 'e3new','aadmm']
target = [    
    "https://kakbb.nctu.edu.tw/dcspc/?p=9872",
    "https://e3new.nctu.edu.tw/mowwwd/assign/view.php?id=85596",
    "https://aadmm.nctu.edu.tw/ggmood",
]
# target = ['ASH1P', 'ASH1P', 'ASHR1P', "BSH1P"]
# target = ['ASHIPEA', 'ASH1PEB', 'ASHRIMPEC', "BSHIPED", "PEBSHI_SHI"]

# target = [
#     # 'https://blog.csdn.net/vitaminc4/article/details/78922612',
#     'https://aadmm.nctu.edu.tw/ggmood',
#     'https://kakbb.nctu.edu.tw/dcspc/?p=9872',
#     'https://erqwjeoiqe.nctu.edu.tw/dcspc/?p=3438',
#     'https://AAQQ.nctu.edu.tw/mod/assign/view.php?id=85596',
#     'https://tw.nctu.edu.tw/mjzjod/assign/view.php?id=85596',
#     'https://e3new.nctu.edu.tw/mowwwd/assign/view.php?id=85596'
# ]

# target = [
#     'maojui0427@gmail.com',
#     'maojui0437@gmail.com',
#     'maojui0447@gmail.com',
#     # 'j6e1n1n2y@gmail.com',
#     # 'a5180352@gmail.com',
#     # 'toregenerate@gmail.com'
# ]

# target = [base64.b64encode(os.urandom(random.randint(i, 64))).decode() for i in range(10)]
# target = [base64.b64encode(os.urandom(64)).decode() for i in range(10)]

# Register code 
# target = []
# for i in range(30) :
#     a = ''.join(random.sample(string.ascii_lowercase[3:] + string.digits, k=5))
#     b = ''.join(random.sample(string.ascii_lowercase + string.digits, k=18))
#     c = ''.join(random.sample(string.ascii_lowercase + string.digits, k=7))
#     target.append('-'.join([a,b,c]))

# IP Address
# target = []
# for i in range(30) :
#     a = str(random.randint(0,256))
#     b = str(random.randint(0,256))
#     c = str(random.randint(0,256))
#     d = str(random.randint(0,256))
#     target.append('.'.join([a,b,c,d]))

# Hex color 
# target = []
# for i in range(30) :
#     if i % 3 == 0 :
#         target.append('#' + ''.join([hex(random.randint(0,16))[2:] for i in range(3)]).upper())
#     target.append( ''.join([hex(random.randint(0,256))[2:].rjust(2,'0') for i in range(3)]).upper())

print()
print("Target :")
for t in target:
    print('\t', t)
print()

# Preprocess
cs_set = common_string(target)
filtered_set = list(cs_filter(cs_set))
sr = split_fixed(target, filtered_set)

debug_print("common_string", cs_set)
debug_print("cs_filter", filtered_set)
debug_print("split_fixed", sr)

MAX_FITNESS = -1e9
BEST_GENE = None
BEST_REGEX = ""

result = []
for val in sr.values():
    
    pop = [random.sample([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 15)for _ in range(POPULATION)]
    i = 1

    while i <= GENERATION:

        print(f"{i} Generation :")
        for idx, gene in enumerate(pop):
            g_res, fitness = generalizer(val, filtered_set, gene)
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