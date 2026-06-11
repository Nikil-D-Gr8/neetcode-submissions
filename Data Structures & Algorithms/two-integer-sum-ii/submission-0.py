class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for left in range(len(numbers)-1):

            for right in range(len(numbers)-1,left,-1):
                print(f"trying in loop at {left} and {right}")
                if numbers[left] + numbers[right] < target:
                    print(f"break at {left} and {right}")
                    break
                elif numbers[left] + numbers[right] == target:
                    return [left+1,right+1] 


