#coding:utf8

class LongestIncreasingSubsequce:
	def getLengthOfLIS(self, sequence):
		if len(sequence) == 2:
			return 0
		lengthOfSequence = len(sequence)
		lengthOfLISBeforeCurrentNum = 0
		everyLengthOfLIS = [1]
		for i in range(lengthOfSequence-1):
			everyLengthOfLIS.append(0)
		for i in range(lengthOfSequence):
			lengthOfLISBeforeCurrentNum = everyLengthOfLIS[i]
			for j in range(i):
				if sequence[i] > sequence[j] and everyLengthOfLIS[j] > lengthOfLISBeforeCurrentNum:
					lengthOfLISBeforeCurrentNum = everyLengthOfLIS[j]
			everyLengthOfLIS[i] = lengthOfLISBeforeCurrentNum + 1
		return max(everyLengthOfLIS)
		
if __name__ == '__main__':
	LIS = LongestIncreasingSubsequce()
	testSeq = [-2,-1]
	print LIS.getLengthOfLIS(testSeq)