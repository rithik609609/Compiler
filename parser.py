# parser.py
import ply.yacc as yacc
from lexer import tokens


# Define a dictionary of names (for storing variables)
symbol_table = {}
# Define the precedence and associativity of operators
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NE')
)

#///////////////////////////// this will handle the assignment part

def p_statement_assign(p):
    'statement : ID EQUALS expression'
    symbol_table[p[1]] = p[3]
    p[0] = p[3]

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    try:
        p[0] = symbol_table[p[1]]
    except LookupError:
        print(f"Undefined variable '{p[1]}'")
        p[0] = ('int', 0)



#//////////this handles the int and float part
def p_expression_int(p):
    'expression : INT'
    p[0] = ('int', int(p[1]))
   

def p_expression_float(p):
    'expression : FLOAT'
    p[0] = ('float', float(p[1]))



#////////////code to handle airthmatic operators
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = ('int' if all(isinstance(i, int) for i in [p[1][1], p[3][1]]) else 'float', p[1][1] + p[3][1])
    elif p[2] == '-':
        p[0] = ('int' if all(isinstance(i, int) for i in [p[1][1], p[3][1]]) else 'float', p[1][1] - p[3][1])
    elif p[2] == '*':
        p[0] = ('int' if all(isinstance(i, int) for i in [p[1][1], p[3][1]]) else 'float', p[1][1] * p[3][1])
    elif p[2] == '/':
        p[0] = ('float', p[1][1] / p[3][1])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

#///////////////this will handle the comparison part
def p_expression_comparison(p):
    '''expression : expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression'''
    if p[2] == '<':
        p[0] = ('int', p[1][1] < p[3][1])
    elif p[2] == '>':
        p[0] = ('int', p[1][1] > p[3][1])
    elif p[2] == '<=':
        p[0] = ('int', p[1][1] <= p[3][1])
    elif p[2] == '>=':
        p[0] = ('int', p[1][1] >= p[3][1])
    elif p[2] == '==':
        p[0] = ('int', p[1][1] == p[3][1])
    elif p[2] == '!=':
        p[0] = ('int', p[1][1] != p[3][1])
#///////////////this will handle the errors
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

def parse(input_string):
    result = parser.parse(input_string)
    return result




# type: ignore