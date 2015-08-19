class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode} 
    def addTwoNumbers(self, l1, l2):
        p1 = l1
        p2 = l2
        answer = ListNode(0)
        p = answer
        c1 = 0
        c2 = 0
        
#        count = 0
        while p1 is not None and p2 is not None:
            val = (p1.val + p2.val + c1) % 10 
            c2 = (p1.val + p2.val + c1) / 10
            c1 = c2
            p.next = ListNode(val)
#            p3.next = p
#            if count == 0:
#                answer = p
#            p3 = p
            p = p.next
            p1 = p1.next
            p2 = p2.next
#            count += 1

        if p2 is not None:
            while p2 is not None:
                val = (p2.val + c1) % 10
                c2 = (p2.val + c1) /10
                c1 = c2
                p.next = ListNode(val)
#                p3.next = p
#                if count == 0 :
#                    answer = p
                p = p.next
                p2 = p2.next
#                count += 1 
        elif p1 is not None:
            while p1 is not None:
                val = (p1.val + c1) % 10
                c2 = (p1.val + c1) /10
                c1 = c2
                p.next = ListNode(val)
#                p3.next = p
#                if count == 0:
#                    answer = p
                p = p.next
                p1 = p1.next
#                count += 1 
        
        if c1 != 0:
            p.next = ListNode(1)
            p = p.next
        return answer.next


                
solution = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l3 = solution.addTwoNumbers(l1, l2)

while l3 is not None:
    print l3.val
    l3 = l3.next
