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
