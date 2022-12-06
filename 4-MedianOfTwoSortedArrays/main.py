class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 171ms / 14.2MB
        combined = nums1 + nums2
        combined = sorted(combined)
        while len(combined) > 2:
            combined.pop(0)
            combined.pop()
        if len(combined) == 1:
            return float(combined[0])
        else:
            return (combined[0] + combined[1]) / 2
