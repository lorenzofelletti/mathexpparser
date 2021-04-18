from .tokens import *
import numpy as np


class Lexer:
    def __init__(self):
        self.__digits__ = '0123456789'
        self.__ops__ = '+-*/^'
        self.__unary_minus_equivalent__ = [ElementToken(-1), MulOp()]

    def __is_digit__(self, ch):
        return self.__digits__.find(ch) >= 0

    def __is_op__(self, ch):
        return self.__ops__.find(ch) >= 0

    def scan(self, exp):
        # eliminate all whitespace
        exp = exp.replace(' ', '')

        tokens = np.array([])

        def append_num():
            nonlocal num
            nonlocal tokens
            if len(num) == 0:
                return
            num_tkn = ElementToken(int(num))
            num = ''
            tokens = np.append(tokens, num_tkn)

        def append_op(op):
            nonlocal tokens

            if op == '+':
                op_tkn = PlusOp()
            elif op == '-':
                op_tkn = MinOp()
            elif op == '*':
                op_tkn = MulOp()
            elif op == '/':
                op_tkn = DivOp()
            elif op == '^':
                op_tkn = PowOp()
            else:
                return
            tokens = np.append(tokens, op_tkn)

        i = 0
        num = ''
        while i < len(exp):
            if self.__is_digit__(exp[i]):
                num += exp[i]
            elif self.__is_op__(exp[i]):
                # check if it is unary +/-
                if i == 0 or self.__is_op__(exp[i-1]) or exp[i-1] == '(':
                    if exp[i] == '+':
                        i += 1
                        continue
                    elif exp[i] == '-':
                        tokens = np.append(
                            tokens, self.__unary_minus_equivalent__)
                        i += 1
                        continue

                append_num()
                append_op(op=exp[i])
            elif exp[i] == '(':
                tokens = np.append(tokens, LeftParenthesis())
            elif exp[i] == ')':
                append_num()
                tokens = np.append(tokens, RightParenthesis())
            else:
                raise Exception('Unidentified character.')
            i += 1

        append_num()

        return tokens
