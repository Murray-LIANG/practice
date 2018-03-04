class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        sz = len(nums)
        if sz < 3:
            return target

        nums.sort()

        minGap = None
        minSum = None
        for i in range(0, sz):

            j = i+1
            k = sz-1

            while j < k:
                sumIJK = nums[i] + nums[j] + nums[k]
                gap = abs(target - sumIJK)
                if minGap is None or gap < minGap:
                    minGap = gap
                    minSum = sumIJK

                if sumIJK == target:
                    return target
                elif sumIJK < target:
                    j += 1
                else:
                    k -= 1
                
        return minSum

if __name__ == '__main__':
    cases = [
        [[-1,2,1,-4], 1],
        [[-1,2,1,-4], 0],
        [[-1,2,1,-4], 2],
    ]

    solution = Solution()
    for case in cases:
        print(case)
        print(solution.threeSumClosest(case[0], case[1]))

