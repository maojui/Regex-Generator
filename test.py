import unittest

from utils import common_string, _longest_common_subseqence as _lcs,longest_common_subseqence as lcs
from maker import find_most_sequence
from parser import cs_filter

class UtilsMethod(unittest.TestCase):

    # 找出出現在所有人身上的 substring
    def test_common_string(self):
        common_str = common_string(['ASHIPEA', 'ASH1PEB', 'ASHRIMPEC', "BSHIPED", "PEBSHI_SHI"])
        self.assertEqual(common_str, {'PE', 'SH', 'S', 'E', 'H', 'P'}) 

    # 找出最長的重複序列
    def test_lcs(self):
        self.assertEqual( _lcs('121513', '1253'), '1253')
        self.assertEqual( lcs(['121012038513', '125213231','1212253123']), '121231')
        pass
    
class MakerMethod(unittest.TestCase) :
    
    def test_find_most_sequence(self):
        sequence = '424b2b4'
        ff = [  ('2', 5), ('4', 1), ('b', 1),
                ('4', 3),
                ('2', 5),  ('b', 1),  ('2', 2),
                ('4', 1),  ('2', 1),
                ('b', 1),
                ('2', 3),
                ('b', 9), ('2', 1), ('4', 1), ('b', 1),
                ('4', 5)]
        self.assertEqual(find_most_sequence(ff, sequence)[1], 27)
        
class ParserMethod(unittest.TestCase) :
    
    # 把比較短的、或已存在的共通字串篩掉
    def test_cs_filter(self):
        commons = {'SH', 'PE', 'S', 'E', 'H', 'P'}
        self.assertEqual(sorted(list(cs_filter(commons))), ['PE','SH']) 

if __name__ == '__main__':
    unittest.main()