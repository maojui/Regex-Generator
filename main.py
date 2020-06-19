
import os
import base64
import random
from parser import *
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
GENERATION = 20

DEBUG = True
WARNING = '\033[93m'
NOCOLOR = '\033[0m'

print()
print("Target :")
for t in target:
    print('\t', t)
print()

MAX_FITNESS = -1e9
BEST_GENE = None
BEST_REGEX = ""

result = []

TEST = False

if TEST :

    # gene = random.sample(range(0,0xf), 15)
    gene = [0x12,0x9]
    g_res, fitness = parser(target, gene)
    result.append((fitness, ''.join(g_res)))

else :

    GG = 1
    pop = [random.sample(range(0,0x15), 0x15) for _ in range(POPULATION)] 
    # pop = [[0,5,2,9] for _ in range(POPULATION)] 
    while GG <= GENERATION:
        
        print(f"{GG} Generation :")
        generation = []

        for idx, gene in enumerate(pop):
            g_res, fitness = parser(target, gene)
            debug_print(f"{idx}", gene)
            result.append((fitness, ''.join(g_res)))
            generation.append((fitness, ''.join(g_res)))
            if fitness > MAX_FITNESS:
                MAX_FITNESS = fitness
                BEST_GENE = gene
                BEST_REGEX = ''.join(g_res)

        print("AVG Fitness :",sum([g[0] for g in generation])/len(generation))
        total = sum([g[0] for g in generation])
        prob = [g[0]/total for g in generation]
        print("BEST REGEX :", BEST_REGEX)

        offspring = []
        for _ in range(POPULATION//2):
            p1, p2 = random.choices(pop, weights=prob, k=2)
            
            # clean mutation
            c1 = [ p& 0x7f for p in p1] 
            c2 = [ p& 0x7f for p in p2]
            
            if random.randint(0,100) < 30 : 
                o1 = crossover(c1, c2)
                for i in range(len(p1)) :
                    idx1 = o1.index(p1[i]& 0x7f)
                    o1[idx1] = p1[i]
            else :
                o1 = p1
            
            if random.randint(0,100) < 30 : 
                o2 = crossover(c2, c1)
                for i in range(len(p1)) :
                    idx2 = o2.index(p2[i]& 0x7f)
                    o2[idx2] = p2[i]
            else :
                o2 = p2
                
            if random.randint(0,100) < 5 : 
                o1 = mutation(o1)
            if random.randint(0,100) < 7 : 
                o2 = mutation(o2)
            
            offspring.append(o1)
            offspring.append(o2)

        pop = offspring
        GG += 1


for fit, regex in  sorted( set(result),key=lambda x : -x[0] )[:20]:
    print(f'{fit}\t\t{regex}')

# print(f"\t{MAX_FITNESS} : {BEST_REGEX}")