# https://leetcode.com/problems/expression-add-operators


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        self.dfs(num, target, '', 0, 0, res, 0)
        return res

    @staticmethod
    def dfs(num, target, path, pos, total, res, to_multiply):
        if pos == len(num):
            if total == target:
                res.append(path)
            return

        for next_pos in range(pos + 1, len(num) + 1):
            if num[pos] == '0' and next_pos != pos+1:
                # skip the number starting with '0' like '05'
                break
            num_pos = int(num[pos:next_pos])
            if pos == 0:
                Solution.dfs(num, target, num[pos:next_pos], next_pos,
                             total + num_pos, res, num_pos)
            else:
                Solution.dfs(num, target, path + '+' + num[pos:next_pos],
                             next_pos, total + num_pos, res, num_pos)
                Solution.dfs(num, target, path + '-' + num[pos:next_pos],
                             next_pos, total - num_pos, res, -num_pos)
                Solution.dfs(num, target, path + '*' + num[pos:next_pos],
                             next_pos,
                             total - to_multiply + to_multiply * num_pos, res,
                             to_multiply * num_pos)

print(Solution().addOperators('123', 6))
print(Solution().addOperators('105', 5))
