class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            x = len(i)
            encoded = encoded + str(x) + "!" + i
        return encoded
    def decode(self, s: str) -> List[str]:
        output = []
        start_pos = 0
        k=1
        while k < len(s):
            if s[k-1].isdigit() and s[k] == "!":
                x = k - start_pos
                length = 0
                for i in range(0, x):
                    length += 10**(x - i - 1) * int(s[i + start_pos])
                word = ""
                for j in range(k+1, min(k+1+length, len(s))):
                    word += s[j]
                output.append(word)
                start_pos += len(str(length)) + 1 + length
            k += 1
        return output