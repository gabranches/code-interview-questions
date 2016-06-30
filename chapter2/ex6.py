from single_linklist import Node


def reverse(node):
    n = node
    rev = Node(node.data)
    n = node.next
    while n:
        rev = rev.head(n.data)
        n = n.next
    return rev


def compare(n1, n2):
    if n1.data != n2.data:
        return False
    if n1.next == None:
        return True
    return compare(n1.next, n2.next)
        

def is_palindrome(node):
    return compare(node, reverse(node))


if __name__ == '__main__':

    a = Node.list_to_link([1,2,3,3,2,1])
    print(is_palindrome(a))