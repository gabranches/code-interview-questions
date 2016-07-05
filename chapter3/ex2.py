import sys
sys.path.insert(0, '.')

from data_structs import Stack


class MinStack(Stack):    

    def __init__(self, list=None):
        self.min = None
        Stack.__init__(self, list)

    
    def push(self, item):
        self.stack.append(item)
        self._set_min(item)


    def _set_min(self, item):
        if self.min:
            if item < self.min:
                self.min = item
        else:
            self.min = item


if __name__ == "__main__":
    
    s = MinStack([5,4,1,3,2])    
    print(s.min)
    s.push(-3)
    print(s.min)