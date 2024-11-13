def intersetPoint(head1,head2):
    temp1=head1
    temp2=head2
    while temp1:
        val=temp1.data
        if val==0:
            temp1.data=float("-inf")
        else:
            temp1.data=-(val)
        temp1=temp1.next
    
    while temp2:
        val=temp2.data
        if val<0 and val!=float("-inf"):
            return -val
        elif val==float("-inf"):
            return 0
        temp2=temp2.next
    return -1