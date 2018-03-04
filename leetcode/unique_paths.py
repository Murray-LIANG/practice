class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        
        cache = [1 for i in range(0, n)]
        i = 1
        while i < m:
            j = 1
            while j < n:
                cache[j] += cache[j-1]
                j += 1
            i += 1
        return cache[n-1]

if __name__ == '__main__':
    cases = [[4,7], [5,8], [1,1], [2,1], [0,100], [100,0]]
    for case in cases:
        print(case)
        print('profit:', Solution().uniquePaths(case[0], case[1]))

