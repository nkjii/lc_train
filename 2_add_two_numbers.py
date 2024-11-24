class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
１の桁から加算していくのをLinkedListでやっている
繰り上がりを保持する変数

最後に桁上がりする場合は1を追加する

if 両者のnextがない
    足し合わせる
    if 桁上がりあるか
桁上がりが存在する
    結果に１追加


[0] [0]
0 + 0 = 0
終了

[1,2] [3,4]
1 + 3 = 4
2 + 4 = 6
終了

[5,6] [7,9]
5 + 7 = 12  [2]
6 + 9 + 1 = 16  [2,6]
[2,6,1]
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0, None)
        n1 = l1
        n2 = l2
        current = result

        # ten, one = self.split_sum_digits(n1.val, n2.val)
        # result.val = one
        # result.next = ListNode(ten, None) if ten == 1 else None
        # current = result.next
        
        while n1 is not None or n2 is not None:
            val1 = n1.val if n1 is not None else 0
            val2 = n2.val if n2 is not None else 0
            ten, one = self.split_sum_digits(n1.val, n2.val)
            current.val = one
            current.next = ListNode(1, None) if ten == 1 else None
            n1 = n1.next
            n2 = n2.next

    def split_sum_digits(self, d1, d2):
        """
        数字を足し合わせて十の位と一の位に分ける関数。

        Args:
            numbers: 足し合わせる整数のリスト。

        Returns:
            tuple: (十の位, 一の位)
        """
        total = d1 + d2
        tens = total // 10
        ones = total % 10
        return tens, ones
