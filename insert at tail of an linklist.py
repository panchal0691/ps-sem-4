def compare_lists(llist1, llist2):
    head1 = llist1
    head2 = llist2
    
    while head1 and head2:
        if head1.data == head2.data:
            head1 = head1.next
            head2 = head2.next
        else:
            return 0
        
    if head1 == None and head2 == None:
        return 1
    else:
        return 0
        
        
