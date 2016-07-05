from ex4 import MyQueue
from time import time



class AnimalShelter:

	def __init__(self):
		self.dog_q = MyQueue()
		self.cat_q = MyQueue()


	def enqueue_cat(self, name):
		self.cat_q.add((name, time()))


	def enqueue_dog(self, name):
		self.dog_q.add((name, time()))


	def dequeue_any(self):

		if self.dog_q.is_empty() and self.cat_q.is_empty():
			return 'There are no more animals.'
		if self.dog_q.is_empty():
			return self.cat_q.remove()
		if self.cat_q.is_empty():
			return self.dog_q.remove()

		if self.dog_q.peek()[1] < self.cat_q.peek()[1]:
			return self.dog_q.remove()
		elif self.dog_q.peek()[1] > self.cat_q.peek()[1]:
			return self.cat_q.remove()


	def dequeue_cat(self):
		return self.cat_q.remove()


	def dequeue_dog(self):
		return self.dog_q.remove()


	def __str__(self):
		return 'Cats: {}\nDogs: {}'.format(str(self.cat_q), str(self.dog_q))



if __name__ == '__main__':
	s = AnimalShelter()
	s.enqueue_dog('Rex')
	s.enqueue_dog('Timmy')
	s.enqueue_cat('Fluffy')
	s.enqueue_cat('Puffy')

