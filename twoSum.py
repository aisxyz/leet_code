class TwoSum(object):
    # method 1( brute force), O(n^2):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexOfAddend = 0
        for addend in nums:
            anotherAddend = target - addend
            try:
                startIndex = indexOfAddend + 1
                indexOfAnotherAddend = nums[indexOfAddend + 1: ].index(anotherAddend) + startIndex
            except ValueError:
                pass
            else:
                break
            indexOfAddend += 1
        if indexOfAddend < len(nums) - 1:
            return [indexOfAddend, indexOfAnotherAddend]

    # method 2( maptable), O(n), learn from other people's anwsers:
    def twoSum2(self, nums, target):
        mapToIndex = {}
        for indexOfCurrentAddend in range(len(nums)):
            currentAddend = nums[indexOfCurrentAddend]
            anotherAddend = target - currentAddend
            indexOfAnotherAddend = mapToIndex.get(anotherAddend)
            if indexOfAnotherAddend is not None:
                return [indexOfAnotherAddend, indexOfCurrentAddend]
            mapToIndex[currentAddend] = indexOfCurrentAddend
    
if __name__ == '__main__':
    ts = TwoSum()
    nums = [3, 2, 4]
    target = 6
    print('result:', ts.twoSum2(nums, target))
