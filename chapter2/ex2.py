from single_linklist import Node


def length(node):
        if node.next == None:
            return 1
        return 1 + length(node.next)


def _find_kth(node, length, k):
    if length-k == 0:
        return node.data
    return _find_kth(node.next, length-1, k)


def kth_to_last(node, k):
        return _find_kth(node, length(node), k)

if __name__ == '__main__':
        
    a = Node('a')
    a.add('b')
    a.add('c')
    a.add('d')
    a.add('e')
    print(a)
    print(length(a))
    print(kth_to_last(a, 2))
