class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0,0,0]
        colorIndex = 0
        index = 0
        
        for i in range(len(nums)):
            temp[nums[i]] += 1
        
        print(temp)
        
        try:
            
            while index < (len(nums)):
                if temp[colorIndex] != 0:
                    nums[index] = colorIndex
                    temp[colorIndex] -= 1
                    index += 1
                else:
                    colorIndex += 1
        except: 
            "Do Nothing."
