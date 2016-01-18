#coding:utf-8

class LongestIncreasingSubsequence(object):
    def longestIncreasingSubsequence(self, nums):
		if len(nums) == 0:
			return []
		increasingSubsequence = []
		positionIndex = 0
		for biggerThanThis in nums:
			itemList = [biggerThanThis]
			tempList = nums[positionIndex+1:]
			for num in tempList:
				if num > biggerThanThis:
					itemList.append(num)
			if len(increasingSubsequence) < len(itemList):
				increasingSubsequence = itemList
			if len(increasingSubsequence) == len(tempList)+1:
				break
			positionIndex += 1
		if len(increasingSubsequence) == 1:
			return increasingSubsequence
		return (increasingSubsequence[:1] + self.longestIncreasingSubsequence(increasingSubsequence[1:]))
        
    def lengthOfLongestIncreasingSubsequence(self, nums):
		return len(self.longestIncreasingSubsequence(nums))

if __name__ == '__main__':
	longestIS = LongestIncreasingSubsequence()
	testSequence = []
	print longestIS.longestIncreasingSubsequence(testSequence)
	print longestIS.lengthOfLongestIncreasingSubsequence(testSequence)
