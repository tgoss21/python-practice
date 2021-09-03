from node import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size

    def enqueue(self, value):
        if self.has_space() == True:
            item_added = Node(value)
            print("Adding: " + str(item_added.get_value()) + "!")

            if self.is_empty():
                self.head = item_added
                self.tail = item_added
            else:
                self.tail.set_next_node(item_added)
                self.tail = item_added
                self.size += 1
        else:
            print("Sorry, no more room!")


    def dequeue(self):
        if self.has_space():
            item_removed = self.head
            print("Removing: " + str(item_removed.get_value())+ "!")
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_removed.get_value()
        else:
            print("Queue empty!")

    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            print("Empty Queue!")
    

    def get_size(self):
        if self.size > 0:
            return self.size

    def has_space(self):
        if self.max_size == None:
          return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        return self.get_size == 0


names = Queue(10)
names.enqueue("Tracy")
names.enqueue("Linda")
names.enqueue("Danielle")
names.enqueue("Tamra")
