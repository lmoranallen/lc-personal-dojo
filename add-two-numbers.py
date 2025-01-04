class ListNode():
    def __init__(self):
        self.val = None
        self.next = None

    
def addTwoNumbers(l1: list[ListNode], l2: list[ListNode]) -> list[list[ListNode]]:
    currL1 = l1
    currL2 = l2
    carry = False

    while currL1 and currL2:
        if carry:
            currL1.val += 1
            carry = False
        val = currL1.val + currL2.val

        if val > 9:
            carry = True
            val -= 10
        currL1.val = val

        if currL1.next is None and currL2.next is not None:
            currL1.next = ListNode(0)
        
        if currL2.next is None and currL1.next is not None:
            currL2.next = ListNode(0)
        
        if currL2.next is None and currL1.next is None:
            break
            
        currL1 = currL1.next
        currL2 = currL2.next

    if carry:
        currL1.next = ListNode(1)
    
    return l1


# Takeaways 
    # Segment away conditional question logic from traversal where possible 
        # For instance, carrying over and modfiying digits should not be done in the same block scope as moving to the next node

        # The only overlap is when creating new nodes, deleting old nodes or merging together. 
        # Even then, carry logic is done separately here

        # Break down traversal into simpler use cases if possible. In this example, uneven Linked Lists are padded out.

        