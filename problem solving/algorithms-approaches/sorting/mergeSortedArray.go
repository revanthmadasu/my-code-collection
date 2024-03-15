/*
	problem: https://leetcode.com/problems/merge-sorted-array/
	concepts: arrays, two pointers, sorting
	performance: runtime 58.82%; memory 15.51%;
    approach - 2 pointer approach
*/

func merge(nums1 []int, m int, nums2 []int, n int) {
	var (
		i_m = 0
		i_n = 0
		i_r = 0
	)
	var listSize int
	listSize = m + n
	resNums := make([]int, listSize)
	if n == 0 {
		return
	}
	for i_r < listSize && i_m < m && i_n < n {
		if nums1[i_m] < nums2[i_n] {
			resNums[i_r] = nums1[i_m]
			i_m += 1
		} else {
			resNums[i_r] = nums2[i_n]
			i_n += 1
		}
		i_r += 1
	}
	if i_m < m {
		for i_m < m {
			resNums[i_r] = nums1[i_m]
			i_m++
			i_r++
		}
	}
	if i_n < n {
		for i_n < n {
			resNums[i_r] = nums2[i_n]
			i_n++
			i_r++
		}
	}

	for i := 0; i < listSize; i++ {
		nums1[i] = resNums[i]
	}
}