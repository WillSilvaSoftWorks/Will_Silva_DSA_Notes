'''
@author William Silva
@version 10.13.24
Description: This file is a linked list with linked list properties and methods.
'''

'''
@param value: the value of the head of the linked list
This class will used to create instances of a linked list 
A linked list will have the properties of nodes, a head and tail pointer,
and it additionally tracks the size of the linked list.
'''
class LinkedList:
    def __init__(self,value):
        # Initializes a new linked list with a single node containing the given value.
        new_node = Node(value)
        # Head and Tail pointers, head points to the first node and 
        # tail points to the last node in the list.
        self.head = new_node
        self.tail = new_node
        # Tracks how many nodes are in the list.
        self.size = 1

    # Prints all the nodes in the linked list.
    def print_list(self):
            curr = self.head
            while curr:
                if curr.next == None:
                    print("(",curr.value,")", end = "\n")
                    return 
                print("(",curr.value,")->", end = "")
                curr = curr.next

    '''
    @param value: value of node 
    @returns True when node is appended 
    Adds a new node to the end of the list
    '''
    def append(self,value):
        linked_list_node = Node(value)
        # if list is empty, set h&t pointers to new list node.
        if self.head is None:
             self.head = linked_list_node
             self.tail = linked_list_node
        # if list is not empty, add node to end of list. Change tail pointer
        else:
            self.tail.next = linked_list_node
            self.tail = linked_list_node
        self.size += 1 
        return True 
    
    # Removes node at the end of the linked list 
    def pop(self):
        #Check if there is nodes in the list
        if self.size == 0:
            return None
        temp = self.head
        pre = self.head
        # Iterates through list to fine pre and tail
        while temp.next:
            pre = temp
            temp = temp.next
        # Removes last node 
        self.tail = pre
        self.tail.next = None
        self.size -= 1
        # If there isn't anymore node set to None 
        if self.size == 0:
            self.head = None
            self.tail = None
        return temp

    '''
    @param value: value of new node
    Adds a new node to the start of the list 
    '''
    def prepend(self,value):
        # Creates new node
        linked_list_node = Node(value)
        if self.size == 0:
            self.head = linked_list_node
            self.tail = linked_list_node
        else:
            # New node points to head
            linked_list_node.next = self.head
            # Head pointer points to new node. Making a new head
            self.head = linked_list_node
        self.size += 1
        return True
    
    # Removes head node of the linked list
    def pop_first(self):
        # if linked list is empty return nothing
        if self.size == 0:
            return None
        
        # Create a temp node then set head to next node. Remove old head node.
        temp = self.head
        self.head = self.head.next 
        temp.next = None
        self.size -= 1
        # if no nodes after pop set tail to None. Then linked list is empty.
        if self.size == 0:
            self.tail = None
        return temp
    '''
     @param index: the node that will be retrieved
     Gets the value of the node at the given index.
    ''' 
    def get(self, index):
        if index >= self.size or index < 0:
            return None 
        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr
            curr = curr.next
            i += 1
        return None
    
    '''
     @param index: the node that will be retrieved
     @param value: the value that will replace the node's value.
     Sets the node at the given index to a new value.
    ''' 
    def set(self, index, value):
        if index >= self.size or index < 0:
            return None 
        i = 0 
        curr = self.head 
        while curr:
            if i == index:
                curr.value = value
            curr = curr.next
            i += 1
        return None 
    
    '''
     @param index: the node that will point to the new node
     @param value: the value of the new node to be inserted
     Returns the value of the node at the given index.
    ''' 
    def insert(self, index, value):
        if index >= self.size or index < 0:
            print("Cannot insert, index is less than 0 or bigger than list size.")
            return None 
        i = 0
        new_node = Node(value)
        curr = self.head 
        while curr:
            if i == index:
                temp = curr.next
                curr.next = new_node
                new_node.next = temp
                self.size += 1
            curr = curr.next
            i += 1
        return None
    
    '''
    @param index: position of node that is to be removed
    Removes a node at a given index in a linked list.
    '''
    def remove(self, index):
        if index < 0 or index >= self.size:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.size - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.size -= 1
        return temp
    
    # Reverses linked list
    def reverse(self):
        curr = self.head
        # Sets head pointer to point at tail. 
        self.head = self.tail
        # Sets tail pointer to old head node.
        self.tail = curr
        # Pointer that save next node. curr will be these node after reversal.
        curr_next = curr.next
        temp = None
        i = 0
        # Goes through each node and sets pointer to temp node.
        while i < self.size:
            curr_next = curr.next
            curr.next = temp
            temp = curr
            curr = curr_next
            i += 1
        
# Node constructor, create a new instance of a node. 
# @param value: any data type
class Node:
    def __init__(self,value):
        # Initializes a node with the given value and sets the next pointer to None.
        self.value = value
        self.next = None

'''
Creates new instance of a linked list and performs various operations.
Runs as main when file is ran by python
To run input 'python3 LinkedList.py'
Output:
( 3 )->( 20 )->( 12 )->( 1 )->( 10 )->( 5 )
( 5 )->( 10 )->( 1 )->( 12 )->( 20 )->( 3 )
'''    
if __name__ == '__main__':
    linked_list = LinkedList(10)
    for i in range(5):
        linked_list.append(i)
    linked_list.set(1,100)
    linked_list.set(1,-1)
    linked_list.insert(3,20)
    linked_list.insert(2,12)
    linked_list.pop()
    linked_list.prepend(5)
    linked_list.remove(5)
    linked_list.remove(2)
    linked_list.reverse()
    linked_list.print_list()
    linked_list.reverse()
    linked_list.print_list()