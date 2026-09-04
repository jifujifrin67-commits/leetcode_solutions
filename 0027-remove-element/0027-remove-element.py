class Solution:
    def removeElement(self, nums, target):
        k = 0
        for i in range(len(nums)):
            if nums[i] != target:
                nums[k] = nums[i]
                k+=1
        return k