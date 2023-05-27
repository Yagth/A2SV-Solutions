class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsDict = {}
        n = len(nums)

        for i in nums:
            numsDict[i] = i

        for i in range(0, n + 1):
            if i not in numsDict:
                return i
