# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head


        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        
        curr=second_half_head = slow.next
        slow.next=None #to break the link

        prev=None

        while curr is not None:
            next_node=curr.next

            curr.next=prev
            prev=curr
            curr=next_node

        new_second_half_head=prev

        first = head
        second = new_second_half_head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2



        

        