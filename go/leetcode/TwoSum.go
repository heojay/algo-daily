package leetcode

func twoSum(nums []int, target int) []int {
	var ret []int

	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				ret = []int{i, j}
			}
		}
	}
	return ret
}
