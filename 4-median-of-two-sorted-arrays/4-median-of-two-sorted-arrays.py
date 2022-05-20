class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ln1 = len(nums1)
        ln2 = len(nums2)

        if ln2 < ln1:
            ln1, ln2, nums1, nums2 = ln2, ln1, nums2, nums1

        start = 0
        end = ln1

        while start <= end:
            pn1 = (start + end) // 2
            pn2 = ((ln1 + ln2 + 1) // 2) - pn1

            max_left_n1 = nums1[pn1 - 1] if pn1 != 0 else float("-inf")
            min_right_n1 = nums1[pn1] if pn1 != ln1 else float("inf")

            max_left_n2 = nums2[pn2 - 1] if pn2 != 0 else float("-inf")
            min_right_n2 = nums2[pn2] if pn2 != ln2 else float("inf")

            if max_left_n1 <= min_right_n2 and max_left_n2 <= min_right_n1:
                if (ln1 + ln2) % 2 == 0:
                    return (
                                   max(max_left_n1, max_left_n2) + min(min_right_n1,
                                                                       min_right_n2)
                           ) / 2
                else:
                    return max(max_left_n1, max_left_n2)

            elif max_left_n1 > min_right_n2:
                end = pn1 - 1

            else:
                start = pn1 + 1