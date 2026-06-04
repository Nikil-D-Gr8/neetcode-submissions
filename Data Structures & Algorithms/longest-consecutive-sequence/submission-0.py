class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet : set = set(nums)

        maxnum = 0
        count = 1
        for number in nums:
            if number - 1 not in numSet:
                count = 1
                while number + 1 in numSet:
                    number +=1
                    count +=1
                maxnum = max(maxnum, count) 

        return maxnum