#coding = utf8
import copy

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class AddTwoNumbers:
    # method 1:
    def addTwoNumbers(self, nums1, nums2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        strFromNums1 = self.extractNumbers(nums1)
        strFromNums2 = self.extractNumbers(nums2)
        sumOfTwoNumbers = int(strFromNums1) + int(strFromNums2)
        #return ' -> '.join(reversed(str(sumOfTwoNumbers)))
        return [int(x) for x in reversed(str(sumOfTwoNumbers))]
    
    def extractNumbers(self, nums):
        tempOfNums = copy.copy(nums)
        strConvertedFromNums = str(tempOfNums.val)
        while tempOfNums.next is not None:
            strConvertedFromNums = str(tempOfNums.next.val) + strConvertedFromNums
            tempOfNums = tempOfNums.next
        return strConvertedFromNums

    # method 2, learn from other people's answers:
    def addTwoNumbers2(self, nums1, nums2):
        dummyNode = ListNode(0)
        headNode = dummyNode
        carryBit = 0
        duplicateOfNums1, duplicateOfNums2 = copy.copy(nums1), copy.copy(nums2)
        while carryBit or duplicateOfNums1 or duplicateOfNums2:
            nextNode = ListNode(carryBit)
            if duplicateOfNums1:
                nextNode.val += duplicateOfNums1.val
                duplicateOfNums1 = duplicateOfNums1.next
            if duplicateOfNums2:
                nextNode.val += duplicateOfNums2.val
                duplicateOfNums2 = duplicateOfNums2.next
            carryBit = nextNode.val // 10
            nextNode.val %= 10
            headNode.next = nextNode
            headNode = nextNode
        return dummyNode.next
    
if __name__ == "__main__":
    nums1 = ListNode(2)
    nums1_2 = ListNode(4)
    nums1.next = nums1_2
    nums1_3 = ListNode(3)
    nums1_2.next = nums1_3

    nums2 = ListNode(5)
    nums2_2 = ListNode(6)
    nums2.next = nums2_2
    nums2_3 = ListNode(4)
    nums2_2.next = nums2_3

    atn = AddTwoNumbers()
    #print(atn.addTwoNumbers2(nums1, nums2))
    r = atn.addTwoNumbers2(nums1, nums2)
    resultList = []
    while r is not None:
        resultList.append(r.val)
        r = r.next
    print(resultList)
