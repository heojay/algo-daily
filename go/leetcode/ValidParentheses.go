package leetcode

func isValid(s string) bool {
	var stack []rune

	for _, v := range s {
		if v == '(' || v == '[' || v == '{' {
			stack = append(stack, v)
		} else {
			if len(stack) >= 1 {
				n := len(stack) - 1
				if (v == ')' && stack[n] == '(') || (v == '}' && stack[n] == '{') || (v == ']' && stack[n] == '[') {
					stack = stack[:n]
				} else {
					return false
				}
			} else {
				return false
			}
		}
	}

	return len(stack) == 0
}
