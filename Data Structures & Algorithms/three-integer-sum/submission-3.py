class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        output = []

        if len(nums) < 3:
            output
        elif len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                output.append(nums)
        else: 
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                l, r = i+1, len(nums)-1
                target = 0 - nums[i]
                
                while l < r:
                    if nums[l] + nums[r] == target:
                        output.append([nums[i], nums[l], nums[r]])
                        l+=1
                        r-=1
                        while l < r and nums[l] == nums[l-1]:
                            l+=1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif nums[l] + nums[r] > target:
                        r-=1
                    else:
                        l+=1
        return output