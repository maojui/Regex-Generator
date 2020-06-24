
import os
import base64
import random
import string
from generator import generator

testset = {
    0 :[
        'c:\windows\temp\radfe995.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfe996.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfe99b.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfe99f.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfe9ae.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfe9b1.tmp\tmmotbzcj.exe',
        'c:\windows\temp\radfe9b3.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfe9b4.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfe9b5.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfe9ba.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfe9bd.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfe9be.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfe9be.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfe9c1.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfe9d5.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfe9e1.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfe9e3.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfe9e9.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfe9eb.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfe9f2.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfe9ff.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfea12.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfea18.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfea1e.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfea25.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfea29.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfea2e.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfea2f.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfea32.tmp\tmmotbzcj.exe',
        'c:\windows\temp\radfea33.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfea34.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfea38.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfea46.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfea4d.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfea51.tmp\tmmotbzcj.exe',
        'c:\windows\temp\radfea54.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfea55.tmp\jxyjjgjymswfr.exe',
        'c:\windows\temp\radfea56.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfea5c.tmp\tmmotbzcj.exe',
        'c:\windows\temp\radfea5d.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfea62.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfea63.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfea64.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfea64.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfea65.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfea80.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfea85.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfea86.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfea8a.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfea91.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfea92.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfea94.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfea98.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfeab1.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfeab1.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfeabe.tmp\tmmotbzcj.exe',
        'c:\windows\temp\radfeaca.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfead5.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfeae7.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfeaef.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfeb01.tmp\jxyjjgjymswfr.exe',
        'c:\windows\temp\radfeb05.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfeb07.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfeb0c.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfeb0f.tmp\jxyjjgjymswfr.exe',
        'c:\windows\temp\radfeb0f.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfeb17.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfeb1a.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfeb1b.tmp\tmmotbzcj.exe',
        'c:\windows\temp\radfeb22.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfeb23.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfeb30.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfeb34.tmp\jxyjjgjymswfr.exe',
        'c:\windows\temp\radfeb34.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfeb3c.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfeb43.tmp\jxyjjgjymswfr.exe',
        'c:\windows\temp\radfeb5d.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfeb61.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfeb64.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfeb67.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfeb70.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfeb7b.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfeb7d.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfeb8a.tmp\tmmotbzcj.exe',
        'c:\windows\temp\radfeb8d.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfeb90.tmp\jxyjjgjymswfr.exe',
        'c:\windows\temp\radfeba1.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfeba9.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfebad.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfebb5.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfebc5.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfebc7.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfebca.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfebd5.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfebd6.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfebef.tmp\kctzrdpurmfr.exe',
        'c:\windows\temp\radfebef.tmp\tmmotbzcj.exe',
        'c:\windows\temp\radfebf2.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfebf9.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfebfb.tmp\tmmotbzcj.exe',
        'c:\windows\temp\radfebfd.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfebfe.tmp\jxyjjgjymswfr.exe',
        'c:\windows\temp\radfec15.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfec1a.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfec24.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfec28.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfec2f.tmp\mfwkxflgtauyn.exe',
        'c:\windows\temp\radfec33.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfec44.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfec47.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfec49.tmp\tmmotbzcj.exe',
        'c:\windows\temp\radfec4a.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfec53.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfec56.tmp\ixplkcrudfbuo.exe',
        'c:\windows\temp\radfec57.tmp\ksyphabjmouoerd.exe',
        'c:\windows\temp\radfec57.tmp\mfwkxflgtauyn.exe',
        'c:\\windows\\temp\\radffdc7.tmp\\kctzrdpurmfr.exe',
        'c:\\windows\\temp\\radffdc9.tmp\\ixplkcrudfbuo.exe',
        'c:\\windows\\temp\\radffdca.tmp\\ksyphabjmouoerd.exe',
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