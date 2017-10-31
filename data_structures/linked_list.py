class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        """Time complexity: O(1)"""
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def remove(self, val):
        """Time complexity: O(N)"""
        prev, curr = self.find(val)
        if curr is None:
            return False
        if prev is None:
            self.head = curr.next
        else:
            prev.next = curr.next
        self.size -= 1
        return True

    def contains(self, val):
        """Time complexity: O(N)"""
        _, curr = self.find(val)
        return curr is not None

    def find(self, val):
        """Time complexity: O(N)"""
        prev, curr = None, self.head
        while curr:
            if curr.val == val:
                return prev, curr
            prev, curr = curr, curr.next
        return prev, curr

    def print_list(self):
        curr = self.head
        while curr:
            print curr.val,
            curr = curr.next
        print

    def get_size(self):
        return self.size


class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.print_list()
assert llist.contains(2)
print "After removing 2"
llist.remove(2)
llist.print_list()
assert not llist.contains(2)
assert llist.get_size() == 3
