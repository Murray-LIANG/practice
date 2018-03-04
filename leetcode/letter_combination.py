class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        mapping = {
            '1': '1',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' ',
        }

        def comb(digits):
            if len(digits) == 1:
                return list(mapping[digits[0]])
            else:
                lst = comb(digits[:-1])
                result = []
                for c in mapping[digits[-1]]:
                    result += [each + c for each in lst]
                return result

        return comb(digits)



if __name__ == '__main__':
    datas = [
        ('23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
    ]

    for digits, expected in datas:
        result = Solution().letterCombination(digits)
        print('digits: {}. Combination: {}. Expected: {}'.format(
            digits, result, set(expected) == set(result)))
