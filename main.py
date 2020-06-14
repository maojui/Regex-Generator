
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


# target = ['ASHIT', 'ASH1P', 'ASHRIMP', "BSHIP"]
target = ['ASHIPEA', 'ASH1PEB', 'ASHRIMPEC', "BSHIPED", "PEBSHI_SHI"]

target = [
    # 'https://blog.csdn.net/vitaminc4/article/details/78922612',
    # 'https://aadmm.nctu.edu.tw/ggmood',
    'https://kakbb.nctu.edu.tw/dcspc/?p=9872',
    'https://erqwjeoiqe.nctu.edu.tw/dcspc/?p=3438',
    'https://AAQQ.nctu.edu.tw/mod/assign/view.php?id=85596',
    'https://tw.nctu.edu.tw/mjzjod/assign/view.php?id=85596',
    'https://e3new.nctu.edu.tw/mowwwd/assign/view.php?id=85596'
]

# target = [
#     'maojui0427@gmail.com',
#     'maojui0437@gmail.com',
#     'maojui0447@gmail.com',
#     'j6e1n1n2y@gmail.com',
#     'a5180352@gmail.com',
#     'toregenerate@gmail.com'
# ]

# target = [base64.b64encode(os.urandom(random.randint(i, 64))).decode() for i in range(10)]
# target = [base64.b64encode(os.urandom(64)).decode() for i in range(10)]

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

MAX_FITNESS = 0
BEST_GENE = None

for val in sr.values():
    pop = [random.sample(range(16), 16) for _ in range(POPULATION)]
    i = 1

    while i <= GENERATION:
        print(f"{i} Generation :")
        for idx, gene in enumerate(pop):
            g_res, fitness = generalizer(val, filtered_set, gene)
            # debug_print(f"{idx}", gene)
            # debug_print(f"{fitness}", ''.join(g_res))
            if fitness > MAX_FITNESS:
                MAX_FITNESS = fitness
                BEST_GENE = gene
                print(f"\t{fitness} : {''.join(g_res)}")

        pop = []
        mutate_best = mutation(BEST_GENE)
        for _ in range(POPULATION):
            pop.append(crossover(BEST_GENE, mutate_best))
        i += 1
