class Solution(object):
    def lengthOfLIS(self, nums):
        def longestIncreasingSubsequence(nums):
            increasingSubsequence =[]
            positionIndex = 0
            for biggerThanThis in nums:
                itemList = [biggerThanThis]
                tempList = nums[positionIndex+1:]
                for num in tempList:
                    if num > biggerThanThis:
                        itemList.append(num)
                    else:
                        break
                if len(increasingSubsequence) < len(itemList):
                    increasingSubsequence = itemList
                if len(increasingSubsequence) == len(tempList)+1:
                    break
                positionIndex += 1
            if len(increasingSubsequence) == 1:
                return increasingSubsequence
            return (increasingSubsequence[:1] + longestIncreasingSubsequence(increasingSubsequence[1:]))
        return len(longestIncreasingSubsequence(nums))
		
if __name__ == '__main__':
	longestIS = Solution()
	testSequence = [10,9,2,1,5,3,2,3,7,101,18]
	#print longestIS.longestIncreasingSubsequence(testSequence)
	print longestIS.lengthOfLIS(testSequence)