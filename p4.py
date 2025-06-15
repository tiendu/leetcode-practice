def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # Ensure nums1 is the smaller array to perform binary search on
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    half = (total + 1) // 2  # Half of the total elements (used for partitioning)
    left, right = 0, m  # Binary search boundaries on nums1

    while left <= right:
        i = (left + right) // 2  # Partition index for nums1
        j = half - i  # Partition index for nums2 (complementary)

        # Handle edge values by assigning -inf or inf when partition is at array ends
        Aleft = nums1[i - 1] if i > 0 else float('-inf')
        Aright = nums1[i] if i < m else float('inf')

        Bleft = nums2[j - 1] if j > 0 else float('-inf')
        Bright = nums2[j] if j < n else float('inf')

        # Check if we have a correct partition
        if Aleft <= Bright and Bleft <= Aright:
            # Even total length: median is average of max left and min right
            if total % 2 == 0:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            else:
                # Odd total length: median is max of left partition
                return max(Aleft, Bleft)
        elif Aleft > Bright:
            # Too many elements taken from nums1, reduce i
            right = i - 1
        else:
            # Not enough elements from nums1, increase i
            left = i + 1

