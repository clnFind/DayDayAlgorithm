# -*- coding: utf-8 -*-


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        nums1 = [1, 2]
        nums2 = [3, 4]
        则中位数是 (2 + 3)/2 = 2.5
        """

        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        if length % 2 == 1:

            return nums1[length // 2]

        result = (nums1[length//2] + nums1[length//2 - 1])/2

        return result

    def median(self, nums1, nums2):
        """
        时间复杂度 O(log(m+n))
        :param nums1:
        :param nums2:
        :return:
        """

        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    print(max_of_left, m, n)
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0


if __name__ == '__main__':

    l1 = [1, 3, 5]
    l2 = [2, 4, 6]
    # r = Solution().findMedianSortedArrays(l1, l2)
    # print(r)

    r1 = Solution().median(l1, l2)
    print(r1)
