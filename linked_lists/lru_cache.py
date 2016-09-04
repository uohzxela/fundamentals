class Node(object):

    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0
        self.hashmap = {}

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.hashmap:
            node = self.hashmap[key]
            self.delete(node)
            self.insert(node)
            return node.val
        else:
            return -1
        
    def set(self, key, val):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.hashmap:
            self.insert(Node(key, val))
        else:
            node = self.hashmap[key]
            node.val = val
            self.delete(node)
            self.insert(node)
    
    def insert(self, node):
        if self.size == self.capacity:
            self.delete(self.tail)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.hashmap[node.key] = node
        self.size += 1
        
    def delete(self, node):
        if not node:
            return
        if node == self.head: 
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        # very important!
        node.prev = None
        node.next = None
        del self.hashmap[node.key]
        self.size -= 1


c = LRUCache(2)
c.set(2,1)
c.set(1,1)
c.set(2,3)
c.set(4,1)
print c.get(1)
print c.get(2)