class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class ConversionTree:
    def __init__(self, root=None):
        self.root = root
        self.postfix = []
    
    def __isEmpty(self, stack):
        return stack == []
    
    def __isOperator(self, op):
        return op in ['+', '-', '*', '/', '^', '(', ')']
    
    def __precedence(self, op):
        precedence = {'(':0, ')':0, '+':1, '-':1, '*':2, '/':2, '^':3}
        return precedence[op]

    def __result(self, operand1, operand2, operator):
        if operator == '+':
            return operand1+operand2
        elif operator == '-':
            return operand1-operand2
        elif operator == '*':
            return operand1*operand2
        else:
            return operand1/operand2
    
    def __infixToPostfix(self, infix):
        operator = []
        for i in infix:
            if not self.__isOperator(i):
                self.postfix.append(Node(i))
            elif i == '(':
                operator.append(Node(i))
            elif i == ')':
                while operator[-1].data!='(' and not self.__isEmpty(operator):
                    self.postfix.append(operator.pop())
                operator.pop()
            elif self.__isOperator(i):
                while not self.__isEmpty(operator) and self.__precedence(i) <= self.__precedence(operator[-1].data):
                    self.postfix.append(operator.pop())
                operator.append(Node(i))
        while not self.__isEmpty(operator):
            self.postfix.append(operator.pop())
    
    def operator(self, i):
        if not self.__isOperator(i.data):
            return i
        i.right = self.operator(self.postfix.pop())
        i.left = self.operator(self.postfix.pop())
        return i

    def Expression(self, infix):
        self.__infixToPostfix(infix)
        self.root = self.operator(self.postfix.pop())

    def evaluateExpression(self, root):
        # Empty Tree
        if not root:
            return 0
        
        # leaf node
        if not (root.left and root.right):
            return int(input("Enter value: "))
        
        left = self.evaluateExpression(root.left)
        right = self.evaluateExpression(root.right)
        return self.__result(left, right, root.data)
    
    def mergeExpression(self, exp1, exp2):
        l = ConversionTree()
        l.Expression(exp1)
        lf = l.evaluateExpression(l.root)
        
        r = ConversionTree()
        r.Expression(exp2)
        rg = r.evaluateExpression(r.root)

        return self.__result(lf, rg, input("Enter Operator: "))

    def height(self, root):
        if not root:
            return -1
        lDepth = self.height(root.left)
        rDepth = self.height(root.right)
        return max(lDepth, rDepth)+1
    
    def leaf(self, root):
        if not root:
            return 0
        if not (root.left and root.right):
            return 1
        left = self.leaf(root.left)
        right = self.leaf(root.right)
        return left+right

    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.data, end=' ')
            self.printInorder(root.right)
            return
        # print("Empty Tree")

if __name__ == "__main__":
    exp1 = "a+b*c+d"
    exp2 = "a+b*c+d"
    t = ConversionTree()
    t.Expression(exp1)
    # t.Expression("k+l-m*n+(o^p)*w/u/v*t+q")
    print(t.evaluateExpression(t.root))
    print(t.height(t.root), t.leaf(t.root))
    # print(t.mergeExpression(exp1, exp2))