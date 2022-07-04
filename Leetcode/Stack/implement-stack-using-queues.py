class Queue:
    def __init__(self):
        self.list = list()

    def is_empty(self):
        return len(self.list) == 0

    def push(self, element):
        self.list.append(element)

    def pop(self):
        if not self.is_empty():
            return self.list.pop(0)

    def size(self):
        return len(self.list)


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        if self.q1.is_empty():
            self.q1.push(x)
        else:
            while not self.q1.is_empty():
                self.q2.push(self.q1.pop())
            self.q1.push(x)
            while not self.q2.is_empty():
                self.q1.push(self.q2.pop())

    def pop(self):
        if not self.q1.is_empty():
            return self.q1.pop()

    def top(self):
        if not self.q1.is_empty():
            return self.q1.list[0]

    def empty(self):
        return self.q1.is_empty()


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    print(stack.empty())