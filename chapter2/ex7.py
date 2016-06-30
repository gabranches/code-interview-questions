from single_linklist import Node


def merge_lists(a, b):
    head = a
    while a.next:
        a = a.next
    a.next = b
    return head


def traverse(a, b):
    while a.next:
        if a == b:
            return a
        a = a.next
    return None


def get_intersection(a, b):
    return traverse(a, b) or traverse(b, a)


if __name__ == '__main__':
    
    a = Node.list_to_link([1,2,3])
    b = Node.list_to_link([4,5,6])
    b = merge_lists(b, a)

    print(get_intersection(b, a))
