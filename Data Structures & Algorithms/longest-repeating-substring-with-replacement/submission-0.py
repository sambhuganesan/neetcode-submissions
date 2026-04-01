class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        hashset = set(s)
        for i in hashset:
            left, right = 0, 0
            count = 0
            while right < len(s):
                if s[right] != i:
                    count += 1
                if count <= k:
                    max_length = max(max_length, right - left + 1)
                    right += 1
                else:
                    while count > k:
                        if s[left] != i:
                            count -= 1
                        left += 1
                    right += 1
        return max_length