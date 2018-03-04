class Solution(object):
    def kSum(self, nums, start, end, k, target):
        #print(start,end,k,target)
        if k > end - start + 1:
            return []
        tmp = {}
        if k == 1:
            for i in range(start, end + 1):
                tmp[nums[i]] = True
            #print(tmp)
            if target in tmp:
                #print('pick ', start,end,k,target)
                return [target]
            else:
                return []
        else:
            i = start + 1
            while end - i + 1 >= 2:
                k_1_sum = self.kSum(nums, i, end, k - 1, target - nums[start])
                if len(k_1_sum) > 0:
                    return [nums[start]] + k_1_sum
                i += 1
        
        return []
            
            
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) < 3:
            return []
        
        nums.sort()
        
        if nums[0] == 0 and nums[-1] == 0:
            return [[0,0,0]]
        
        print(nums)
        result = []
        for i in range(0, len(nums) - 3):
            tmp = self.kSum(nums, i, len(nums)-1, 3, 0)
            if len(tmp) != 0:
                result.append(tmp)
            i += 1

        return result

if __name__ == "__main__":

    nums = [-15,13,6,-11,-4,5,-13,5,3,2,6,-1,4,12,-10,-13,-7,-4,-5,6,9,-14,1,-6,13,7,-8,10,-4,11,-8,-3,1,5,-7,4,-13,-13,-5,-3,4,-14,11,-14,5,-13,-12,13,-10,-10,-4,-15,13,13,-14,11,-3,-15,6,1,3,5,13,-11,-5,-9,1,-2,-14,11,10,5,4,-1,6,-6,-7,9,-15,-2,7,-12,-10,5,-14,13,-6,-9,6,7,7,-6,-2,-3,-9,0,-5,7,5,-4,-5,-7,-13,14,7,8,-15,7,-5,-15,-10,9]
    #nums = [-1,0,1,2,-2,2,-4]
    print(nums)
    print(Solution().threeSum(nums))
