from utils import *

class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

def balance_(h, n):
	if n <= 0: return None, h
	left_child, curr_root = balance_(h, n/2)
	curr_root.left = left_child
	right_child, next_root = balance_(curr_root.next, n-n/2-1)
	curr_root.right = right_child
	return curr_root, next_root

def findLen(curr):
	count = 0
	while curr:
		count += 1
		curr = curr.next
	return count

def balance(h):
	n = findLen(h)
	return balance_(h, n)[0]


printList(head)
printTree(balance(head))