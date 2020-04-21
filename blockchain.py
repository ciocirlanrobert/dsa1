import hashlib
from time import gmtime, strftime

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class Block:
    def __init__(self, timestamp, data, index, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
    
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp) + str(self.data)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

    def __str__(self):
        return "index:{}, timestamp: {}, data:{}, hash:{}, previous hash:{}\n".format(self.index, self.timestamp, self.data, self.hash, self.previous_hash)

class Blockchain:
    def __init__(self):
        self.head = LinkedListNode(Block(strftime("%H:%M %m/%d/%Y", gmtime()), "general", 0, 0))
        self.size = 1

    @property
    def head_value(self):
        return self.head.value
    
    def add(self, block):
        if block.previous_hash != self.head_value.hash:
            return

        node = LinkedListNode(block)
        node.next = self.head
        self.head = node
        self.size += 1
        
    def get_by_index(self, index):
        if index < 0:
            return None

        current_node = self.head
        while current_node:
            if current_node.value.index == index:
                return current_node.value
            current_node.next = current_node
        

    def get_size(self):
        return self.size

    def __str__(self):
        string = ""
        current_node = self.head
        while current_node:
            string += str(current_node.value)
            if current_node.next:
                string += ' ' * 5 + '|\n'
                string += ' ' * 5 + '|\n'
            current_node = current_node.next
        return string




blockchain = Blockchain()
sep = 100 * '=' + "\n"


print("Test case 1")
print(blockchain)
print("Size: {}".format(blockchain.get_size()))
print(sep)


# Test case 2: expected size 4. 3 transaction bocks are there
print("Test case 2")
block = Block(strftime("%H:%M %m/%d/%Y", gmtime()),"first data",blockchain.head_value.index + 1, blockchain.head_value.hash)
blockchain.add(block)

block = Block(strftime("%H:%M %m/%d/%Y", gmtime()),"second data",blockchain.head_value.index + 1,blockchain.head_value.hash)
blockchain.add(block)

block = Block(strftime("%H:%M %m/%d/%Y", gmtime()),"third data",blockchain.head_value.index + 1,blockchain.head_value.hash)
blockchain.add(block)

print(blockchain)
print("Size: {}".format(blockchain.get_size()))
print(sep)


#Test case  3: Expected: size 4. Block with "fourth data" wasn't added
print("Test case 3")
block = Block(strftime("%H:%M %m/%d/%Y", gmtime()),"fourth data",blockchain.head_value.index + 1,"tg4398thq3498ht8qgh8gheh88ifiewir3qbradslfna")
blockchain.add(block)

print(blockchain)
print("Size: {}".format(blockchain.get_size()))

#Test case 4: Expected: block with "third"
print("Test case 4")
print(blockchain.get_by_index(3))
