class Stack:
    __storage = None
    __stack_size = None

    def __init__(self):
        self.storage = []
        self.stack_size = -1

    def push(self, value):
        self.storage.append(value)
        self.stack_size += 1

    def pop(self):
        if self.stack_size == -1:
            print("Stack underflow")
            return False
        else:
            popped_value = self.storage.pop()
            self.stack_size -= 1
            return popped_value

    def top(self):
        if self.stack_size == -1:
            print("Stack is empty")
        else:
            print(self.storage[self.stack_size])
            return self.storage[self.stack_size]

    def empty(self):
        if self.stack_size == -1:
            print("Stack is empty")
            return True
        else:
            print("Stack is not empty")
            return False

    def size(self):
        print(self.stack_size + 1)
        return self.stack_size + 1
