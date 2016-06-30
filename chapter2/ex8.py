from single_linklist import Node
from ex7 import merge_lists


def detect_loop(n):
    head = n
    n = n.next
    while n.next:
        if n == head:
            return t
        n = n.next
    return None


if __name__ == '__main__':
        
    a = Node.list_to_link([1,2,3])
    b = Node.list_to_link([5,4,3])
    c = merge_lists(a, b)

    print(c)
    print(detect_loop(c))