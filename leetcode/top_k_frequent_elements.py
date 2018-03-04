class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequent = {}
        for n in nums:
            if n not in frequent:
                frequent[n] = 0
            else:
                frequent[n] += 1

        bucket = {}
        for n, f in frequent.items():
            if f not in bucket:
                bucket[f] = [n]
            else:
                bucket[f].append(n)

        result = []
        for f in sorted(bucket.keys(), reverse=True):
            if len(result) >= k:
                break
            result += bucket[f]

        return result


if __name__ == '__main__':
    datas = [
        ([1,2,3,2,1,1], 2, [1,2]),
        ([1,1,1,1,1,1], 1, [1]),
    ]

    for i, (nums, k, expected) in enumerate(datas, 1):
        print('>>> Test #{} <<<'.format(i))
        print('Nums: {}. k: {}.'.format(nums, k))
        result = Solution().topKFrequent(nums, k)
        print('Result: {}. Expected: {}. {}.'.format(
            result, expected,
            'PASS' if sorted(result)==sorted(expected) else 'FAIL'))
