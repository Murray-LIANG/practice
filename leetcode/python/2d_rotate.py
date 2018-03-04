class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sz = len(nums)
        is sz == 0:
            return True

        farest = 0
        for i in range(0, sz):
            if farest == sz - 1:
                return True
            elif i >= farest:
                return False
            elif i + nums[i] > farest:
                farest = i + nums[i]

        return False


if __name__ == '__main__':
    cases = [
        [3,2,1,0,4],
        [2,2,1,1,4],
    ]

    for case in cases:
        print(case)
        print(Solution().canJump(case))
