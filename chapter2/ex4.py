from single_linklist import Node


def swap(node):
    tmp = node.data
    n = node.next
    node.data = n.data
    n.data = tmp


def move_to_end(node):
    n = node
    while n.next:
        swap(n)
        n = n.next


def check_if_lesser_to_right(node):
    n = node
    while n.next:
        if n.data < node.data:
            return True
        n = n.next
    return False


def partition(node, key):
    n = node
    while n.next:
        if n.data >= key and check_if_lesser_to_right(n):
            move_to_end(n)
        else:
            n = n.next
        

if __name__ == '__main__':
        
    a = Node.list_to_link([2,8,3,4,5,99,5,6,3])

    print(a)
    partition(a, 5)
    print(a)




