# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def print_list(lst):
            cur = lst
            while cur:
                print(cur.val,"-> ", end = "")
                cur = cur.next

        def reverse_list(lst):
            prev = None
            cur = lst
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

                
        fast = slow = head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        sec_half = slow.next
        slow.next = None
        first_half = head
        # Reverse after mid
        sec_half = reverse_list(sec_half)
        # print_list(first_half)
        # print()
        # print_list(sec_half)
        res = ListNode(0)
        while first_half and sec_half:
            nxt1 = first_half.next
            nxt2 = sec_half.next
            first_half.next = sec_half
            sec_half.next = nxt1
            sec_half = nxt2
            first_half = nxt1
        head = first_half
            
