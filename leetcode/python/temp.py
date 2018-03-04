class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        if size == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
            
        i = 0
        j = size - 1
        
        while i < j:
            if nums[i] > nums[j]:
                i += 1
                j -= 1
            else:
                break
        
        if i == j and nums[i-1] < nums[i]:
            i += 1
        print('i',i)
        sorted = nums[-i::-1] + nums[:-i:-1]
        
        x = 0
        y = size - 1
        while x <= y:
            c = (x+y) / 2
            print(x, c, y)
            if sorted[c] < target:
                y = c - 1
            elif sorted[c] > target:
                x = c + 1
            else:
                if c >= i:
                    return (i+size-1) - c
                else:
                    return (i-1) - c   
        return -1


if __name__ == "__main__":

    #matrix = [[1,2,3,0],[2,4,0,7],[8,6,5,1]]
    nums = [1,3]
    print(nums)
    print(Solution().search(nums,1))
