class Solution(object):
    def addTwoNumbers(self, l1, l2):

        a = []
        b = []

        # Convert l1 → list
        while l1:
            a.append(l1.val)
            l1 = l1.next

        # Convert l2 → list
        while l2:
            b.append(l2.val)   # FIXED
            l2 = l2.next

        # Convert list → number
        s = int(''.join(map(str, a[::-1]))) 
        s1 = int(''.join(map(str, b[::-1]))) 

        total = s + s1

        # Convert number → linked list
        dummy = ListNode(0)
        curr = dummy

        if total == 0:
            return ListNode(0)

        for digit in str(total)[::-1]:   # reverse for linked list format
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next
