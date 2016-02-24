#coding: utf8

class  LongestSubstringWithoutRepeat:
    def lengthOfLongestSubstring(self, s):
        startPosition, endPosition = 0, 0
        maxLengthOfSubstring = 0
        tempMaxLength = 0
        for char in s:
            if char in s[startPosition: endPosition]:
                startPosition = s.find(char, startPosition, endPosition) + 1
                tempMaxLength = endPosition + 1 - startPosition
            else:
                tempMaxLength += 1
            endPosition += 1
            maxLengthOfSubstring = max(maxLengthOfSubstring, tempMaxLength)
        return maxLengthOfSubstring

    # method 2: (learn from other people's answers):
    def lengthOfLongestSubstring2(self, s):
        maxLengthOfSubstring = 0
        startPosition = 0
        mapToIndex = {}
        for index, char in enumerate(s):
            if char in mapToIndex and mapToIndex[char] >= startPosition:
                startPosition = mapToIndex[char] + 1
            mapToIndex[char] = index
            maxLengthOfSubstring = max(maxLengthOfSubstring, index - startPosition + 1)
        return maxLengthOfSubstring
            
if __name__ == '__main__':
    lswr = LongestSubstringWithoutRepeat()
    length = lswr.lengthOfLongestSubstring2('abba')
    print(length)
