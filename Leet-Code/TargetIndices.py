class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        nums = sorted(nums)

        for i, num in enumerate(nums):
            if num == target:
                result.append(i)
            elif num > target:
                break
        return result
