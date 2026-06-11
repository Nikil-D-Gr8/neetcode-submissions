class Solution:
    def isPalindrome(self, s: str) -> bool:
        letter = list(filter(lambda x : x.isalnum(),s))
        letter = "".join(letter).lower()
        print(letter)
        return letter[::-1] == letter