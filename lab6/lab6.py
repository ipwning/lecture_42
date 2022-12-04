import sys
import ply.lex as lex

tokens = ('INT', 'FLOAT','RETURN', 'INCLUDE', 'ID', 'END', 'INC_PATH', 'PLUS', 'ASSIGN', 'START_SCOPE', 'END_SCOPE')

t_RETURN = r'return'
t_INCLUDE = r'\#include'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_END = r';'
t_INC_PATH = r'(<[/a-zA-Z_][./a-zA-Z0-9_]*.h>)|\"[./a-zA-Z_][./a-zA-Z0-9_]*.h\"'
t_PLUS = r'\+'
t_ASSIGN = r'='
t_START_SCOPE = r'\{'
t_END_SCOPE = r'\}'

t_ignore = ' \t'
literals = '(),'

def t_INT(t):
    r'int'
    t.value = 'long'
    return t

def t_FLOAT(t):
    r'float'
    t.value = 'double'
    return t
    
# Tokens

#TODO


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: python %s <input file>" % sys.argv[0])
    fp = open(sys.argv[1], "r")
    if (fp == 0):
        sys.exit("File not open: %s" % sys.argv[1])

    lexer = lex.lex()
    lexer.input(fp.read())
    ln = 1
    pos = 0
    prv = ''
    scp_cnt = 0
    tap = True
    for tok in lexer:

        diff = tok.lexpos - pos - len(prv)
        
        if diff > 0 and ln == tok.lineno:
            print(' ', end='')
        
        if ln != tok.lineno:
            print(''*(ln - tok.lineno))
            ln = tok.lineno
            tap = True
        
        if tap:
            mul = scp_cnt
            if tok.type == 'END_SCOPE':
                mul -= 1
            print('    '*mul, end='')
            tap = False
            
        if tok.type == 'START_SCOPE':
            scp_cnt += 1
        elif tok.type == 'END_SCOPE':
            scp_cnt -= 1

        prv = tok.value
        pos = tok.lexpos

        if tok.type == 'INT' or tok.type == 'FLOAT':
            pos -= 1

        print(tok.value, end='') 