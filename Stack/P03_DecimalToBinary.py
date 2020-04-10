# Author: OMKAR PATHAK

# Decimal to binary using Stack

class Stack(object):
    def __init__(self, limit = 10):
        self.stack = []
        self.limit = limit

    # for printing the stack contents
    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    # for pushing an element on to the stack
    def push(self, data):
        if len(self.stack) >= self.limit:
            print('Stack Overflow')
        else:
            self.stack.append(data)

    # for popping the uppermost element
    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()

    # for peeking the top-most element of the stack
    def peek(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[len(self.stack) - 1]

    # to check if stack is empty
    def isEmpty(self):
        return self.stack == []

    # for checking the size of stack
    def size(self):
        return len(self.stack)


def dtob(decimal, base = 2):
    myStack = Stack()
    while decimal > 0:
        myStack.push(decimal % base)
        decimal //= base

    result = ''
    while not myStack.isEmpty():
        result += str(myStack.pop())

    return result


if __name__ == '__main__':
    dtob(15)
