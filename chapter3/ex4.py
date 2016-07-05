import sys
sys.path.insert(0, '.')

from data_structs import Stack


class MyQueue:

	def __init__(self):
		self.queue = Stack()


	def add(self, item):
		self.queue.push(item)


	def remove(self):
		temp = self.queue.reverse()
		res = temp.pop()
		self.queue = temp.reverse()
		return res


	def peek(self):
		temp = self.queue.reverse()
		res = temp.peek()
		self.queue = temp.reverse()
		return res


	def is_empty(self):
		return self.queue.is_empty()


	def __str__(self):
		return str(self.queue)


if __name__ == '__main__':

	q = MyQueue()
	q.add(1)
	q.add(2)
	q.add(3)
	print(q.remove())
	print(q)
	print(q.peek())
	print(q)
	print(q.is_empty())
