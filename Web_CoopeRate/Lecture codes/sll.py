class Node:
    def __init__(self, element = None, next = None):
        self.element = element
        self.next = next 
        
class SingleLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return (self._size == 0)
    def insertAtFirst(self, e):
        newNode = Node(e, self._head)
        self._head = newNode
        self._size += 1
        return newNode
    def __str__(self):
        result = "Head-->"
        currNode = self._head
        while currNode is not None:
            result += str(currNode.element) + "-->"
            currNode = currNode.next
        return(result + "None")
    def even_odd_sort(self):
        even_tail, odd_head, even_head, odd_tail  = None, None, None, None
        currNode = self._head
        while currNode != None:
            currNode_next = currNode.next
            currNode.next = None
            if currNode.element % 2 == 0:
                if even_head == None:
                    even_head = currNode
                    even_tail = currNode
                else:
                    even_tail.next = currNode
                    even_tail = currNode
            else:
                if odd_head == None:
                    odd_head = currNode
                    odd_tail = currNode
                else:
                    odd_tail.next = currNode
                    odd_tail = currNode
            currNode = currNode_next
        self._head = even_head
        even_tail.next = odd_head
if __name__ == "__main__":
    sll = SingleLinkedList()
    for x in range(10):
        sll.insertAtFirst(x)
    print(sll)
    sll.even_odd_sort()
    print(sll)
         

