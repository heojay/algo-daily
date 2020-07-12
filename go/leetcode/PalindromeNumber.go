package leetcode

func isPalindrome(x int) bool {
	var elements []int
	ret := true
	if x < 0 {
		return false
	}
	for {
		if x < 10 {
			elements = append(elements, x)
			break
		}
		elements = append(elements, x%10)
		x /= 10
	}
	for i := 0; i < len(elements)/2; i++ {
		if elements[i] != elements[len(elements)-i-1] {
			ret = false
			break
		}
	}
	return ret
}
