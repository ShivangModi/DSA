# Expression Evaluation:-
# Evaluate an expression represented by a String. 
# The expression can contain parentheses, we can assume parentheses are well-matched. 
# For simplicity, we can assume only binary operations allowed are +, -, *, and /. 
# Arithmetic Expressions can be written in one of three forms:
#   - Infix Notation: Operators are written between the operands they operate on, e.g. 3 + 4.
#   - Prefix Notation: Operators are written before the operands, e.g + 3 4
#   - Postfix Notation: Operators are written after operands.

# Infix:
# The typical mathematical form of expression that we encounter generally is known as infix notation. 
# In infix form, an operator is written in between two operands.
# For example, An expression in the form of A * ( B + C ) / D is in infix form. 
# This expression can be simply decoded as: 
# “Add B and C, then multiply the result by A, and then divide it by D for the final answer.”

# Prefix: 
# In prefix expression, an operator is written before its operands. 
# This notation is also known as “Polish notation”.
# For example, The above expression can be written in the prefix form as / * A + B C D. 
# This type of expression cannot be simply decoded as infix expressions.

# Postfix: 
# In postfix expression, an operator is written after its operands. 
# This notation is also known as “Reverse Polish notation”.
# For example, The above expression can be written in the postfix form as A B C + * D /. 
# This type of expression cannot be simply decoded as infix expressions.

# Precedence of Operators:
# The precedence of operators gives us an order in which operators are evaluated in any expression.
# Computers have a similar idea of precedence, too, when it comes to operators. 
# It is as follows:
#   - Exponential (^)
#   - Multiplication and division (* /)
#   - Addition and subtraction (+ –)

from Stack import Stack


class ExpressionEvaluation:
    def __init__(self):
        self.operand = None
        self.operator = None

    def __isOperator(self, operator):
        return operator in ['+', '-', '*', '/', '^']

    def __precedence(self, operator):
        if operator in ['+', '-']:
            return 1
        elif operator in ['*', '/']:
            return 2
        elif operator in ['^']:
            return 3
        return -1

    def __executeOperation(self):
        a = self.operand.pop()
        b = self.operand.pop()
        sign = self.operator.pop()
        if sign == '+':
            return a + b
        elif sign == '-':
            return b - a
        elif sign == '*':
            return a * b
        elif sign == '/':
            if a == 0:
                print("Can't divide by zero.")
                return
            return b / a
        return 0

    # Infix Expression Evaluation Algorithm:
    # Step 1: Create two stacks - the operand stack and the character stack.
    # Step 2: Push the character to the operand stack if it is an operand.
    # Step 3: If it is an operator, check if the operator stack is empty. 
    # Step 4: If the operator stack is empty, push it to the operator stack.
    # Step 5: If the operator stack is not empty, compare the precedence of the operator and the top character in the stack. If the character’s 
    #         precedence is greater than or equal to the precedence of the stack top of the operator stack, then push the character to the operator 
    #         stack. Otherwise, pop the elements from the stack until the character’s precedence is less or the stack is empty.
    # Step 6: If the character is “(“, push it into the operator stack.
    # Step 7: If the character is “)”, then pop until “(” is encountered in the operator stack.
    def evaluateInfixExpression(self, exp):
        self.operand = Stack()
        self.operator = Stack()

        exp = exp.split()
        for i in exp:
            if i.isdigit():
                self.operand.push(int(i))
            elif i == '(':
                self.operator.push(i)
            elif i == ')':
                while self.operator.peek() != '(':
                    op = self.__executeOperation()
                    self.operand.push(op)
                self.operator.pop()
            elif self.__isOperator(i):
                while not self.operator.isEmpty() and self.__precedence(i) <= self.__precedence(self.operator.peek()):
                    op = self.__executeOperation()
                    self.operand.push(op)
                self.operator.push(i)

        while not self.operator.isEmpty():
            op = self.__executeOperation()
            self.operand.push(op)
        print(self.operand.peek())

    # Postfix Expression Evaluation Algorithm:
    # Step 1: Create an operand stack.
    # Step 2: If the character is an operand, push it to the operand stack.
    # Step 3: If the character is an operator, pop two operands from the stack, operate and push the result back to the stack.
    # Step 4: After the entire expression has been traversed, pop the final result from the stack.
    def evaluatePostfixExpression(self, exp):
        self.operand = Stack()
        self.operator = Stack()

        exp = exp.split()
        for i in exp:
            if i.isdigit():
                self.operand.push(int(i))
            else:
                self.operator.push(i)
                op = self.__executeOperation()
                self.operand.push(op)
        print(self.operand.peek())

    # Prefix Expression Evaluation Algorithm:
    # Step 1: Reverse the postfix expression.
    # Step 2: Create an operand stack.
    # Step 3: If the character is an operand, push it to the operand stack.
    # Step 4: If the character is an operator, pop two operands from the stack, operate and push the result back to the stack.
    # Step 5: After the entire expression has been traversed, pop the final result from the stack.
    def evaluatePrefixExpression(self, exp):
        self.operand = Stack()

        exp = exp.split()
        e = exp[::-1]
        for i in e:
            if i.isdigit():
                self.operand.push(int(i))
            else:
                a = self.operand.pop()
                b = self.operand.pop()
                res = 0
                if i == '+':
                    res = a + b
                elif i == '-':
                    res = a - b
                elif i == '*':
                    res = a * b
                elif i == '/':
                    if b == 0:
                        print("Can't divide by zero.")
                        return
                    res = a / b
                self.operand.push(res)
        print(self.operand.peek())


if __name__ == "__main__":
    ee = ExpressionEvaluation()
    ee.evaluateInfixExpression("( 2 + 3 ) * 4 - 5")
    ee.evaluatePostfixExpression("2 3 + 4 * 5 -")
    ee.evaluatePrefixExpression("- * + 2 3 4 5")
