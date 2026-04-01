class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set()
        counts = []
        if len(nums) == 0:
            return 0
        for i in nums:
            hashmap.add(i)
        for i in hashmap:
            count = 0
            k = i+1
            while k in hashmap:
                count += 1
                k += 1
            counts.append(count + 1)
        return max(counts)
        