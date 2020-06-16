# import string

# def encoder(element):
#     # Const list
#     IS_NUM          = 0b0000001  # 0-> Not Num(\D), 1-> Num(\d)
#     IS_BLANK        = 0b0000010
#     IS_LOWER_STRING = 0b0000100
#     IS_UPPER_STRING = 0b0001000
#     IS_WORD         = 0b0010000  # 0->

#     def test(element, mapping, const):
#         return const if element in mapping else 0

#     res = []
#     for e in element:
#         num = 0
#         num |= test(e, string.digits, IS_NUM)
#         num |= test(e, string.ascii_lowercase, IS_LOWER_STRING)
#         num |= test(e, string.ascii_uppercase, IS_UPPER_STRING)
#         num |= IS_WORD if num | IS_LOWER_STRING | IS_UPPER_STRING != 0 else 0
#         num |= test(e, BLANK, IS_BLANK)
#         num |= test(e, BLANK, IS_BLANK)

# 'A0ABC9' : [11000, 10001, 11000, 11000, 10001] -> \w{6}, .{6}, [A-Z]{6}



# boss = [[('0', 2), ('2', 1), ('0', 2), ('2', 1), ('0', 1), ('1', 1), ('2', 3), ('1', 2), ('2', 2), ('1', 1), ('2', 1), ('0', 1), ('2', 2), ('0', 2), ('2', 2), ('1', 4), ('2', 1), ('9', 1), ('1', 1), ('9', 1), ('1', 1), ('0', 1), ('1', 3), ('2', 1), ('0', 1), ('1', 2), ('0', 1), ('2', 2), ('1', 1), ('0', 1), ('1', 1), ('2', 2), ('0', 2), ('1', 1), ('2', 5), ('1', 2), ('2', 1), ('1', 1), ('0', 1), ('2', 3), ('1', 4), ('0', 1), ('9', 1), ('0', 1), ('6', 1), ('2', 2), ('1', 1), ('2', 2), ('1', 4), ('0', 1), ('2', 1), ('1', 2), ('2', 1), ('1', 1)], [('1', 4), ('2', 1), ('1', 1), ('2', 2), ('1', 3), ('0', 1), ('2', 2), ('1', 1), ('2', 1), ('0', 1), ('9', 1), ('1', 1), ('2', 1), ('1', 1), ('0', 1), ('2', 1), ('1', 3), ('2', 4), ('1', 3), ('0', 1), ('1', 1), ('0', 1), ('1', 1), ('2', 1), ('0', 1), ('1', 1), ('2', 1), ('0', 1), ('1', 1), ('2', 1), ('0', 1), ('2', 1), ('1', 1), ('0', 3), ('1', 1), ('2', 1), ('1', 1), ('0', 1), ('2', 1), ('1', 1), ('2', 3), ('1', 1), ('2', 1), ('1', 2), ('2', 1), ('0', 1), ('2', 2), ('0', 1), ('1', 1), ('2', 2), ('6', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 3), ('1', 1), ('0', 3), ('1', 2), ('0', 1), ('1', 1), ('2', 1), ('0', 2), ('2', 1), ('1', 1), ('2', 2), ('0', 1), ('9', 1)], [('2', 2), ('1', 6), ('2', 2), ('1', 5), ('2', 3), ('1', 1), ('0', 1), ('1', 1), ('9', 1), ('1', 1), ('0', 2), ('2', 1), ('6', 1), ('1', 1), ('2', 2), ('1', 2), ('0', 1), ('1', 2), ('2', 4), ('0', 1), ('2', 1), ('1', 1), ('0', 3), ('1', 1), ('6', 1), ('2', 1), ('0', 1), ('2', 3), ('1', 1), ('2', 1), ('9', 1), ('2', 1), ('1', 1), ('0', 1), ('2', 1), ('1', 1), ('2', 3), ('1', 2), ('2', 2), ('1', 1), ('0', 1), ('1', 2), ('0', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('6', 1), ('1', 1), ('2', 4), ('0', 1), ('2', 1), ('9', 1), ('1', 2), ('2', 1), ('9', 1)], [('2', 1), ('1', 1), ('2', 1), ('1', 3), ('2', 1), ('1', 1), ('2', 1), ('0', 1), ('2', 2), ('1', 1), ('2', 1), ('6', 1), ('0', 1), ('2', 1), ('1', 1), ('2', 2), ('1', 1), ('2', 1), ('1', 2), ('2', 2), ('0', 1), ('1', 1), ('6', 1), ('1', 2), ('2', 2), ('0', 1), ('1', 1), ('2', 1), ('1', 7), ('6', 1), ('2', 4), ('0', 2), ('1', 1), ('0', 1), ('1', 1), ('0', 1), ('6', 1), ('2', 1), ('1', 2), ('2', 3), ('0', 1), ('2', 2), ('0', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 2), ('1', 1), ('0', 1), ('2', 1), ('0', 1), ('1', 2), ('2', 3), ('1', 3), ('2', 1), ('0', 2), ('2', 1), ('9', 1), ('2', 1), ('1', 1), ('2', 2), ('1', 1), ('2', 3), ('0', 1), ('2', 1), ('1', 1), ('2', 3), ('9', 1)], [('1', 7), ('9', 1), ('2', 1), ('1', 1), ('0', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('0', 1), ('2', 4), ('1', 3), ('2', 2), ('1', 1), ('9', 1), ('1', 1), ('9', 1), ('2', 1), ('1', 6), ('2', 3), ('0', 1), ('1', 1), ('2', 2), ('1', 2), ('2', 2), ('0', 1), ('2', 2), ('0', 1), ('2', 1), ('0', 1), ('1', 1), ('2', 2), ('1', 1), ('2', 2), ('1', 2), ('2', 1), ('1', 2), ('2', 3), ('0', 1), ('1', 2), ('2', 1), ('6', 1), ('0', 2), ('2', 1), ('0', 1), ('1', 2), ('2', 1), ('1', 2), ('2', 3), ('1', 4), ('9', 1), ('2', 2), ('9', 1)], [('0', 2), ('2', 1), ('1', 1), ('2', 1), ('0', 1), ('1', 2), ('2', 2), ('1', 2), ('2', 2), ('1', 1), ('0', 1), ('1', 2), ('2', 2), ('1', 3), ('9', 1), ('2', 1), ('9', 2), ('2', 1), ('1', 2), ('2', 1), ('0', 1), ('1', 1), ('2', 1), ('1', 2), ('2', 1), ('0', 1), ('1', 1), ('2', 2), ('1', 3), ('2', 2), ('1', 1), ('2', 2), ('1', 2), ('0', 1), ('2', 2), ('1', 2), ('2', 1), ('1', 1), ('2', 3), ('1', 2), ('6', 1), ('0', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 2), ('2', 1), ('1', 2), ('0', 1), ('2', 1), ('1', 1), ('2', 2), ('1', 2), ('0', 1), ('2', 1), ('1', 1), ('2', 1), ('0', 1), ('1', 2), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 2), ('0', 1)], [('1', 2), ('2', 2), ('1', 1), ('2', 1), ('1', 1), ('2', 2), ('1', 1), ('2', 1), ('1', 1), ('0', 1), ('1', 1), ('2', 1), ('1', 2), ('2', 1), ('0', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 2), ('1', 3), ('2', 1), ('6', 1), ('2', 1), ('1', 1), ('2', 1), ('0', 1), ('1', 1), ('2', 1), ('0', 1), ('2', 2), ('9', 1), ('0', 1), ('1', 1), ('2', 1), ('9', 3), ('2', 5), ('1', 1), ('2', 2), ('1', 2), ('2', 1), ('0', 1), ('1', 2), ('2', 3), ('1', 1), ('2', 1), ('1', 2), ('2', 1), ('0', 2), ('2', 1), ('1', 1), ('2', 2), ('0', 1), ('2', 1), ('1', 2), ('2', 1), ('0', 1), ('1', 1), ('2', 2), ('1', 1), ('2', 1), ('0', 1), ('2', 1), ('1', 2), ('2', 2), ('1', 2), ('2', 1), ('1', 1), ('2', 2), ('1', 1), ('2', 1), ('9', 1), ('2', 2), ('0', 2), ('2', 1), ('1', 1), ('0', 1), ('1', 5), ('2', 1), ('1', 1), ('2', 1), ('0', 1), ('9', 1)], [('9', 2), ('2', 1), ('1', 3), ('2', 4), ('1', 1), ('0', 1), ('2', 2), ('1', 1), ('2', 1), ('1', 1), ('2', 6), ('0', 1), ('2', 2), ('0', 1), ('2', 1), ('0', 1), ('2', 1), ('1', 1), ('2', 2), ('0', 1), ('2', 2), ('0', 1), ('1', 1), ('0', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('6', 1), ('2', 1), ('1', 1), ('2', 2), ('1', 1), ('0', 1), ('2', 1), ('1', 2), ('2', 1), ('1', 1), ('0', 1), ('2', 3), ('1', 1), ('0', 2), ('2', 2), ('0', 1), ('2', 2), ('6', 1), ('2', 1), ('1', 1), ('2', 2), ('1', 1), ('2', 2), ('1', 2), ('2', 3), ('9', 1), ('2', 1), ('1', 3), ('2', 1), ('0', 1), ('2', 4), ('1', 1), ('2', 1), ('1', 1), ('0', 1), ('2', 1), ('1', 2), ('9', 1)], [('0', 1), ('2', 1), ('1', 2), ('0', 1), ('1', 1), ('2', 1), ('0', 1), ('1', 1), ('2', 1), ('1', 3), ('2', 1), ('1', 1), ('2', 3), ('1', 1), ('0', 1), ('2', 2), ('1', 1), ('2', 5), ('1', 1), ('2', 4), ('9', 1), ('2', 4), ('0', 1), ('9', 1), ('2', 2), ('1', 1), ('0', 1), ('2', 1), ('0', 1), ('9', 1), ('1', 1), ('0', 1), ('1', 1), ('0', 1), ('1', 1), ('2', 3), ('1', 3), ('0', 1), ('1', 1), ('2', 9), ('9', 1), ('1', 2), ('2', 2), ('1', 1), ('0', 1), ('6', 1), ('0', 1), ('2', 2), ('1', 3), ('0', 1), ('2', 2), ('0', 2), ('1', 4)], [('1', 2), ('2', 1), ('1', 2), ('2', 3), ('0', 1), ('1', 2), ('2', 1), ('1', 2), ('0', 1), ('1', 2), ('9', 2), ('1', 1), ('2', 1), ('1', 1), ('2', 4), ('0', 1), ('1', 1), ('2', 2), ('1', 2), ('2', 1), ('6', 1), ('2', 3), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 2), ('2', 1), ('1', 1), ('0', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('9', 1), ('0', 1), ('2', 1), ('1', 1), ('0', 1), ('2', 2), ('1', 1), ('2', 1), ('1', 2), ('2', 1), ('0', 1), ('1', 2), ('2', 1), ('1', 1), ('2', 3), ('0', 1), ('1', 3), ('0', 1), ('2', 1), ('6', 1), ('0', 2), ('2', 1), ('0', 1), ('2', 2), ('1', 1), ('2', 1), ('1', 4), ('0', 1), ('1', 4), ('0', 1), ('1', 2), ('9', 1), ('0', 3), ('1', 1), ('0', 1), ('2', 3), ('0', 1), ('1', 1), ('6', 1), ('0', 1), ('1', 1), ('2', 1), ('1', 2), ('2', 1), ('1', 1), ('2', 1), ('0', 1), ('1', 1), ('2', 1), ('1', 2), ('0', 1), ('1', 2), ('2', 1), ('1', 1), ('9', 1)]]
# seq1 = '21212102121012000121212102121'
# # --
# [[('2', 2), ('0', 1), ('1', 2), ('2', 1), ('1', 4), ('2', 2), ('0', 1), ('2', 1), ('1', 3), ('2', 1), ('9', 2)], [('6', 1), ('2', 1), ('1', 1), ('0', 1), ('2', 4), ('1', 1), ('0', 1), ('2', 2), ('1', 1), ('2', 4), ('1', 2), ('2', 2), ('0', 2), ('1', 1), ('2', 1), ('1', 1), ('0', 1), ('2', 2), ('1', 1), ('2', 1), ('0', 1), ('6', 1), ('2', 1), ('1', 2), ('2', 2), ('9', 1), ('1', 1), ('0', 2), ('1', 1), ('2', 7), ('1', 1), ('2', 3), ('1', 2), ('0', 1), ('1', 2), ('2', 1), ('0', 1), ('1', 1), ('0', 1), ('9', 1)], [('2', 2), ('1', 2), ('2', 2), ('1', 1), ('0', 1), ('1', 2), ('0', 1), ('1', 1), ('0', 1), ('1', 2), ('0', 1), ('2', 1), ('1', 2), ('0', 1), ('1', 1), ('0', 1), ('1', 1), ('2', 1), ('0', 1), ('1', 3), ('2', 2), ('9', 2)], [('2', 2), ('1', 2), ('2', 1), ('0', 1), ('2', 1), ('1', 1), ('2', 2), ('0', 1), ('2', 1), ('1', 3), ('2', 2), ('1', 1), ('2', 3), ('1', 1), ('2', 1), ('1', 5), ('9', 1), ('0', 2), ('1', 3), ('2', 1), ('0', 1), ('1', 2), ('2', 2), ('1', 2), ('9', 2)], [('1', 1), ('2', 2), ('1', 1), ('2', 1), ('0', 1), ('1', 1), ('2', 2), ('1', 1), ('0', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 2), ('1', 1), ('2', 2), ('1', 1), ('2', 1), ('9', 1), ('1', 2), ('0', 1), ('2', 1), ('9', 1), ('6', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 2), ('0', 1), ('1', 1), ('9', 1), ('0', 1), ('1', 1), ('0', 1), ('2', 1), ('1', 1), ('0', 1), ('2', 1), ('0', 1), ('1', 1), ('2', 4), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('9', 1)], [('1', 1), ('2', 1), ('1', 3), ('2', 1), ('0', 1), ('1', 1), ('2', 1), ('1', 2), ('0', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 4), ('1', 2), ('6', 1), ('1', 1), ('0', 1), ('1', 1), ('2', 3), ('1', 1), ('9', 1), ('2', 1), ('1', 2), ('2', 1), ('0', 1), ('2', 3), ('0', 1), ('9', 1)], [('1', 3), ('2', 2), ('1', 2), ('2', 1), ('1', 1), ('2', 1), ('0', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('0', 2), ('2', 1), ('1', 1), ('2', 1), ('1', 5), ('2', 1), ('0', 1), ('2', 1), ('0', 2), ('1', 1), ('9', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('6', 1), ('1', 1), ('0', 1), ('1', 2), ('6', 1), ('1', 2), ('0', 2), ('2', 1), ('1', 1), ('0', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 4), ('1', 2), ('9', 1)], [('1', 2), ('2', 1), ('1', 1), ('2', 1), ('1', 2), ('0', 1), ('1', 2), ('0', 2), ('2', 1), ('0', 1), ('1', 1), ('0', 1), ('1', 3), ('2', 4), ('1', 1), ('2', 4), ('0', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('6', 1), ('9', 2)], [('2', 1), ('0', 2), ('1', 1), ('2', 2), ('1', 1), ('2', 1), ('1', 3), ('2', 5), ('1', 1), ('9', 1), ('0', 2), ('1', 1), ('2', 3), ('1', 2), ('2', 1), ('1', 2), ('0', 1), ('1', 1), ('2', 1), ('0', 1), ('2', 1), ('1', 2), ('2', 2), ('1', 1), ('0', 1), ('1', 1), ('2', 1), ('1', 1), ('0', 1), ('1', 2), ('2', 1), ('1', 2), ('9', 1), ('1', 1), ('9', 1)], [('1', 2), ('9', 1), ('1', 2), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('0', 1), ('2', 4), ('1', 1), ('2', 1), ('1', 1), ('2', 3), ('0', 1), ('1', 5), ('9', 1), ('2', 2), ('1', 1), ('0', 1), ('1', 3), ('6', 1), ('1', 1), ('2', 1), ('0', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 1), ('2', 1), ('1', 2), ('0', 2), ('1', 1), ('2', 4), ('1', 3), ('0', 2), ('2', 2), ('0', 1), ('2', 1), ('1', 3), ('2', 3), ('1', 1), ('0', 2), ('2', 1), ('1', 1), ('2', 1), ('9', 1)]]
# # 2012120129
# # Find Sequence : 1.748992919921875
# # ---
# mid_boss =[
#     [('5', 1), ('6', 4), ('5', 1), ('6', 1), ('5', 2), ('6', 3), ('5', 1), ('6', 3), ('5', 1), ('6', 1), ('4', 1), ('5', 1), ('6', 2), ('5', 1), ('6', 1)], 
#     [('6', 2), ('5', 1), ('6', 1), ('5', 1), ('6', 1), ('5', 1), ('6', 5), ('5', 1), ('6', 5), ('5', 1), ('6', 3), ('d', 2)], 
#     [('6', 1), ('4', 1), ('6', 1), ('4', 1), ('6', 3), ('5', 1), ('6', 5), ('5', 1), ('6', 3), ('5', 1), ('6', 1), ('5', 4), ('6', 1), ('5', 1), ('4', 1), ('5', 1), ('6', 2), ('5', 2), ('6', 1), ('5', 1), ('6', 3), ('5', 3), ('6', 2), ('4', 1), ('6', 1), ('5', 1), ('6', 5), ('5', 1), ('6', 3), ('5', 1), ('4', 1), ('6', 1), ('5', 1), ('6', 2), ('5', 1), ('6', 5), ('5', 1), ('6', 2)], 
#     [('6', 1), 
#     ('d', 1), ('4', 1), ('6', 1), ('5', 1), 
#     ('6', 2), 
#     ('4', 2), ('6', 6), 
#     ('5', 2), 
#     ('4', 1), ('5', 3), 
#     ('6', 2), 
#     ('5', 1), 
#     ('6', 3), 
#     ('d', 1)], 
#     [('6', 4), ('5', 1), ('6', 2), ('4', 1), ('6', 4), ('4', 1), ('6', 1), ('4', 1), ('6', 2), ('5', 2), ('4', 1), ('5', 2), ('6', 2), ('5', 1), ('4', 1), ('6', 1), ('5', 1), ('6', 4), ('4', 1), ('6', 2), ('5', 2), ('6', 2), ('a', 1), ('6', 1), ('5', 1), ('6', 1), ('d', 1), ('5', 1), ('4', 1), ('d', 1), ('6', 4), ('5', 4), ('d', 1), ('4', 1), ('5', 1), ('6', 1), ('5', 1), ('d', 1), ('6', 2), ('5', 1), ('6', 4), ('5', 1), ('6', 2), ('4', 1), ('5', 3), ('6', 1)], [('6', 5), ('5', 2), ('6', 1), ('4', 1), ('5', 2), ('6', 1), ('4', 1), ('6', 3), ('4', 1), ('6', 5), ('5', 3), ('6', 1), ('4', 1), ('6', 1), ('5', 1), ('6', 2), ('5', 1), ('6', 3), ('d', 1)], [('6', 3), ('4', 1), ('5', 1), ('6', 1), ('4', 1), ('6', 5), ('5', 1), ('a', 1), ('6', 10), ('4', 1), ('6', 4), ('5', 1), ('6', 4), ('5', 1), ('6', 2), ('4', 1), ('6', 3), ('5', 2), ('6', 1), ('4', 1), ('6', 1), ('4', 1), ('6', 3), ('4', 1), ('5', 1), ('6', 3), ('5', 3), ('6', 1), ('d', 1), ('5', 1), ('6', 2), ('d', 1)], [('5', 1), ('6', 1), ('5', 1), ('6', 1), ('4', 1), ('6', 1), ('5', 2), ('6', 2), ('5', 1), ('6', 1), ('4', 1), ('6', 1), ('5', 1), ('6', 3), ('4', 1), ('6', 2), ('5', 2), ('6', 1), ('4', 1), ('5', 1), ('6', 4), ('4', 2), ('5', 2), ('6', 1), ('d', 1)], [('6', 3), ('a', 1), ('6', 1), ('5', 1), ('6', 1), ('5', 1), ('6', 4), ('4', 1), ('5', 1), ('6', 5), ('5', 2), ('6', 1), ('4', 2), ('6', 6), ('5', 1), ('6', 2), ('5', 1), ('6', 1), ('4', 1), ('6', 1), ('4', 1), ('6', 1), ('5', 2), ('6', 3), ('5', 1), ('6', 3), ('d', 1), ('6', 7), ('5', 1), ('4', 1), ('6', 1), ('5', 1)], [('6', 4), ('5', 2), ('4', 1), ('6', 2), ('5', 1), ('6', 1), ('5', 1), ('6', 3), ('5', 1), ('d', 1), ('a', 1), ('4', 1), ('5', 1), ('a', 1), ('6', 3), ('5', 1), ('4', 1), ('6', 3), ('5', 1), ('4', 1), ('5', 1), ('6', 1), ('d', 1), ('5', 1), ('6', 1), ('5', 1), ('6', 5), ('d', 2)]]
# seq2= '656655656'

