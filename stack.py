class Stack:
    def __init__(self):
        self.body = []

    def isempty(self) -> bool:
        return (self.body == [])

    def push(self, elem):
        self.body.append(elem)

    def pop(self):
        if self.body:
            return self.body.pop()
        else:
            return None

    def peek(self):
        if self.body:
            return self.body[-1]
        else:
            return None

    def size(self) -> int:
        return len(self.body)
