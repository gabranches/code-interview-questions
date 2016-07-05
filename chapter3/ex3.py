import sys
sys.path.insert(0, '.')

from data_structs import Stack


class SetOfStacks:

    max_items = 3

    def __init__(self):
        self.piles = Stack()
        self._create_new_stack()


    def _create_new_stack(self):
        self.piles.push(Stack())


    def push(self, item):
        if self.piles.peek().size() == self.max_items:
            self._create_new_stack()
            self.push(item)
        else:
            self.piles.peek().push(item)


    def pop(self):
        return self.piles.peek().pop()


    def pop_stack(self):
        return Stack.pop(self.piles)


    def is_empty(self):
        return self.piles.is_empty()


    def _backfill(self, new, old):
        while new.size() > 0:
            old.push(new.pop())


    def pop_at(self, index):
        if index > self.piles.size()-1:
            raise "Invalid index."

        temp_stack = Stack()
        for i in range(index, 0, -1):
            temp_stack.push(SetOfStacks.pop_stack(self))
        item = self.piles.pop()
        self._backfill(temp_stack.reverse(), self.piles)
        return item.pop()


    def __str__(self):
        if not self.is_empty():
            return Stack.__str__(self.piles)
        return "Stack is empty."


if __name__ = "__main__":
        
    a = SetOfStacks()
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    a.push(5)
    a.push(6)
    a.push(7)
    print(a.pop_at(3))
    print(a)

