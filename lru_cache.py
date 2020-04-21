class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None
        
    def __str__(self):
        return "({},{})".format(self.key, self.value)

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.hash_map = {}
        self.current_size = 0
        
        self.head = None
        self.tail = None
    
    def move_tail(self, node):
        if self.current_size == 1:
            self.tail = node
            self.hash_map[self.tail.key] = self.tail
        else:
            node.next.previous = None
            self.tail = node.next
            self.hash_map[self.tail.key] = self.tail
            self.head.next = node
            self.hash_map[self.head.key] = self.head
            node.previous = self.head
            node.next = None
            self.hash_map[node.key] = node
            self.head = node
    
            
    
            
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.hash_map: # if the key is in the hash
            node = self.hash_map[key] # take the node
            if self.head != node: # if the node is the head just return the value, if not we need to move it as the head
                if self.tail == node:# if the node is the tail, make the tail the node's next and move the node as the head
                    self.move_tail(node)
                else: # if the node is in-between two nodes, make the connection between those nodes, then move the node as the head
                    node.next.previous = node.previous
                    node.previous.next = node.next
                    self.hash_map[node.next.key] = node.next
                    self.hash_map[node.previous.key] = node.previous
                    
                    self.head.next = node
                    self.hash_map[self.head.key] = self.head # every time save the new changes in the hash-map
                    node.previous = self.head
                    node.next = None
                    self.hash_map[node.key] = node
                    self.head = node
                    
            return node.value
        
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        
        if key not in self.hash_map:# if the key is not in the hash, add it
            new_node = Node(key, value)
            if self.current_size < self.capacity:# if the still have space, we just add it, don't need to pop any element
                if self.head == None:
                    self.head = new_node
                    self.tail = new_node
                    self.hash_map[key] = new_node
                else:
                    self.head.next = new_node
                    new_node.previous = self.head
                    self.hash_map[self.head.key] = self.head
                    self.head = new_node
                    self.hash_map[key] = new_node
                    
                self.current_size += 1
            else:# if the cache is full we remove the tail then add the new node as the head
                if self.current_size == 1:
                    self.tail, self.head = new_node, new_node
                    self.hash_map[self.tail.key], self.hash_map[self.head.key] = new_node, new_node
                else:
                    removed_node = self.tail
                    del self.hash_map[removed_node.key]
                    self.tail = removed_node.next
                    self.tail.previous = None
                    self.hash_map[self.tail.key] = self.tail
                
                    self.head.next = new_node
                    new_node.previous = self.head
                    self.hash_map[self.head.key] = self.head
                    self.head = new_node
                    self.hash_map[key] =  new_node
        else:# if the key is already in the cache update the node with the new value and move it as the head of the list
            if self.current_size == 1:
                node = self.hash_map[key]
                node.value = value
                self.hash_map[key] = node
            else:
                node = self.hash_map[key]
                node.value = value
            
                if node == self.tail:# the tail case from get()            
                    self.move_tail(node)
                else:#the in-between case from get()
                    node.next.previous = node.previous
                    node.previous.next = node.next
                    self.hash_map[node.next.key] = node.next
                    self.hash_map[node.previous.key] = node.previous
                    
                    self.head.next = node
                    self.hash_map[self.head.key] = self.head
                    node.previous = self.head
                    node.next = None
                    self.hash_map[node.key] = node
                    self.head = node
                
            
    
    def print_list(self):
        node = self.head
        string = ""
        while node:
            string += str(node.value) + "->"
            node = node.previous
        
        return string

#Test case 1
print("Test case 1")
our_cache = LRU_Cache(5)

value = our_cache.get(6)     # returns -1
print(value)                

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

value = our_cache.get(1)     # expected 1
print(value)

value = our_cache.get(2)     # expected 2
print(value)

value = our_cache.get(9)     # expected -1 because 9 is not present in the cache
print(value)


our_cache.set(5, 5)
our_cache.set(6, 6)

value = our_cache.get(3)     # expected -1 because the cache reached it's capacity and 3 was the least recently used entry
print(value)

our_cache.set(5, 100)        # set a new value for the node with key 5 which is already in the cache
value = our_cache.get(5)     # expected 100
print(value)

value = our_cache.get(1)     #expected 1 because this should not be popped in the set method since we just replace it
print(value)
print()

#Test case 2
print("Test case 2")
our_cache = LRU_Cache(1)

our_cache.set(1, 1)
value = our_cache.get(1) #expected 1
print(value)

our_cache.set(1,5)
value = our_cache.get(1)#expected 5
print(value)

value = our_cache.get(5) #expected -1
print(value)

our_cache.set(2,2)
value = our_cache.get(2)#expected 2
print(value)

print(our_cache.current_size)#expected 1
print()

#Test case 3
print("Test case 3")
our_cache = LRU_Cache(10)

our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(1,1)
our_cache.set(3,3)
our_cache.set(4,4)
our_cache.set(5,5)

print(our_cache.print_list()) #expected 5->4->3->1->2 because we set 1 again and moved it at the top

value = our_cache.get(1)#expected 1
print(value)

value = our_cache.get(2)#expected 2
print(value)

value = our_cache.tail
print(value)#expected (3,3) as this is the least recently used node
