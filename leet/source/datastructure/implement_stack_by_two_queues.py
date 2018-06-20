class Stack:
    def __init__(self):
        self.queue0 = []
        self.queue1 = []

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.queue0.append(x)

    """
    @return: nothing
    """
    def pop(self):
        if self.isEmpty():
            return

        self.exchange(0, len(self.queue0) - 1)
        self.queue0.pop()
        self.exchange(1, len(self.queue1))

    """
    @return: an integer
    """
    def top(self):
        if self.isEmpty():
            return None

        self.exchange(0, len(self.queue0))
        result = self.queue1[-1]
        self.exchange(1, len(self.queue1))
        return result

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return len(self.queue0) == 0

    def exchange(self, startid, n):
        if startid == 0:
            for i in range(n):
                self.queue1.append(self.queue0[0])
                del self.queue0[0]
        else:
            for i in range(n):
                self.queue0.append(self.queue1[0])
                del self.queue1[0]

    def show(self):
        print(self.queue0)

class Stack1:

    def __init__(self):
        import Queue
        self.queue1 = Queue.Queue()
        self.queue2 = Queue.Queue()
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.queue1.put(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        item = self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return item

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        item = self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1
        self.push(item)
        return item

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return self.queue1.empty()

if __name__ == "__main__":
    stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.show()
    #
    # stack.pop()
    # stack.show()
    #
    # stack.top()
    # stack.show()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.show()
    stack.top()
    stack.pop()
    stack.top()
    stack.pop()
    stack.top()
    stack.isEmpty()
    stack.pop()
    stack.isEmpty()

