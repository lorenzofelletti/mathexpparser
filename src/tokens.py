class Token:
    pass


class ElementToken(Token):
    def __init__(self, value):
        super().__init__()
        self.type = 'element'
        self.value = value


class ParenthesisToken(Token):
    def __init__(self):
        super().__init__()
        self.type = 'parenthesis'


class LeftParenthesis(ParenthesisToken):
    def __init__(self):
        super().__init__()
        self.side = 'L'


class RightParenthesis(ParenthesisToken):
    def __init__(self):
        super().__init__()
        self.side = 'R'


class BinOp(Token):
    def __init__(self):
        super().__init__()
        self.type = 'bin_op'


class PlusOp(BinOp):
    def __init__(self):
        super().__init__()
        self.op = '+'


class MinOp(BinOp):
    def __init__(self):
        super().__init__()
        self.op = '-'


class MulOp(BinOp):
    def __init__(self):
        super().__init__()
        self.op = '*'


class DivOp(BinOp):
    def __init__(self):
        super().__init__()
        self.op = '/'


class PowOp(BinOp):
    def __init__(self):
        super().__init__()
        self.op = '^'


class UnaryOp(Token):
    def __init__(self):
        super().__init__()
        self.type = 'un_op'


class UnaryMinus(UnaryOp):
    def __init__(self):
        super().__init__()
        self.op = '-'
