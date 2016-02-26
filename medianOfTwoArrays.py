#coding: utf8

class MedianOfTwoArrays:
    # Brute force:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        allNums = sorted(nums1 + nums2)
        lengthOfAllNums = len(allNums)
        if lengthOfAllNums % 2 == 1:
            return allNums[lengthOfAllNums // 2]
        else:
            return (allNums[(lengthOfAllNums - 1) // 2] + allNums[lengthOfAllNums // 2]) / 2.0

if __name__ == '__main__':
    moa = MedianOfTwoArrays()
    print(moa.findMedianSortedArrays([], [2, 3]))
