class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        sz = len(prices)
        if sz <= 1:
            return 0

        profit = prices[0]
        i = 0
        j = 0
        while j < sz:
            if j != sz - 1 and prices[j+1] >= prices[j]:
                j += 1
            else:
                if profit < prices[j] - prices[i]:
                    profit = prices[j] - prices[i]
                    print(i,j,profit)
                i = j + 1
                j = i
        return profit

if __name__ == '__main__':
    cases = [
        #[1,2,3,4],
        #[1,1,1,2,3,3,4,5,5,5],
        #[1,2,2,1,3,4,4,5,6],
        [6,1,3,2,4,7],
    ]
    for case in cases:
        print(case)
        print(Solution().maxProfit(case))

