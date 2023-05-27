class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for i in range(len(nums)):
            if nums[i] in temp:
                return [i, temp[nums[i]]]
            temp[target - nums[i]] = i
