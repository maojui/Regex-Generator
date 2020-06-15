import unittest
from parser import cs_filter

class ParserMethod(unittest.TestCase):

    # 把比較短的、或已存在的共通字串篩掉
    def test_cs_filter(self):
        commons = {'SH', 'PE', 'S', 'E', 'H', 'P'}
        self.assertEqual(sorted(list(cs_filter(commons))), ['PE', 'SH'])

if __name__ == '__main__':
    unittest.main()
