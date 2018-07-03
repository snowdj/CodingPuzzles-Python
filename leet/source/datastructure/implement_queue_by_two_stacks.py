class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack0 = []
        self.stack1 = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack0.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack1) > 0:
            return self.stack1.pop()

        self.transfer()
        if len(self.stack1) == 0:
            return None
        return self.stack1.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack1) > 0:
            return self.stack1[-1]

        self.transfer()
        if len(self.stack1) == 0:
            return None
        return self.stack1[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack0) == 0

    def transfer(self):
        while True:
            try:
                self.stack1.append(self.stack0.pop())
            except IndexError:
                break

if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.pop()
    q.push(2)
    q.push(3)
    print(q.top())
    print(q.pop())


