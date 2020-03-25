class SimpleScanner():
    def __init__(self):
        __init__(self)
    
    def tokenize(self, input):
        self.rv = []
        GenericScanner.tokenize(self, input)
        return self.rv
    
    def t_whitespace(self, s):
        r' \s+ '
        pass
        
    def t_op(self, s):
        r' \+ | \* '
        self.rv.append(Token(type=s))
        
    def t_number(self, s):
        r' \d+ '
        t = Token(type='number', attr=s)
        self.rv.append(t)

class FloatScanner(SimpleScanner):
    def __init__(self):
        SimpleScanner.__init__(self)
        
    def t_float(self, s):
        r' \d+ \. \d+ '
        t = Token(type='float', attr=s)
        self.rv.append(t)


class ExprParser():
    def __init__(self, start='expr'):
        __init__(self, start)
                
    def p_expr_1(self, args):
        ' expr ::= expr + term '
        return AST(type=args[1],
                   left=args[0],
                   right=args[2])
        
    def p_expr_2(self, args):
        ' expr ::= term '
        return args[0]
        
    def p_term_1(self, args):
        ' term ::= term * factor '
        return AST(type=args[1],
                   left=args[0],
                   right=args[2])
        
    def p_term_2(self, args):
        ' term ::= factor '
        return args[0]
        
    def p_factor_1(self, args):
        ' factor ::= number '
        return AST(type=args[0])

    def p_factor_2(self, args):
        ' factor ::= float '
        return AST(type=args[0])

class TypeCheck():
    def __init__(self, ast):
        __init__(self, ast)
        self.postorder()
        
    def n_number(self, node):
        node.exprType = 'number'
    def n_float(self, node):
        node.exprType = 'float'
        
    def default(self, node):
        # this handles + and * nodes
        leftType = node.left.exprType
        rightType = node.right.exprType
        if leftType != rightType:
            raise 'Type error.'
        node.exprType = leftType

class Interpret():
    def __init__(self, ast):
        __init__(self, ast)
        self.postorder()
        print(ast.value)
        
    def n_number(self, node):
        node.value = int(node.attr)
    def n_float(self, node):
        node.value = float(node.attr)
        
    def default(self, node):
        left = node.left.value
        right = node.right.value
        
        if node.type == '+':
            node.value = left + right
        else:
            node.value = left * right
class ExprParser():
    def __init__(self, start='expr'):
        __init__(self, start)
                
    def p_expr_term(self, args):
        '''
            expr ::= expr + term
            term ::= term * factor
        '''
        return AST(type=args[1],
                   left=args[0],
                   right=args[2])
        
    def p_expr_term_2(self, args):
        '''
            expr ::= term
            term ::= factor
        '''
        return args[0]
        
    def p_factor(self, args):
        '''
            factor ::= number
            factor ::= float
        '''
        return AST(type=args[0])

class ExprParser():
    def __init__(self, start='expr'):
        __init__(self, start)
                
    def p_rules(self, args):
        '''
            expr ::= expr + term
            expr ::= term
            term ::= term * factor
            term ::= factor
            factor ::= number
            factor ::= float
        '''
