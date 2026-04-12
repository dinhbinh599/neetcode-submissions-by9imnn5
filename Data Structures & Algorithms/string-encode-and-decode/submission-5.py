class Solution:

    def encode(self, strs: List[str]) -> str:
        res = str()
        for s in strs:
            res += str(len(s)) + "#" + s

        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        curr = 0
        currentStr = str()
        for i in range(len(s)):
            if i < curr and curr != 0:
                continue
            
            if s[i] == '#':
                if curr == 0:
                    numberOfChars = int(s[0:i])
                else:
                    numberOfChars = int(s[curr:i])

                res.append(s[i+1:i+1+numberOfChars])
                curr = i+1+numberOfChars

        return res
