class ASTNode:
    pass


class ValueNode(ASTNode):
    def __init__(self, value):
        super().__init__()
        self.value = value
    
    def evaluate(self):
        return self.value


class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        super().__init__()
        self.left = left
        self.op = op
        self.right = right


class PlusOpNode(BinOpNode):
    def __init__(self, left, right):
        super().__init__(left=left, op='+', right=right)

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()


class MinOpNode(BinOpNode):
    def __init__(self, left, right):
        super().__init__(left=left, op='-', right=right)

    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()


class MulOpNode(BinOpNode):
    def __init__(self, left, right):
        super().__init__(left=left, op='*', right=right)

    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()


class DivOpNode(BinOpNode):
    def __init__(self, left, right):
        super().__init__(left=left, op='/', right=right)

    def evaluate(self):
        if self.right.evaluate() == 0:
            raise Exception('Cannot divide by 0')
        return self.left.evaluate() / self.right.evaluate()


class PowOpNode(BinOpNode):
    def __init__(self, left, right):
        super().__init__(left=left, op='^', right=right)

    def evaluate(self):
        return self.left.evaluate() ** self.right.evaluate()
