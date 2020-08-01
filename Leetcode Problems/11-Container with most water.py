class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
# Start from the beginning and compare with the end
# Move the left and right as, if left height less than right height, ofc move right to go to the next possible maximum height, and similarly for right.
# Ans will be always the maximum value so no reason to loop through everything twice as list of max one sweep list
