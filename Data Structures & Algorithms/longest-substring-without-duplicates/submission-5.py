class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        length = 0
        max_length = 0
        substring = ""
        left, right = 0, 0
        max_left = 0
        max_right = 0

        while right < len(s):
            if s[right] not in hashset:
                hashset.add(s[right])
                right += 1
            else:
                hashset.remove(s[left])
                left += 1  
            length = right - left 
            if length > max_length:
                max_length = length
                max_left = left
                max_right = right

        substring = s[max_left:max_right]
        return max_length


