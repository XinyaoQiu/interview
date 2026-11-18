def one_over_n(n):
    if n == 1:
        return "1"
    digits = []
    seen = {}
    rem = 1
    while rem and rem not in seen:
        seen[rem] = len(digits)
        q, rem = divmod(rem * 10, n)
        digits.append(str(q))
    if rem:
        i = seen[rem]
        return "0." + "".join(digits[:i]) + "(" + "".join(digits[i:]) + ")"
    return "0." + "".join(digits)


def fraction_to_decimal(m, n):
    if m == 0:
        return "0"
    sign = "-" if (m < 0) != (n < 0) else ""
    m, n = abs(m), abs(n)

    integer, rem = divmod(m, n)
    if rem == 0:
        return sign + str(integer)

    digits = []
    seen = {}
    while rem and rem not in seen:
        seen[rem] = len(digits)
        q, rem = divmod(rem * 10, n)
        digits.append(str(q))
    if rem:
        i = seen[rem]
        frac = "".join(digits[:i]) + "(" + "".join(digits[i:]) + ")"
    else:
        frac = "".join(digits)
    return sign + str(integer) + "." + frac


print(one_over_n(2))
print(one_over_n(3))
print(one_over_n(6))
print(one_over_n(7))
print(one_over_n(1))

print(fraction_to_decimal(1, 2))
print(fraction_to_decimal(2, 1))
print(fraction_to_decimal(4, 333))
print(fraction_to_decimal(22, 7))
print(fraction_to_decimal(1, 6))
print(fraction_to_decimal(-50, 8))
print(fraction_to_decimal(7, -12))
print(fraction_to_decimal(0, -5))
print(fraction_to_decimal(-2147483648, -1))
