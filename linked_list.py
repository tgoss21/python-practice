from node import Node

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)

    def get_head(self):
        return self.head

    def insert_node(self,value):
        new_node = Node(value)
        new_node.set_next_node(self.head)
        self.head = new_node
    
    def stringly_list(self):
        str1 = ''
        curr_node = self.get_head()
        while curr_node:
            if curr_node.get_value != None:
                str1 += str(curr_node.get_value()) + ', '
                curr_node = curr_node.get_next_node()
        return str1

    def remove_node(self, value):
        curr_node = self.get_head()
        if curr_node.get_value() == value:
            self.head = curr_node.get_next_node()
        else:
            while curr_node:
                next_node = curr_node.get_next_node()
                if next_node.get_value() == value:
                    curr_node.set_next_node(next_node.get_next_node())
                    curr_node = None
                else:
                    curr_node = next_node
        return curr_node

    def swap_nodes(self, input_list, val1, val2):
        print(f'Swapping {val1} with {val2}')
#1. Instantiate varibles
        node1_prev = None
        node2_prev = None
        node1 = input_list.head
        node2 = input_list.head

        if val1 == val2:
            print("Elements are the same - no swap needed")
        return

#2. find matching and preceding nodes
        while node1 is not None:
            if node1.get_value() == val1:
              break
        node1_prev = node1
        node1 = node1.get_next_node()

        while node2 is not None:
            if node2.get_value() == val2:
                break
        node2_prev = node2
        node2 = node2.get_next_node()

        if (node1 is None or node2 is None):
            print("Swap not possible - one or more element is not in the list")
        return
    
#3. Update preciding pointerss
        if node1_prev is None:
            input_list.head_node = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev is None:
            input_list.head_node = node1
        else:
            node2_prev.set_next_node(node1)

#4. update next node pointers
        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)



            

ll = LinkedList(5)
for i in range(10):
    ll.insert_node(i)

print(ll.stringly_list())
ll.remove_node(5)
ll.remove_node(5)
print(ll.stringly_list())
ll.swap_nodes(ll,2,4)
print(ll.stringly_list())
        

