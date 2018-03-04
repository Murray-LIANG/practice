class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
    
        m = len(triangle)
        if m == 0:
            return 0
        n = len(triangle[-1])
        if n == 0:
            return 0
        
        cache = triangle[-1]
        for i in range(m-2, -1, -1):
            print(i, cache)
            lineCache = triangle[i]
            for j in range(i, -1, -1):
                print(i,j,lineCache)
                minCacheJ = min(cache[j], cache[j+1])
                lineCache[j] = triangle[i][j] + minCacheJ
            cache[:i+1] = lineCache

        return cache[0]

if __name__ == '__main__':
    cases = [
        [   [-1],
            [3,2],
            [-3,1,-1],
        ]
    ]

    solution = Solution()
    for case in cases:
        print(case)
        print(solution.minimumTotal(case))

