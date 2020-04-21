For this algorithm I used the Intersection and Union of sets, considering not to take duplicate elements.

Time Complexities:
    => make_list O(n)
    => set union (|) O(len(llist_1) + len(llist_2))
    => set intersection (&) O(min(len(llist_1), len(llist_2))
    => def union() O(len(llist_1) + len(llist_2))
    => def intersection() O(min(len(llist_1), len(llist_2))

Space Complexities:
    Let n1,n2 = number of elements of the first respectively second initial linked list.
    First ll = O(n1)
    Second ll = O(n2)
    Intersection : Two sets of O(n1) respectively O(n2) + a LinkedList of O(m) where m = number of common elements between the initial linked lists.
    Two sets of O(n1) respectively O(n2) + a LinkedList of O(m) where m = number of the elements in the union
