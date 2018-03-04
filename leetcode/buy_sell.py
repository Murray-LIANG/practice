class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        sz = len(prices)

        if sz == 0:
            return 0
        
        profit = 0
        i = 0
        j = i + 1
        while j < sz:
            #print(i,j,prices[j-1],prices[j])
            if prices[j] >= prices[j-1]:
                profit += prices[j] - prices[j-1]
                j += 1
            else:
                i = j
                j = i + 1
        if i == sz - 1:
            profit += prices[i]
        return profit

if __name__ == '__main__':
    cases = [
                [1,2,5,3,6,4,3,5],
                [1,2,3,4,5,6,7],
                [6,5,4,3,2,1],
                [1,2,1,2,1]
            ]
    for case in cases:
        print(case)
        print('profit:', Solution().maxProfit(case))

