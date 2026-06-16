class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = set()


        for x in range(len(nums)-2):
            left = x + 1
            right = len(nums) - 1

            while left < right:
                total = nums[x] + nums[left] + nums[right] 
                if total == 0:
                    out.add(tuple([nums[x],nums[left],nums[right]]))
                    left += 1
                    right -= 1
                elif total <= 0:
                    left += 1
                else:
                    right -= 1
        return list([list(x) for x in out])



