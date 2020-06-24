
import os
import base64
import random
import string
from generator import generator

testset = {
    0 :[
        'c:\\windows\\temp\\radffdc7.tmp\\kctzrdpurmfr.exe',
        'c:\\windows\\temp\\radffdc9.tmp\\ixplkcrudfbuo.exe',
        'c:\\windows\\temp\\radffdca.tmp\\ksyphabjmouoerd.exe'
    ],
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

print("\nTarget :\n\t", end='')
print('\n\t'.join(target), end='\n\n')

result = []

TEST = False

if TEST :

    gene = [0x12,0x9]
    g_res, fitness = parser(target, gene)
    result.append((fitness, ''.join(g_res)))

else :
    result = generator(target, POPULATION, GENERATION)

for fit, regex in  sorted( set(result),key=lambda x : -x[0] )[:20]:
    print(f'{fit}\t\t{regex}')