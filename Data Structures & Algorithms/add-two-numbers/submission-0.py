# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        stack={}
        multiplier=1
        number1,number2=0,0

        while curr1 is not None:
            value1=curr1.val
            
            number1+=value1*multiplier
            multiplier*=10
            curr1=curr1.next
        
        multiplier=1
        while curr2 is not None:
            
            value2=curr2.val
            number2+=value2*multiplier
            multiplier*=10
            curr2=curr2.next
       
        newNumber=number1+number2

        print(newNumber)

        temp=newNumber%10

        newNode=ListNode(temp)
        newNode1=newNode
        
        newNumber=newNumber//10

        while newNumber>0:
            
            temp1=newNumber%10
            newNode1.next=ListNode(temp1)
            newNode1=newNode1.next
            newNumber=newNumber//10
        return newNode



        


        

            
        