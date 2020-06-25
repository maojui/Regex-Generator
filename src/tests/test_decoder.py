import unittest
from ..decoder import find_sequence

class MakerMethod(unittest.TestCase):

    def test_find_sequence(self):
        sequence = '424b2b4'
        ff = [('2', 5), ('4', 1), ('b', 1),('4', 3),('2', 5), ('b', 1), ('2', 2),('4', 1), 
              ('2', 1),('b', 1),('2', 3),('b', 9), ('2', 1), ('4', 1), ('b', 1),('4', 5)]
        count = ''.join([ff[idx][0] for idx in find_sequence(ff, sequence)])
        self.assertEqual(count, sequence) 

if __name__ == '__main__':
    unittest.main()