# ans = [2, 5, 1, 1, 0, 2, 3, 1, 0, 1, 2, 2, 0, 2, 0, 2, 0, 2, 0, 2, 4, 3, 0, 3]
# Find Sequence : 4.642381906509399




# def find_remain(seq, target, cur=[], inc=0, idx=0):
#     cur = []
#     t_idx = 0
#     start = 0
#     print(target)
#     while t_idx < len(target):
#         for i in range(start, len(seq)):
#             if seq[i][0] == target[t_idx]:
#                 t_idx += 1
#                 cur.append(i)
#                 print( (seq[i],i) ,end=" ")
#                 start = i + 1
#                 break
#     print()
#     print("REMAIN", start)
#     return start

# def good_find_sequence(seq, target) :
#     obj = {}
#     for idx, s in enumerate(seq) :
#         sym = s[0]
#         if not sym in obj :
#             obj[sym] = []
#         obj[sym].append((s[1],idx))
#     output = []

#     lb = -1 #lower bound
#     for i in range(len(target)) :
#         sym = target[i]
#         print(target[i+1:][::-1])
#         print(len(seq))
#         ub = len(seq) - find_remain(seq[::-1],target[i+1:][::-1])
#         selectable = obj[sym]
#         print("BOUND",lb,'~',ub)
#         selectable = list(filter(lambda x: ub > x[1] > lb, selectable))
#         best = sorted(selectable,key=lambda x :-x[0])[0]  
#         lb = best[1]
#         output.append(lb)
#         print(output)

