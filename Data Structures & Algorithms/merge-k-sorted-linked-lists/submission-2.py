# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_2_list(list1, list2):
            res = cur = ListNode(0)
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            
            cur.next = list1 if list1 else list2
            return res.next
        
        if not lists or len(lists) == 0:
            return None
        if len(lists) == 1:
            return list[0]
        result = lists[0]
        for i in range(1, len(lists)):
            result = merge_2_list(result, lists[i])
        return result