class Solution:

    def encode(self, strs: List[str]) -> str:
        output=""
        outputlen=""
        for x in strs:
            output += x
            outputlen+="|" + str(len(x))
        return f"{output}**endofstring**{outputlen}"

    def decode(self, s: str) -> List[str]:
        start = int(s.find("**endofstring**")) + 15
        codedstring = s[:(start-15)]
        codedlength = s[start:]   
     
        lengths = codedlength.split("|")[1:]
        print(lengths)
        out = []
        for x in range(len(lengths)):
            x= int(x)
            out.append(codedstring[:int(lengths[x])])
            codedstring= codedstring[int(lengths[x]):]
        return out
            

        



