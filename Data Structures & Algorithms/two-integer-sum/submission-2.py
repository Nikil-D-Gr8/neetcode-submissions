class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indexNum: dict = {}

        for index in range(len(nums)):
            if target - nums[index] in indexNum:
                return sorted([index,indexNum[target-nums[index]]])
            indexNum[nums[index]] = index