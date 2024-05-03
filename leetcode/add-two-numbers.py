# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def returnNextNode(self, listNode, append_list):
        append_list.append(listNode.val)
        if listNode.next != None:
            return self.returnNextNode(listNode.next, append_list)
        else:
            return append_list
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = self.returnNextNode(l1, [])
        l2_list = self.returnNextNode(l2, [])
        l1_list.reverse()
        l2_list.reverse()
        string_l1 = [ str(I) for I in l1_list ]
        string_l2 = [ str(I) for I in l2_list ]
        l1_reversed = int(''.join(string_l1))
        l2_reversed = int(''.join(string_l2))
        sum_reversed = list(str(l1_reversed + l2_reversed))
        final_node = None
        for single_element in sum_reversed:
            final_node = ListNode(val = single_element, next = final_node)
        return final_node