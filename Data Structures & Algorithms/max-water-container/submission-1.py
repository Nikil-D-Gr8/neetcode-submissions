class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxi = 0
        while left < right:
            water = (right-left) * min(heights[left],heights[right])
            maxi = max(maxi,water)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] == heights[right]:
                if heights[left+1] < heights[right-1]:
                    left += 1
                else:
                    right -=1
            else:
                right -= 1

        return maxi


