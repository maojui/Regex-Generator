import re

score_table = {
    '0': 9,
    '1': 26,
    '2': 26,
    '3': 52,
    '4': 16,
    '5': 16,
    '6': 60,
    '7': 5,
    '8': 1,
    '9': 100,
    'a': 5,
    'b': 5,
    'c': 30,
    'd': 10,
    'e': 40,
    'f': 10,
}

def fitness(regex, seq, target, negative=[]) :
    
    # init
    score = 50

    # 可以 Match
    for t in target :
        if not re.search(regex, t) :
            print(regex,t)
            return -1000
    
    # 不可以 Matche
    for t in negative :
        if re.search(regex, t) :
            return -1000
    
    # regex 長度 (-)
    score -= len(regex)
    # or 數量
    if '|' in regex :
        score += 10
        score -= regex.count('|')

    # 基因分層分數
    for g in set(seq) :
        score -= score_table[g]
    
    # 單純度 (.*) ENTROPY
    score -= 10 * len(set(seq))

    # 覆蓋率 (可 generalize 度)
    print("??")
    return score

if __name__ == "__main__":
    
    target = [
        'https://blog.csdn.net/vitaminc4/article/details/78922612', 
        'https://transbiz.com.tw/regex-regular-expression-ga-%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%A4%BA%E5%BC%8F/', 
        'https://AAQQ.nctu.edu.tw/mod/assign/view.php?id=85596',
        'https://erqwjeoiqe.nctu.edu.tw/dcspc/?p=3438', 
        'https://tw.nctu.edu.tw/mjzjod/assign/view.php?id=85596', 
        'https://kkab.nctu.edu.tw/dcspc/?p=9872',
        'https://e3new.nctu.edu.tw/mowwwd/assign/view.php?id=85596', 
        'https://aadm.nctu.edu.tw/ggmood',
    ]

    regexs = [
        ('^https://.*[0-9a-f]{1,3}.*(u.tw/mowww|u.tw/mjzjo|om.tw/r|u.tw/mo|tu.|m.n|log.|rqwj).*[0-9a-f]{1,2}(t/vit|xpr|tu.|u.tw/|ssign/vi).*[0-9a-f]{1,2}(rti|u.tw/ggmoo|w.php?i|u.tw/|ssion-g|sp).*[0-9a-f]{1,2}.*','5e5e5e5'),
        ('^https://.*[A-Za-z]+.*.[A-Za-z]{3,6}.*.[A-Za-z]+.*.[A-Za-z]+.*.{1,2}.*[A-Za-z]+.*','393939393'),
        ('^https://([./2789=?abcdeknpstuw]|[./348=?cdeijnopqrstuw]|[%-./1345678ABCDEFabcegilmnoprstuwxz]|[./5689=?acdeghijmnopstuvwz]|[./acdegmnotuw]|[./35689=?acdeghimnopstuvw]|[./5689=?AQacdeghimnopstuvw]|[./1246789abcdegilmnorstv])+', 'f'),
        ('^https://.+', '9')
    ]
    for r in regexs:
        print(fitness(r[0], r[1], target))


