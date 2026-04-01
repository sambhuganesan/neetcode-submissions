class Solution:
    def minWindow(self, s: str, t: str) -> str:
        slow, fast = 0, 0
        hashmap_t = {}
        hashmap_window = {}
        min_string = ""

        if s == t:
            return s

        if len(t) > len(s):
            return ""

        for i, ch in enumerate(t):
            hashmap_t[ch] = hashmap_t.get(ch, 0) + 1

        while fast < len(s):
            if s[fast] in hashmap_t.keys():
                hashmap_window[s[fast]] = hashmap_window.get(s[fast], 0) + 1
                while slow <= fast and all(hashmap_window.get(ch, 0) >= count for ch, count in hashmap_t.items()):
                    if min_string == "" or fast+1-slow < len(min_string):
                        min_string = s[slow:fast+1]
                    hashmap_window[s[slow]] = hashmap_window.get(s[slow], 0) - 1
                    slow += 1
            fast += 1

        return min_string