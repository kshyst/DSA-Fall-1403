def merge(nums1, m, nums2, n):

    index1 , index2 , k = 0 ,0 ,0
    merged_array = [0] * (n + m )

    while index1 < m and index2 < n:
        if nums1[index1] <= nums2[index2]:
            merged_array[k] = nums1[index1]
            index1 += 1
        else :
            merged_array[k] = nums2[index2]
            index2 += 1
        k += 1

    while index1 < m:
        merged_array[k] = nums1[index1]
        index1 += 1
        k += 1

    while index2 < n:
        merged_array[k] = nums2[index2]
        index2 += 1
        k += 1

    nums1 = merged_array



nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(merge(nums1 , m , nums2 , n))