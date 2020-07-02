
import string

DEBUG = False
INDEX_TABLE = lambda x : chr(x)

ESCAPE = '{([])^$.|*+?}\\'    # Inside () or Outside
INESCAPE = '^-'           # Inside []
DIGIT = string.digits
UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
LETTERS = string.ascii_letters
WORD = LETTERS + DIGIT + '_'
LOWER_HEXDIGIT = DIGIT + LOWER[:6]
UPPER_HEXDIGIT = DIGIT + UPPER[:6]
CHAR_RANGE = WORD[:-1] # A-Za-z0-9
SYMBOL = '''!@#$%^&*()[]';./,<>?:"{}-=`~|+-\\ '''
CHAR_RANGE_WITH_SYMBOLS = WORD[:-1] + SYMBOL 
SPACE = '\x0c\n\r\t\x0b\xa0\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u200a\u2028\u2029\u202f\u205f\u3000\ufeff'