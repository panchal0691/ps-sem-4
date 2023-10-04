def insertNodeAtHead(head, data):
    node = SinglyLinkedListNode(data)
    if head != None:
        node.next = head
    return node
   
