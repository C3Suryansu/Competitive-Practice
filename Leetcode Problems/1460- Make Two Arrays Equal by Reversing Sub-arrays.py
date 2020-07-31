class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
#Time complexity O(n logn), can be improved to O(n) using dictionary.
