class Solution:
    def isHappy(self, n: int) -> bool:
        res = set()
        while n not in res:
            res.add(n)
            count = 0
            while n!=0:
                count += (n%10) ** 2
                n = n // 10
            if count == 1 :
                return True
            n = count
        return False
