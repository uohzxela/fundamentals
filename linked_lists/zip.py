
class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

def _insert_node_into_singlylinkedlist(head, val):
    if head == None:
        head = LinkedListNode(val)
    else:
        end = head;
        while end.next != None:
            end = end.next
        node = LinkedListNode(val)
        end.next = node
    return head

def printList(curr):
	while curr:
		print curr.val,
		curr = curr.next
	print

def  Zip( pList):
    if not pList: return None
    h = curr = pList
    s = []
    while curr:
        s.append(curr)
        curr = curr.next
    t = s.pop()
    while t != h and t != h.next:
        next_h = h.next
        h.next = t
        t.next = next_h
        h = next_h
        t = s.pop()
    t.next = None
    return pList

def merge(h1, h2):
	p1 = h1
	p2 = h2
	while p2:
		p1_next = p1.next
		p2_next = p2.next
		p1.next = p2
		p1 = p1_next
		p2.next = p1
		p2 = p2_next 

def zip2(pList):
	if not pList: return None
	count = 1
	curr = pList
	while curr:
		curr = curr.next
		count += 1
	curr = pList
	prev = None
	mid = count/2
	count = 1
	print 'mid:', mid
	while curr:
		curr_next = curr.next
		if count == mid: curr.next = None
		if count > mid:
			# print 'asdf'
			curr.next = prev
			prev = curr

		curr = curr_next 
		count += 1
	merge(pList, prev)
	printList(pList)
	# printList(prev)


_pList = None
inputList = [1,2,3,4,5,6]
for i in inputList: 
    _pList_item = i 
    _pList = _insert_node_into_singlylinkedlist(_pList, _pList_item)


# res = Zip(_pList);
zip2(_pList)
# printList(res)