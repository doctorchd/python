class Stack:
    def __init__(self):
        self.items = []


    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: str) -> None:
        self.items.append(item)

    def pop(self) -> str | None:
        if self.is_empty():
            print('stack is empty')
            return None
        else:
            return self.items.pop()

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> str | None:
        if self.is_empty():
            return None
        else:
            return self.items[-1]

    def dump(self):
        # print(f'items: {self.items}, len: {self.size()}')
        for num in range(0, self.size()):
            # print(f'num: {num}')
            print(self.items[self.size() - num - 1])


my_stack = Stack()
for i in range(0, 4):
    my_stack.push(input('item? '))
    print('stack:')
    my_stack.dump()
    print(f'tos: {my_stack.peek()}')

for i in range(0, 5):
    print(f'pop {i + 1}')
    print(f'item: {my_stack.pop()}')
    print(f'tos: {my_stack.peek()}')
    print('')
