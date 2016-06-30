from single_linklist import Node


def link_to_num(node, reverse=False):
    n = node
    num = ''
    while n:
        if reverse:
            num += str(n.data)
        else:
            num = str(n.data) + num
        n = n.next
    return int(num)


if __name__ == '__main__':
      
    a = Node.list_to_link([6,1,7])
    b = Node.list_to_link([2,9,5])

    c = link_to_num(a, True) + link_to_num(b, True)
    c = [int(x) for x in list(str(c))]

    print(Node.list_to_link(c))


