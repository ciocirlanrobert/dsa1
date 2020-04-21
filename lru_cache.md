For this problem, as the requirement is for the set()/get() functions to be O(1), I used a Doubly Linked List and a hash-map where I saved the (key,value) pair and the next and previous node, for a current node. We know that accesing a key in a dictionary is O(1) and the Doubly Linked List allows us to insert and remove the nodes in O(1) because we know the nodes next to a specific node, that's why I used these data structures.

Time Complexities:
    As required:
        => get() O(1)
        => set() O(1)

Space Complexities:
	=> O(n)

