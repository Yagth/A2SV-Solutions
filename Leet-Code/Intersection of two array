class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()
        intersection = []
        
        i = 0
        k = 0

        while i < len(nums1) and k < len(nums2):
            if nums1[i] == nums2[k]:
                intersection.append(nums1[i])
                k+=1
                i+=1
            elif nums1[i] > nums2[k]:
                k+=1
            else:
                i+=1
                
        return intersection
        
   """ class Solution:
        def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

            intersection = []
            firstListCount = defaultdict(int)

            if len(nums2) < len(nums1):
                temp = nums1
                nums1 = nums2
                nums2 = temp

            for i in range(len(nums1)):
                firstListCount[nums1[i]] += 1

            for i in range(len(nums2)):
                if firstListCount[nums2[i]] > 0:
                    firstListCount[nums2[i]] -= 1
                    intersection.append(nums2[i])

            return intersection  """
                
