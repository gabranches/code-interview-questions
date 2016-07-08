import sys
sys.path.insert(0, '.')

from data_structs import Stack


def find_max(stack):
	max = None
	temp = Stack()
	while not stack.is_empty():
		if not max:
			max = stack.pop()
		else:
			next = stack.pop()
			if next >= max:
				temp.push(max)
				max = next
			else:
				temp.push(next)
	stack = temp
	return (max, temp)


def sort_recursive(old, new):
	if old.is_empty():
		return new
	max = find_max(old)
	new.push(max[0])
	return sort_recursive(max[1], new)


def sort_stack(stack):
	new = Stack()
	return sort_recursive(stack, new)



if __name__ == '__main__':
		
	a = Stack([6,5,4,3,2,1])
	print(sort_stack(a))



