class Heap(object):
    """
    - Info: Class module that implements a heap structure and it's methods

    """

    # Maximum heap size
    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0] * Heap.HEAP_SIZE
        self.current_position = -1

    def insert(self, item):
        """
        - Info: Method that inserts elements into the heap.
        - @param: item: Element to be inserted.
        """

    	if self.isFull():
    		print("Heap is full...")
    		return

    	self.current_position += 1
    	self.heap[self.current_position] = item
    	self.fixUp(self.current_position)

    def fixUp(self, index):
    	"""
        - Info: Fixes the parent-child order from the leaves to the root.
        - @param: index: Element that is out of order.

        parent_index = int((index - 1) / 2)
        """

        while parent_index >= 0 and self.heap[parent_index] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parent_index]
            self.heap[parent_index] = temp

            index = parent_index
            parent_index = int((index - 1) / 2)

    def fixDown(self, index, upto):
        """
        - Info: Fixes the parent-child order from the root to the leaves.
        - @param: index: Element that is out of order.
        - @param: upto: 

        """
        
        if upto < 0:
            upto = self.current_position

        while index <= upto:
            
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child <= upto:

                child_to_swap = None

                if right_child > upto:
                    child_to_swap = left_child
                else:
                    if self.heap[left_child] > self.heap[right_child]:
                        child_to_swap = left_child
                    else:
                        child_to_swap = right_child

                if self.heap[index] < self.heap[child_to_swap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[child_to_swap]
                    self.heap[child_to_swap] = temp
                else:
                    break

                index = child_to_swap
            else:
                break

    def heapSort(self):
        
        """
        - Info: Executes a sorting algorithm in O(N logN) complexity.
        """

        for i in range(0, self.current_position + 1):
            temp = self.heap[0]
            print ("%d" % temp)
            self.heap[0] = self.heap[self.current_position - i]
            self.heap[self.current_position - i] = temp
            self.fixDown(0, self.current_position - i)
   
    def getMax(self):
        """
        - Info: Provides the maximum/root element and restructure the heap.
        - @return: result: Highest value element.
        """
    	result = self.heap[0]
    	self.current_position -= 1
    	self.heap[0] = self.heap.current_position
    	del self.heap[current_position + 1]
    	self.fixDown(0, -1)
    	return result

    def getMin(self):
    	pass


    def isFull(self):
        """
        - Info: Vrifies if the heao structure is full
        - @return: Bool: True if heap is full or false otherwise
        """
    	if self.current_position == HEAP_SIZE:
    		return True
    	else:
    		return False


       