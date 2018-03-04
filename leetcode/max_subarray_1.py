class Solution(object):
    def maxOf3(self, first, second, third):
        if first > second:
            return first if first > third else third
        else:
            return second if second > third else third

    def maxSum(self, nums, startIndex, endIndex):
        if startIndex == endIndex:
            return nums[startIndex]

        centerIndex = (startIndex + endIndex) / 2
        leftMax = self.maxSum(nums, startIndex, centerIndex)
        rightMax = self.maxSum(nums, centerIndex+1, endIndex)
        #('index sce:', startIndex, centerIndex, endIndex)

        tmpLeftMax = nums[centerIndex]
        #print('tmpLeftMax:', tmpLeftMax)
        tmp = tmpLeftMax
        for i in range(centerIndex-1, startIndex-1, -1):
            #print('nums[i]', i, nums[i])
            tmp += nums[i]
            if tmp > tmpLeftMax:
                #print('nums[i] + tmpLeftMax', nums[i] + tmpLeftMax)
                tmpLeftMax = tmp
        tmpRightMax = nums[centerIndex+1]
        tmp = tmpRightMax
        for num in nums[centerIndex+2:endIndex+1]:
            tmp += num
            if tmp > tmpRightMax:
                tmpRightMax = tmp
        result = self.maxOf3(leftMax, tmpLeftMax+tmpRightMax, rightMax)
        #print('max left tmpLeft tmpRight right result:', leftMax, tmpLeftMax, tmpRightMax, rightMax, result)
        return result

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.maxSum(nums, 0, len(nums)-1)

if __name__ == '__main__':
    cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ]

    solution = Solution()
    for case in cases:
        print(case)
        print(solution.maxSubArray(case))

