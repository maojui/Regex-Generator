from .const import DEBUG, ESCAPE, INESCAPE

def debug_print(title: str, obj) -> bool:
    if DEBUG:
        print(f"[{WARNING}DEBUG{NOCOLOR}]", title, ":")
        print(obj)
        print()
    return DEBUG

def common_string(strings):
    """
    Find all common substring of `strings` by DP.
    """
    cs_set = None
    strings = sorted(strings, key=lambda x: len(x))
    if len(strings) > 1:
        for T in strings[1:]:
            tmp_set = set()
            # DP table
            counter = [[0] * (len(T) + 1) for x in range(len(strings[0]) + 1)]
            for i in range(len(strings[0])):
                for j in range(len(T)):
                    if strings[0][i] == T[j]:
                        c = counter[i][j] + 1
                        counter[i + 1][j + 1] = c
                        for cc in range(c):
                            tmp_set.add(strings[0][i - cc:i + 1])
            if cs_set == None:
                cs_set = tmp_set
            cs_set = cs_set.intersection(tmp_set)
        return cs_set
    else:
        return strings

def cs_compress(cs_set):
    """
    @cs_set 是所有字串共有的 substring 的集合。
    從 @cs_set 中拿出有交集的部分
    For example: ['ht', 'htt', 'http', 'https', 'abcde'] -> ['https', 'abcde']
    """
    # 列出可能有用的 set
    cs_set = sorted(cs_set, key=lambda x: -len(x))
    prob = []
    if len(cs_set) > 0:
        prob = [cs_set[0]]
        for cs in cs_set:
            for p in prob:
                if cs in p:
                    break
            else:
                prob.append(cs)
                continue
    return set(prob)

def _longest_common_subseqence(s1, s2):
    if s1 == '' or s2 == '':
        return ''
    matrix = [["" for x in range(len(s2))] for x in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = s1[i]
                else:
                    matrix[i][j] = matrix[i - 1][j - 1] + s1[i]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1], key=len)
    cs = matrix[-1][-1]
    return cs

def longest_common_subseqence(type_list):
    subsequence = type_list[0]
    for t in type_list[1:]:
        subsequence = _longest_common_subseqence(subsequence, t)
    return subsequence

def escape_format(strs, inside=False) :
    tmp = ''
    for c in strs :
        if inside and c in INESCAPE:
            tmp += '\\' + c
        elif not inside and c in ESCAPE :
            tmp += '\\' + c
        else :
            tmp += c
    return tmp
