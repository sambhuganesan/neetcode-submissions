class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # algorithm : start at nums[0], go to the index of the value
        # of num[0], change num[0] = -1, then go to index of the value
        # of the next of num[0] and so on.
        i = 0
        while(nums[i] != -1):
            val = nums[i]
            nums[i] = -1
            i = val
        return i
