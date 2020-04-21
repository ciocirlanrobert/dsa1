For this problem I used a min heap to make the Huffman Tree. I used the built-in heapq.
Encoding: I recursively traverse the heap in order to find the code for every letter and for that I also used a Hash map ( I did a bit of research because I didn't know how to do this at once and I found out this methoud would work nicely).

Time Complexities:
    => creating the tree O(n*logn) since creating the min heap is O(n*logn)
    => encoding the data O(n) since I only traverse the tree once
    => Let n = length of the data, m = number of unique letters = > Decoding the data O(n*logm)

Space Complexities:
    => Building the Tree: Let n = number of unique letters => Space Compl. O(n)
    => Hash Map: O(n)	

