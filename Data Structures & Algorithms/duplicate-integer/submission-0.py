class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hashmap = set()
        for i in nums:
            if i in hashmap:
                return True
            else:
                hashmap.add(i)
        return False
