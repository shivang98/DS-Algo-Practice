from linked_list import Linked_List

# ~ 1-2-3-4-5-6-7-8-9-10

def nth_from_end(head,n):
    if head == None: return None
    curr = head
    run = head
    for i in range(n):
        if run == None:
            return None
        run = run.next
    
    while run != None:
        curr = curr.next
        run = run.next
        
    return curr.data

ll = Linked_List()
ll.insert_at_head(1)
ll.insert_at_head(2)
ll.insert_at_head(3)
ll.insert_at_head(4)
ll.insert_at_head(5)
ll.insert_at_head(6)
ll.insert_at_head(7)
ll.insert_at_head(8)
ll.insert_at_head(9)
ll.insert_at_head(10)

ll.display()
print()

print(nth_from_end(ll.head, 3))

