class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, head=None):
        self.__head = head
    
    def isEmpty(self):
        return not self.__head
    
    def push(self, val):
        new = Node(val)
        new.next = self.__head
        self.__head = new
    
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            temp = self.__head
            self.__head = self.__head.next
            temp.next = None
            del temp
    
    def peek(self):
        if self.isEmpty():
            print("Underflow")
        else:
            return self.__head.data

class Conversion:
    def __init__(self):
        self.precedence = {'(':0, ')':0, '+':1, '-':1, '*':2, '/':2, '^':3}
    
    def __isOperator(self, op):
        return op in ['+', '-', '*', '/', '^', '(', ')']

    # Infix to Postfix Conversion:-
    # Begin
    #    for each character ch from infix expression, do
    #       if ch is alphanumeric character, then
    #          add ch to postfix expression
    #       else if ch = opening parenthesis (, then
    #          push ( into stack
    #       else if ch = ^, then            //exponential operator of higher precedence
    #          push ^ into the stack
    #       else if ch = closing parenthesis ), then
    #          while stack is not empty and stack top ≠ (,
    #             do pop and add item from stack to postfix expression
    #          done
    
    #          pop ( also from the stack
    #       else
    #          while stack is not empty AND precedence of ch <= precedence of stack top element, do
    #             pop and add into postfix expression
    #          done
    
    #          push the newly coming character.
    #    done
    
    #    while the stack contains some remaining characters, do
    #       pop and add to the postfix expression
    #    done
    #    return postfix
    # End
    def infixToPostfix(self, infix):
        postfix = ''
        s = Stack()
        for i in infix:
            if not self.__isOperator(i):
                postfix += i
            elif i == '(':
                s.push(i)
            elif i == ')':
                while s.peek()!='(' and not s.isEmpty():
                    postfix += s.peek()
                    s.pop()
                s.pop()
            elif self.__isOperator(i):
                while not s.isEmpty() and self.precedence[i] <= self.precedence[s.peek()]:
                    postfix += s.peek()
                    s.pop()
                s.push(i)
        while not s.isEmpty():
            postfix += s.peek()
            s.pop()
        return postfix


if __name__ == "__main__":
    c = Conversion()
    print(c.infixToPostfix("k+l-m*n+(o^p)*w/u/v*t+q"))
    # print(c.infixToPostfix("a+b*(c+d*e)+f*g^h^i"))
