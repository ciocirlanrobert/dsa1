import sys
from heapq import heapify, heappop, heappush
from itertools import groupby


class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def check(self, node):
        return hasattr(node, "freq")

    def __eq__(self, node):
        if not self.check(node):
            return NotImplemented
        else:
            return self.freq == node.freq

    def __lt__(self, node):
        if not self.check(node):
            return NotImplemented
        else:
            return self.freq < node.freq    


def process(data):
    if data is None or len(data) == 0:
        return None
    
    heap = [Node(value, len(list(group))) for value, group in groupby(sorted(data))]
    heapify(heap)

    while len(heap) > 1:
        
        left = heappop(heap)
        right = heappop(heap)
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heappush(heap, new_node) 

    return heap[0]


def huffman_encoding(data):
    codes = {}
    node = process(data)
    _huffman_encoding(node, codes, "")
    
    encoded = ""
    for char in data:
        encoded += codes[char]
    
    return encoded, node


def _huffman_encoding(node, codes, string):
    if node == None:
        return
    delattr(node, 'freq')

    if node.value:
        if len(string) == 0:
            string = "0"
        codes[node.value] = string
    else:
        delattr(node, 'value')
        _huffman_encoding(node.left, codes, string + "0")
        _huffman_encoding(node.right, codes, string + "1")


def huffman_decoding(data, tree):
    current_node = tree
    s = ""
    
    for char in data:
        if char == '0' and current_node.left:
            current_node = current_node.left
            
        elif current_node.right:
            current_node = current_node.right
            
        if current_node.left is None and current_node.right is None:
            s += str(current_node.value)
            current_node = tree
            
    return s

if __name__ == "__main__":
    codes = {}
    

# Test case 1
    print('Test case 1')
    a_great_sentence = "Huffman"

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Test case 2
    print('Test case 2')
    a_great_sentence = "a"

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Test case 3
    print('Test case 3')
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
#Test_case 4
    print('Test case 4')
    a_great_sentence = "aaaaaaaaaaaaaaa"

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