#     return obj


# # for bos in mid_boss:
# #     print(find_sequence(bos,seq2))

# # print(find_remain(mid_boss[0],seq2))
# print(good_find_sequence(mid_boss[3],seq2))


test = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'abc', 'def', 'ghi']

def alg1(cs_set):
    length = 1
    while True :
        cs_set = set(cs_set)
        if len(cs_set) > 10 :
            cs_set = filter(lambda x : len(x) > length, cs_set)
            break
        length += 1
    return cs_set
    
test = list(alg1(test))  # ['abc', 'def', 'ghi']

# ['abc', 'def', 'ghi']
from itertools import combinations
def alg2(cs_set):
    filtered_permutation = []
    for i in range(len(cs_set), 0, -1):
        filtered_permutation.extend(list(combinations(cs_set, i)))
    return filtered_permutation

test = alg2(test)
print(test)

test2 = ['abcdefgnbabc','defghiasdf','abcdefghijkl']
import re

for per in test :
    _const = None
    print(per)
    for t in test2 :
        reg = '|'.join(per)
        const = '&&&&&&&&&&&'.join([find.group() for find in re.finditer(reg,t)])
        print(const)
        if _const == None :
            _const = const # init
        if _const != None and const != _const :
            break
    else :
        print(per)
        break
else :
    print("SHIT")
