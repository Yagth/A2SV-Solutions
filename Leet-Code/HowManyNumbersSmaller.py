class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i] and j!=i:
                    count += 1
            counts.append(count)
        return counts
