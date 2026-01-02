class ListNode:
    def __init__(self, val=0, next=None):
        self.val= val
        self.next= next

class Solution:
    def addTwoNumbers(self, l1, l2): # Bu fonksiyon iki sayı alıyor
        # bağlı liste şeklinde ve toplamı da bağlı liste olarak döndürüyor.
        dummy_head= ListNode(0)  # Başlangıç düğümü
        current= dummy_head
        carry= 0  # Elde var mı?

        while l1 or l2 or carry:
            val1= l1.val if l1 else 0  # l1 varsa değeri al, yoksa 0
            val2= l2.val if l2 else 0

            total= val1+ val2+ carry
            carry= total// 10  # Yeni elde
            digit= total% 10   # Bu basamağa yazılacak rakam

            current.next= ListNode(digit)
            current= current.next

            if l1: l1= l1.next
            if l2: l2= l2.next

        return dummy_head.next
# Bağlı listeyi oluşturur
def create_linked_list(nums):
    dummy= ListNode()
    current= dummy
    for num in nums:
        current.next= ListNode(num)
        current= current.next
    return dummy.next

# Bağlı listeyi yazdırır
def print_linked_list(node):
    while node:
        print(node.val, end=" ")
        node= node.next
    print()

# Test
l1 = create_linked_list([2,4,3])  # 342
l2 = create_linked_list([5,6,4])  # 465

solution = Solution()
result = solution.addTwoNumbers(l1, l2)  # 807 -> [7, 0, 8]

print_linked_list(result)
