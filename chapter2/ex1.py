from double_linklist import Node

def remove_dups(n):
    while n:
        runner = n.next
        while runner:
            if runner.data == n.data:
                runner.remove_node()
            runner = runner.next
        n = n.next 

if __name__ == '__main__':
    
    ll = Node(1)
    ll.append_tail(2)
    ll.append_tail(1)
    ll.append_tail(3)
    ll.append_tail(3)
    ll.append_tail(3)
    ll.append_tail(4)
    ll.append_tail(5)
    ll.append_tail(3)
    ll.append_tail(5)
    remove_dups(ll)
    print(ll)

