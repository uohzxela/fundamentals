from collections import defaultdict
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.table = defaultdict(lambda: None)
    
    # for debugging
    def printList(self):
        curr = self.head.next
        while curr:
            print curr.value, 
            curr = curr.next
        print
        
    def delete(self, node):
        if node == self.head: 
            self.head = node.next
        prev = node.prev
        if prev:
            prev.next = node.next
        if node.next:
            node.next.prev = prev
        else:
            self.tail = prev
            
    def addToBeginning(self, node):
        if not self.tail: self.tail = node
        node.next = self.head
        if node.next:
            node.next.prev = node
        node.prev = None
        self.head = node

    def evict(self):
        if not self.tail: return
        key = self.tail.key
        self.delete(self.tail)
        self.table[key] = None
        self.size -= 1
        
    def get(self, key):
        """
        :rtype: int
        """
        if not self.table[key]: return -1
        node = self.table[key]
        self.delete(node)
        self.addToBeginning(node)
        return node.value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if not self.table[key]:
            new_node = Node(key, value)
            self.addToBeginning(new_node)
            self.table[key] = new_node
            self.size += 1
            if self.size > self.capacity:
                self.evict()
        else:
            node = self.table[key]
            node.value = value
            self.delete(node)
            self.addToBeginning(node)

c = LRUCache(2)
c.set(2,1)
c.set(1,1)
c.set(2,3)
c.set(4,1)
print c.get(1)
print c.get(2)