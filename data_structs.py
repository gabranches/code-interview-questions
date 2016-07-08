class LinkListNode:
    'A singly-listed link'
    
    def __init__(self, data):
        self.next = None
        self.data = data


    def head(self, data):
        head = Node(data)
        head.next = self
        return head


    def add(self, data):
        if self.next == None:
            self.next = Node(data)
        else:
            self.next.add(data)


    def __str__(self):
        res = ''        
        while self.next != None:
            res += str(self.data) + ' -> '
            self = self.next
        return (res + str(self.data))


    @classmethod
    def list_to_link(self, list):
        x, xs = list[0], list[1:]
        link = Node(x)
        for each in xs:
            link.add(each)
        return link


class Stack:
    'Stack implented using a list'

    def __init__(self, list=None):
        self.stack = []
        if list:
            for item in list:
                self.push(item)


    def pop(self):
        xs, x = self.stack[:-1], self.stack[-1]
        self.stack = xs
        return x


    def push(self, item):
        self.stack.append(item)


    def is_empty(self):
        return True if len(self.stack) == 0 else False


    def peek(self):
        return self.stack[-1]


    def size(self):
        return len(self.stack)


    def reverse(self):
        temp = Stack()
        while self.size() > 0:
            temp.push(self.stack.pop())
        return temp


    def __str__(self):
        if not self.is_empty():
            return str([x for x in reversed(self.stack)])
        return "Stack is empty."


class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def add(self, value):
        if self.value == None:
            self.value = value
        else:
            if value <= self.value:
                if self.left is not None:
                    self.left.add(value)
                else:
                    self.left = BinaryTreeNode(value)
            else:
                if self.right is not None:
                    self.right.add(value)
                else:
                    self.right = BinaryTreeNode(value)


    def print_tree(self):
        print(self.value)
        if self.left is not None:
            self.left.print_tree()
        if self.right is not None:
            self.right.print_tree()


    def __str__(self):
        self.print_tree()
        return ""
        























