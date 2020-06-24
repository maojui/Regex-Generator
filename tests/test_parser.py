import unittest
from parser import cs_filter, split_fixed

class ParserMethod(unittest.TestCase):
    
    def test_cs_filter(self):
        test1 = ['1','2','3','4','5','6','7','8','ab','cd','ef']
        self.assertEqual(cs_filter(test1), set(['ab','cd','ef'])) 
        test2 = ['ab','cd','ef']
        self.assertEqual(cs_filter(test2), set(['ab','cd','ef'])) 
    
    # This feature is random now
    # def test_split_fixed(self):
    #     target = ['ASHIAAA']
    #     self.assertEqual(split_fixed(target, ['SH']), [['A', 0, 'IAAA']])
    #     target = ['https://abc','https://defabc']
    #     self.assertEqual(split_fixed(target, ['abc','https://']), [['', 1, '', 0, ''],['', 1, 'def', 0, '']])

if __name__ == '__main__':
    unittest.main()
