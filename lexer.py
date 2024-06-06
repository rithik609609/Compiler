# lexer.py
import ply.lex as lex

# Reserved keywords
reserved = {
    'if': 'IF',
    'else': 'ELSE'
}

tokens = [
    'ID',
    'INT',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'LT',
    'GT',
    'LE',
    'GE',
    'EQ',
    'NE'
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='

t_FLOAT = r'\d+\.\d+'
t_INT = r'\d+'
t_ignore = ' \t\n'  # Ignore whitespace and newlines

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
