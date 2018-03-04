class Solution(object):
    def calcSum(self, candidates, target):
        sz = len(candidates)
        print('S:calcsum', 'candidates:', candidates, ', target:', target)

        if sz == 0:
            return []

        i = 0
        result = []
        while i < sz:
            current = candidates[i]
            if current > target:
                print('E:calcsum', 'candidates:', candidates, ', target:', target)
                break
            elif current == target:
                print('E:calcsum', 'candidates:', candidates, ', target:', target)
                #return [[current]]
                result.append([current])
            else:
                print('i:', i)
                subSums = self.calcSum(candidates[i+1:], target - current)
                print('subSums:', subSums)
                if len(subSums) != 0:
                    result += [[current] + each for each in subSums]

            tmp = i
            i += 1
            while i < sz and candidates[i] == candidates[tmp]:
                print('skip:', candidates[i])
                i += 1
        print('E:calcsum', 'candidates:', candidates, 'target:', target, 'result:', result)
        return result

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sz = len(candidates)
        if sz == 0:
            return []

        candidates.sort()
        return self.calcSum(candidates, target)

if __name__ == '__main__':
    cases = [
        [[10,1,2,7,6,1,5], 8]
    ]

    solution = Solution()
    for case in cases:
        print(case)
        print(solution.combinationSum2(case[0], case[1]))
