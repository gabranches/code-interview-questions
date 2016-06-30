from single_linklist import Node

def get_node(node, data):
    if node.data == data:
        return node
    return get_node(node.next, data)


def middle_remove(node):
    node.data = node.next.data
    node.next = node.next.next


if __name__ == '__main__':
    
    a = Node('a')
    a.add('b')
    a.add('c')
    a.add('d')
    a.add('e')

    b = get_node(a, 'd')
    middle_remove(b)
    print(a)

