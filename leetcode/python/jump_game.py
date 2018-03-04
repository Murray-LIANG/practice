class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sz = len(nums)
        if sz <= 1:
            return True

        farest = -1
        for i in range(0, sz):
            if i + nums[i] > farest:
                farest = i + nums[i]
            print(i, farest)

            if farest >= sz - 1:
                return True
            if i >= farest:
                return False

        return False


if __name__ == '__main__':
    cases = [
        [3,2,1,0,4],
        [2,2,1,1,4],
        [1,2],
        [0,2,3]
    ]

    for case in cases:
        print(case)
        print(Solution().canJump(case))

