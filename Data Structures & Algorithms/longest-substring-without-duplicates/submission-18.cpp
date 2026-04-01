class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int right = 0;
        int max_length = 0;

        if (s.length() == 0) return 0;
        if (s.length() == 1) return 1;

        unordered_map<char, int> freq;
        while (right < s.length()) {
            if (freq.count(s[right]) && freq[s[right]] >= left) {
                int new_length = right - left;
                max_length = max(max_length, new_length);
                left = freq[s[right]] + 1;
            }
            freq[s[right]] = right;
            max_length = max(max_length, right - left + 1);
            right++;
        }

        return max_length;
    }
};
