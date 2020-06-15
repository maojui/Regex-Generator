
import string

WORD = string.ascii_letters + string.digits + '_'
SPACE = '\x0c\n\r\t\x0b\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u200a\u2028\u2029\u202f\u205f\u3000\ufeff'
SYMBOL = '''!@#$%^&*()[]';./,<>?:"{}-=`~|+-\/ '''
ESCAPE = '{([])^$.|*+?}'
INESCAPE = '^-'
LOWER_HEXDIGIT = '0123456789abcdef'
UPPER_HEXDIGIT = '0123456789ABCDEF'
CHAR_RANGE = WORD[:-1] # A-Za-z0-9
CHAR_RANGE_WITH_SYMBOLS = WORD[:-1] + SYMBOL 