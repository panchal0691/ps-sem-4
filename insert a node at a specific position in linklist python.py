def insertNodeAtPosition(head, data, position):
    node =SinglyLinkedListNode(data)
    if head == None:
        head = node
    else:
        temp = head
        count =1
        
        while temp != None and count < position:
            temp = temp.next
            count +=1
        node.next = temp.next
        temp.next = node
    return head
