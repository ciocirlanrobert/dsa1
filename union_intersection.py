class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    
    def make_list(self):
        llist = []
        current_node = self.head
        
        while current_node:
            llist.append(current_node.value)
            current_node = current_node.next
            
        return llist
    


def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1
    
def union(llist_1, llist_2):
    if llist_1.head == None and llist_2.head == None:
        return None
    
    llist_1 = set(llist_1.make_list())
    llist_2 = set(llist_2.make_list())
    
    new_ll = LinkedList()
    for elem in llist_1 | llist_2:
        new_ll.append(elem)
        
    return new_ll
    

def intersection(llist_1, llist_2):
    llist_1 = set(llist_1.make_list())
    llist_2 = set(llist_2.make_list())
    
    new_ll = LinkedList()
    for elem in llist_1 & llist_2:
        new_ll.append(elem)
    
    if new_ll.head is None:
        return None
    return new_ll
        
    
# Test case 1
print("Test case 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2)) # expected 1,2,3,4,6,9,11,21,32,35,65 not necessary in this order
print(intersection(linked_list_1, linked_list_2)) # expected 4 6 21 not necessary in this order
print()

# # Test case 2
print("Test case 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
    
print (union(linked_list_3,linked_list_4)) # expected 1,2,3,4,6,7,8,,9,11,21,23,35,65 not necessary in this order
print (intersection(linked_list_3,linked_list_4))# expected the empty set
print()

# # Test case 3
print("Test case 3")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)
    
print (union(linked_list_5,linked_list_6)) # expected the empty set
print (intersection(linked_list_5,linked_list_6)) # expected the empty set
print()

# # Test case 4
print("Test case 4")
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [1,2,3,4]
element_2 = [1,2,3,4]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)
    
print (union(linked_list_7,linked_list_8)) # expected 1,2,3,4 not necessary in this order
print (intersection(linked_list_7,linked_list_8)) # expected 1,2,3,4 not necessary in this order

