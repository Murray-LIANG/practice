class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        sz = len(nums)
        if sz <= 1:
            return []

        output = [1] * sz
        
        for i in range(1, sz):
            output[i] = nums[i - 1] * output[i - 1]

        tmp = 1
        for i in range(sz - 2, -1, -1):
            output[i] = nums[i + 1] * output[i] * tmp
            tmp *= nums[i + 1]
            print(output, tmp)

        return output



if __name__ == '__main__':
    cases = [
        #[1,2,3,4],
        #[1,1,1,2,3,3,4,5,5,5],
        [1,2,3,4,5],
    ]
    for case in cases:
        print(case)
        print(Solution().productExceptSelf(case))

