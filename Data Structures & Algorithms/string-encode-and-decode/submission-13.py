class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word))
            res += "#"
            res += word
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        length = 0 
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            print("length", length)
            start = j + 1
            end = start + length
            word = s[start:end]
            res.append(word)

            i = end
        
        return res

                