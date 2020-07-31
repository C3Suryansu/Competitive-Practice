class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2 == 0:
            for i in range(1, (n // 2) + 1):
                res.append(i)
                res.append(-1 * i)
        else:
            for i in range(1, ((n - 1) // 2) + 1):
                res.append(i)
                res.append(-1 * i)
            res.append(0)
        return res
            
        
