class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += str(len(word))
            ans += "#"
            ans += word
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        count = 0
        buffer = ""
        while i < len(s):
            if s[i] == "#":
                count = int(buffer)
                word = s[(i + 1):(i + count + 1)]
                ans.append(word)
                buffer = ""
                i += count + 1
            else:
                buffer += s[i]
                i += 1
        return ans
            
