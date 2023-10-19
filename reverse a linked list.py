def reverse(head):
    prev = None
    cur = head
    nxt = head.next
    while cur != None:
        nxt = cur.next
        cur.next = prev
        prev = cur 
        cur = nxt 
    head = prev
    return head
