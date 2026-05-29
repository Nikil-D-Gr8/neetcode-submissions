from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countDict = Counter(nums)

        sortedList: list = sorted(countDict.items(),key=lambda x : x[1])

        return [x[0] for x in sortedList[::-1][:k]]
