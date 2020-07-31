class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        for i in range(len(prices)):
            c = 0
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    res.append(prices[i] - prices[j])
                    c = 1
                    break
            if c != 1:
                res.append(prices[i])
        return res
