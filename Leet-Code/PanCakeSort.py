class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        def isSorted(nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    return False
            return True

        sorted = isSorted(arr)

        result = []
        n = len(arr)
        print(n)
        while not sorted:
            maxIndex = arr.index(n)

            if maxIndex == n - 1:
                n -= 1
                continue
            
            if maxIndex != 0:
                arr = arr[:maxIndex+1][::-1] + arr[maxIndex+1:]
                result.append(maxIndex+1)
                
            arr = arr[:n][::-1]
            result.append(n)

            n-= 1
            sorted = isSorted(arr)

        return result
