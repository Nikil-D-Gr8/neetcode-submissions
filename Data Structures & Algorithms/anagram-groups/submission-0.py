class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups: dict = {}

        for word in strs:
            newWord: tuple = tuple(sorted(word)) 

            if newWord not in groups:
                groups[newWord] = [word]
            else:
                groups[newWord] += [word]

        return list(groups.values())