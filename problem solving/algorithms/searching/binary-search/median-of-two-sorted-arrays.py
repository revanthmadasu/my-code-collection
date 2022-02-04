def findMedianSortedArrays(nums1, nums2):
    nums1Len = len(nums1)
    nums2Len = len(nums2)
    totalElements = nums1Len + nums2Len
    half = totalElements//2
    # nums1 should always be greater
    if nums2Len > nums1Len:
        nums1,nums2 = nums2,nums1
        nums1Len,nums2Len = nums2Len, nums1Len
    if nums1Len%2 == 1:
        nums1Median = nums1[nums1Len//2]
    else:
        nums1Median = (nums1[nums1Len//2] + nums1[(nums1Len//2)+1])/2
    l, r = 0, (nums2Len - 1)
    m = (l+r)//2
    direction = nums1Median > nums2[m]
    while abs(l-r) > 1:
        print(f'l is {l}, r is {r}')
        m = (l+r)//2
        if nums2[m] > nums1Median:
            #
            r = m
        elif nums2[m] < nums1Median:
            #
            l = m
        else:
            #
            l = m-1
            r = m+1
            break
    print(f'l is {l}, r is {r}')
    


nums1 = [2,4,6,8,10,12,14]
nums2 = [5,7,9,11,13,15]

findMedianSortedArrays(nums1, nums2)