class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashtable = {}
        for i, elem in enumerate(nums):
            hashtable[elem] = i

        for first, second in operations:
            index = hashtable[first]
            del hashtable[first]
            hashtable[second] = index

        for key, i in hashtable.items():
            nums[i] = key

        return nums
