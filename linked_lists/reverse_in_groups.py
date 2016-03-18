# Enter your code here. Read input from STDIN. Print output to STDOUT

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def createList(arr):
    head = curr = Node(arr[0])
    for i in xrange(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    return head

def printList(curr):
    while curr:
        print curr.val,
        curr = curr.next
    print
    
def reverse(head, k):
    prev, curr, count = None, head, 0
    while curr and count < k:
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next
        count += 1
    #      head, tail, next
    return prev, head, curr
    
def reverseInGroups(head, k):
    if not head.next: return head
    curr, t = head, None
    while curr:
        prev_t = t
        h, t, nxt = reverse(curr, k)
        t.next = nxt 
        if prev_t: prev_t.next = h
        else: head = h 
        curr = nxt
    return head
    
h = createList([1,2,3,4,5,6,7,8])
printList(h)
h = reverseInGroups(h, 10)
printList(h)