class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        sz = len(nums)

        nums.sort()

        cache = {}

        for i in range(0, sz):
            for j in range(i+1, sz):
                sumIJ = nums[i] + nums[j]
                if sumIJ in cache:
                    cache[sumIJ].append([i, j])
                else:
                    cache[sumIJ] = [[i, j]]

        twoSums = cache.keys()
        twoSums.sort()

        result = []
        i = 0
        j = len(twoSums) - 1

        while i <= j:
            if twoSums[i] + twoSums[j] == target:
                for sumsI in cache[twoSums[i]]:
                    for sumsJ in cache[twoSums[j]]:
                        if sumsI[0] == sumsJ[0] \
                            or sumsI[0] == sumsJ[1] \
                            or sumsI[1] == sumsJ[0] \
                            or sumsI[1] == sumsJ[1]:
                                continue
                        else:
                            print(sumsI + sumsJ)
                            tmp = sorted(sumsI + sumsJ)
                            if tmp not in result:
                                result.append(tmp)
                i += 1
                j -= 1
            elif twoSums[i] + twoSums[j] < target:
                i += 1
            else:
                j -= 1

        final = []
        for each in result:
            final.append([nums[i] for i in each])
        return final

        
if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    print(Solution().fourSum(nums, 0))
