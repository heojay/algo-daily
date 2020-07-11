package leetcode

import "strconv"

func reverse(x int) int {
	negFlag := false
	if x < 0 {
		x *= -1
		negFlag = true
	}
	stringX := strconv.Itoa(x)
	var reveredStringX string
	for _, v := range stringX {
		reveredStringX = string(v) + reveredStringX
	}
	var ret int
	ret, _ = strconv.Atoi(reveredStringX)
	if negFlag {
		ret *= -1
	}
	if ret < -2147483648 || ret > 2147483647 {
		ret = 0
	}

	return ret
}
