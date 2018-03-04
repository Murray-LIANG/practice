class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sz = len(nums)
        if sz == 0:
            return 0

        i = 0
        j = 1
        full = False
        while j < sz:
            if nums[j] == nums[i]:
                if full:
                    j += 1
                else:
                    full = True
                    i += 1
                    nums[i] = nums[j]
                    j += 1
            else:
                full = False
                i += 1
                nums[i] = nums[j]
                j += 1
        print(nums)
        print('[' + '., ' * (i) + '^')
        return i+1


if __name__ == '__main__':
    cases = [
        [1,2],
        [1,1,1,2,3,3,4,5,5,5],
        [1,1],
        [2,2,2],
        [1,2,2,2,3,4,4,5,5,5,5],
        [1,1,1,1,3,3],
        [1,1,2,2]
    ]
    for case in cases:
        print(case)
        print(Solution().removeDuplicates(case))

