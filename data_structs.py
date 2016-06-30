class LinkListNode:
    
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