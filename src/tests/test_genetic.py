import types
import random
import unittest
from ..genetic import *


class GeneticMethod(unittest.TestCase):

    def getRandomTarget(self, strings):
        return [''.join(random.sample(strings, k=random.randint(0,len(strings)))) for i in range(random.randint(10,30))]

    def isNone(self, obj) :
        return [elements for elements in obj if None in elements]

    # 把比較短的、或已存在的共通字串篩掉
    def test_encoder_number(self):
        # digit
        target = self.getRandomTarget('0123456789')
        self.assertEqual(self.isNone(encoder(target,[0])), [])
        # upper_hexdigit
        target = self.getRandomTarget('0123456789ABCDEF')
        self.assertEqual(self.isNone(encoder(target,[4])), [])
        # lower_hexdigit
        target = self.getRandomTarget('0123456789abcdef')
        self.assertEqual(self.isNone(encoder(target,[5])), [])
        
    def test_encoder_alpha(self):
        # 0x1 : upper_alpha
        target = self.getRandomTarget(string.ascii_uppercase)
        self.assertEqual(self.isNone(encoder(target,[1])), [])
        # 0x2 : lower_alpha
        target = self.getRandomTarget(string.ascii_lowercase)
        self.assertEqual(self.isNone(encoder(target,[2])), [])
        # 0x3 : alpha
        target = self.getRandomTarget(string.ascii_letters)
        self.assertEqual(self.isNone(encoder(target,[3])), [])
        # 0x6 : words
        target = self.getRandomTarget(WORD)
        self.assertEqual(self.isNone(encoder(target,[6])), [])
        # 0xc : char_range
        target = self.getRandomTarget(CHAR_RANGE)
        self.assertEqual(self.isNone(encoder(target,[0xc])), [])
        # 0xd : char_range_letter
        target = self.getRandomTarget(CHAR_RANGE_WITH_SYMBOLS)
        self.assertEqual(self.isNone(encoder(target,[0xd])), [])
        
    def test_encoder_symbols(self):
        # 0x7 : space
        target = self.getRandomTarget(SPACE)
        self.assertEqual(self.isNone(encoder(target,[7])), [])
        # 0x8 : space_only
        target = self.getRandomTarget(' ')
        self.assertEqual(self.isNone(encoder(target,[8])), [])
        # 0xa : escape
        target = self.getRandomTarget(ESCAPE)
        self.assertEqual(self.isNone(encoder(target,[0xa])), [])
        # 0xb : symbol
        target = self.getRandomTarget(SYMBOL)
        self.assertEqual(self.isNone(encoder(target,[0xb])), [])

    def test_encoder_anything(self) :
        # 0x9 : anything
        target = self.getRandomTarget(string.printable)
        self.assertEqual(self.isNone(encoder(target,[0x9])), [])
        # 0xe : char_or
        target = self.getRandomTarget(string.printable)
        self.assertEqual(self.isNone(encoder(target,[0xe])), [])
        # 0xf : string_or
        target = self.getRandomTarget(string.printable)
        self.assertEqual(self.isNone(encoder(target,[0xf])), [])

if __name__ == '__main__':
    unittest.main()
