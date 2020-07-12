package leetcode

import "strconv"

func count(n string) string {
	ret := ""
	count := 1
	for i := 1; i < len(n); i++ {
		if n[i-1] != n[i] {
			ret += strconv.Itoa(count)
			ret += string(n[i-1])
			count = 0
		}
		count++
	}
	ret += string(n[len(n)-1])
	ret += string(n[len(n)-1])
	return ret
}

func countAndSay(n int) string {
	ans := "1"
	for i := 1; i < n; i++ {
		ans = count(ans)
	}
	return ans
}
