def deleteNode(head, position):
    if position ==0:
        head =head.next
    else:
        temp = head 
        count = 1
        while temp != None and count < position:
            temp = temp.next
            count +=1
        temp.next = temp.next.next
    return head
