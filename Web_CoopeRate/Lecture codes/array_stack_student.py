class ArrayStack:
    ''' Stack implemented with python list append/pop'''
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def push(self, e):
        self.array.append(e)

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self.array[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self.array.pop(-1)

    def __repr__(self):
        return str(self.array)

def spans2(X):
    '''
    :param X: List[Int] -- list of integers.
    Use a stack. We use the stack to compute the span distance.
    If the top of the stack is “Smaller” than the next data,
    top of the stack should be popped.
    :return: list of span values.
    '''
    stk = ArrayStack()
    spans = [0] * len(X)
    
    for i in range(len(X)):
        print("looping:",i)
        # Pop elements that are smaller than X[i]
        while not stk.is_empty() and X[i] >= X[stk.top()]:
            stk.pop()
        
        # If stack is empty, span is i + 1
        spans[i] = i + 1 if stk.is_empty() else i - stk.top()
        
        # Push this element to the stack
        stk.push(i)

        
    return spans

def main():
    print(spans2([6,3,4,5,2])) # [1, 1, 2, 3, 1]
    print(spans2([6,7,1,3,4,5,2]))  # [1, 2, 1, 2, 3, 4, 1]

if __name__ == '__main__':
    main()

