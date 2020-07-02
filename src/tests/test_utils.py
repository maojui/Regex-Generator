import unittest
from ..utils import cs_compress, common_string, escape_format
from ..utils import _longest_common_subseqence as _lcs, longest_common_subseqence as lcs

class UtilsMethod(unittest.TestCase):

    # 找出出現在所有人身上的 substring
    def test_common_string(self):
        common_str = common_string(
            ['ASHIPEA', 'ASH1PEB', 'ASHRIMPEC', "BSHIPED", "PEBSHI_SHI"])
        self.assertEqual(common_str, {'PE', 'SH', 'S', 'E', 'H', 'P'})

    # 找出最長的重複序列
    def test_lcs(self):
        self.assertEqual(_lcs('121513', '1253'), '1253')
        self.assertEqual(
            lcs(['121012038513', '125213231', '1212253123']), '121231')
        pass

    # 把比較短的、或已存在的共通字串篩掉
    def test_cs_compress(self):
        commons = {'SH', 'PE', 'S', 'E', 'H', 'P'}
        self.assertEqual(sorted(list(cs_compress(commons))), ['PE', 'SH'])
    
    def test_escape_format(self):
        self.assertEqual(escape_format('c:\\windows'), 'c:\\\\windows')


if __name__ == '__main__':
    unittest.main()