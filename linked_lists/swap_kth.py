
    
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

def swapNodes( pList,  iK):
	if not pList or iK <= 0: return
	# we need to get pointers to:
	# 1. nodes before Kth node, and n-kth node
	# 2. kth node and n-kth node
	# and then, we need to swap the nodes
	# we will use prev1, node1 for kth node
	# and prev2, node2 for n-kth node
	prev1 = prev2 = None
	head = pList
	node1 = node2 = tmp = head 
	# determine Kth node from the beginning
	while iK-1 and tmp:
		prev1 = tmp
		tmp = tmp.next 
		iK -= 1
	# at this point, tmp is at kth node
	node1 = tmp
	# now, to find n-kth node, we start moving node2 and tmp together
	# until tmp reaches the end
	# at the point, node2 will be pointing at n-kth node
	while tmp and tmp.next:
		prev2 = node2
		node2 = node2.next
		tmp = tmp.next

	# swap nodes
	if not node1 or not node2: return
	# prev1 can be null when first node is being swapped
	if not prev1:
		head = node2
	else:
		prev1.next = node2
	# allows symmetrical case i.e., k is > n-k
	if not prev2:
		head = node1
	else:
		prev2.next = node1

	tmp = node1.next 
	node1.next = node2.next
	node2.next = tmp
	return head

_pList = None
_iK = 2
for n in [11,4,2]: 
	print 'asdf'
	_pList = _insert_node_into_singlylinkedlist(_pList, n);


res = swapNodes(_pList, _iK);

while (res != None):
    print res.val,
    res = res.next;
print