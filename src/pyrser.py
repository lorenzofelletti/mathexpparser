from .lexer import Lexer
from .tokens import *
from .math_exp_ast import *


class Pyrser:
    """
    Pyrser parse mathematical expressions and return the expression's AST.
    The grammar recognized by the parser is:
    EXP ::= TERM(('+'|'-') TERM)*
    TERM ::= (TERM '*'|'/')* POW
    POW ::= FACTOR('^'POW)*
    FACTOR ::= num | '(' EXP ')'
    """

    def __init__(self):
        self.lxr = Lexer()

    def parse(self, exp):
        def next_tkn_initializer(exp):
            tokens = self.lxr.scan(exp=exp)

            i = -1

            def next_tkn():
                nonlocal i
                nonlocal tokens
                nonlocal curr_tkn
                i += 1
                if i < len(tokens):
                    curr_tkn = tokens[i]
                else:
                    curr_tkn = None

            return next_tkn

        def parse_exp():
            node = parse_term()

            while isinstance(curr_tkn, PlusOp) or isinstance(curr_tkn, MinOp):
                op_tkn = curr_tkn
                next_tkn()
                r_node = parse_term()
                if r_node is not None:
                    node = PlusOpNode(node, r_node) if isinstance(
                        op_tkn, PlusOp) else MinOpNode(node, r_node)
                else:
                    raise Exception('Unable to parse expression.')
            return node

        def parse_term():
            node = parse_pow()
            while isinstance(curr_tkn, BinOp) and curr_tkn.op in ('*', '/'):
                op_tkn = curr_tkn  # save the operation
                next_tkn()
                r_node = parse_pow()
                if r_node is not None:
                    node = MulOpNode(node, r_node) if isinstance(op_tkn, MulOp) \
                        else DivOpNode(node, r_node)
                else:
                    raise Exception('Unable to parse term.')
            return node

        def parse_pow():
            node = parse_factor()
            while curr_tkn is not None and isinstance(curr_tkn, PowOp):
                next_tkn()
                next_node = parse_factor()
                if next_node is not None:
                    # right associativity
                    if isinstance(node, PowOpNode):
                        node = PowOpNode(
                            node.left, PowOpNode(node.right, next_node))
                    else:
                        node = PowOpNode(node, next_node)
                else:
                    raise Exception('Unable to parse pow.')
            return node

        def parse_factor():
            if isinstance(curr_tkn, LeftParenthesis):
                next_tkn()
                inner_exp = parse_exp()
                if isinstance(curr_tkn, RightParenthesis):
                    next_tkn()
                    return inner_exp
                else:
                    raise Exception('Missing closing parenthesis.')
            elif isinstance(curr_tkn, ElementToken):
                node = ValueNode(curr_tkn.value)
                next_tkn()
                return node
            else:
                raise Exception('Missing factor.')

        curr_tkn = None
        next_tkn = next_tkn_initializer(exp)
        next_tkn()
        return parse_exp()
