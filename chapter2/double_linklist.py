class Node:

    def __init__(self, d, prev=None):
        self.prev = prev
        self.next = None
        self.data = d


    def append_tail(self, d):
        n = self
        # Find the last node
        while n.next:
            n = n.next
        # Attach new node to tail
        n.next = Node(d, n)


    def remove_node(self):
        # Last element
        if self.next == None:
            self.prev.next = None 
        # First element
        elif self.prev == None:
            self.data = self.next.data
            self.next = self.next.next
        # All otherse
        else:
            self.prev.next = self.next
            self.next.prev = self.prev


    def delete(self, d):
        n = self
        while n:
            if n.data == d:
                n.remove_node()
            n = n.next





    def __str__(self):
        res = ''        
        while self.next != None:
            res += str(self.data) + ' -> '
            self = self.next
        
        return (res + str(self.data))
        
