class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        def seendict(string):
            seen = {}
            for x in string:
                if x not in seen:
                    seen[x] = 1
                else:
                    seen[x] += 1
            return seen

        if seendict(s)==seendict(t):
            return True
        else:
            return False

        