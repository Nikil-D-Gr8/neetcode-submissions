class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded : str = ""
        for word in strs:
            encoded += "|%|"+ str(len(word))+ "|%|" + word 
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            i += 3
            j = s.find("|%|", i)
            length = int(s[i:j])
        
            i = j + 3

            decoded.append(s[i:i+length])

            i += length

        return decoded