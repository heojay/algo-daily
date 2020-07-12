package leetcode

func longestCommonPrefix(strs []string) string {
	if len(strs) > 0 {
		i := 0
		for {
			flag := true
			temp := strs[0][:i]
			for _, v := range strs[1:] {
				if len(v) < i || v[:i] != temp {
					flag = false
					break
				}
			}
			if flag {
				if len(strs[0]) == i {
					break
				}
				i++
			} else {
				i--
				break
			}
		}
		return strs[0][:i]
	}
	return ""
}
