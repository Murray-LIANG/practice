class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        mapping = {
            'M': ('', 'M', 'MM', 'MMM'),
            'C': ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
            'X': ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
            'I': ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')
        }

        return (mapping['M'][num/1000] + mapping['C'][num%1000/100] +
                mapping['X'][num%100/10] + mapping['I'][num%10])

if __name__ == '__main__':
    datas = [
        (1234, 'MCCXXXIV'),
        (0, ''),
    ]

    for num, expected in datas:
        result = Solution().intToRoman(num)
        print('Num: {}. Rome: {}. Expected: {}'.format(
            num, result, expected == result))

