def italic(text):
    return ("italic", text)


def not_italic(text):
    return ("not_italic", text)


def parse_italic(html):
    result = []
    stack = []
    buf = []
    i = 0
    n = len(html)

    def flush():
        if buf:
            text = "".join(buf)
            result.append(italic(text) if stack else not_italic(text))
            buf.clear()

    while i < n:
        if html.startswith("<i>", i):
            flush()
            stack.append("i")
            i += 3
        elif html.startswith("</i>", i):
            if not stack:
                raise ValueError(f"unmatched </i> at index {i}")
            flush()
            stack.pop()
            i += 4
        else:
            buf.append(html[i])
            i += 1

    if stack:
        raise ValueError("unclosed <i>")
    flush()
    return result


print(parse_italic("this is not italic<i>this is italic</i>this is another not italic<i>this is another italic</i>"))
print(parse_italic("<i>start italic</i>end plain"))
print(parse_italic("a<i>b<i>c</i>d</i>e"))
print(parse_italic("plain only"))
print(parse_italic(""))
print(parse_italic("<i></i>"))
try:
    parse_italic("a</i>b")
except ValueError as e:
    print("error:", e)
try:
    parse_italic("a<i>b")
except ValueError as e:
    print("error:", e)
