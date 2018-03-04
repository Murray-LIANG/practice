class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums1)
        n = len(nums2)

        if m == 0 and n == 0:
            return 0

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        i_min, i_max, half_len = 0, m, (m + n + 1) / 2

        while i_min <= i_max:
            i = (i_min + i_max) / 2
            j = half_len - i


            if i >= 1 and nums1[i-1] > nums2[j]:
                i_max = i - 1
            elif i <= m-1 and nums2[j-1] > nums1[i]:
                i_min = i + 1
            else:

                print(i, j)
                # TODO check boundary
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])
                if (m + n) % 2:
                    return max_left
                else:
                    if i == m:
                        min_right = nums2[j]
                    elif j == n:
                        min_right = nums1[i]
                    else:
                        min_right = min(nums1[i], nums2[j])
                    return (max_left + min_right) / 2.0

        return 0


if __name__ == '__main__':
    datas = [
        ([], [], 0),
        ([], [1], 1),
        ([], [1,2], 1.5),
        ([1], [2], 1.5),
        ([1,3], [2], 2.0),
        ([1,2], [3,4], 2.5),
    ]

    for i, (nums1, nums2, expected) in enumerate(datas, 1):
        print('=' * 60)
        print('Test #{}'.format(i))
        print('nums1: {}. nums2: {}.'.format(nums1, nums2))
        result = Solution().findMedianSortedArrays(nums1, nums2)
        print('Result: {}. Expected: {}.'.format(result, result==expected))


