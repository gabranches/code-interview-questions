from data_structs import BinaryTreeNode
from timeit import default_timer as timer


def main():
    a = BinaryTreeNode(10)
    a.add(5)
    a.add(7)
    a.add(3)
    a.add(12)
    print(a)
	


if __name__ == '__main__':
	start = timer()
	main()
	end = timer()
	print((end - start)*1000)  