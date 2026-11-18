def calculator(s):
    i = 0

    def helper():
        nonlocal i
        res, last, num, op = 0, 0, 0, '+'
        while i < len(s):
            ch = s[i]
            i += 1
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '(':
                num = helper()
            if ch in "+-*/)" or i == len(s):
                if op == "+": 
                    res += last
                    last = num
                elif op == "-": 
                    res += last
                    last = -num
                elif op == "*": 
                    last *= num
                elif op == "/": 
                    last = int(last / num)
                if ch == ')':
                    break
                op, num = ch, 0
        return res + last

    return helper()