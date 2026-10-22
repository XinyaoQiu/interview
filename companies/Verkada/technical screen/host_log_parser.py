"""
Problem: Host Log Parser

Read a log file and yield one dictionary per nonblank line. Each line starts
with a timestamp followed by whitespace-separated key=value pairs.
Store the timestamp under "timestamp" and keep all field values as strings.

Assumptions to confirm with the interviewer:
- Every nonblank line is valid; no malformed-input handling is required.
- Timestamps use YYYY-MM-DDTHH:MM:SS or YYYY-MM-DD HH:MM:SS, optionally
  followed by fractional seconds and a timezone suffix such as Z or +00:00.
- Keys contain letters, digits, underscores, dots, or hyphens.
- Keys are unique within a line and do not use the reserved key "timestamp".
- There are no spaces around the equals sign.
- Unquoted values are nonempty and end at whitespace or the end of the line.
- Double-quoted values may be empty and may contain spaces, equals signs,
  escaped double quotes, and escaped backslashes. These are the only escapes.
- A quoted value stays on one physical line. The file uses UTF-8.

Approach:
Scan the line with one index. Read the timestamp, then repeat:
1. Skip whitespace and read the key up to the equals sign.
2. For an unquoted value, read until whitespace.
3. For a quoted value, read until the closing quote. A backslash escapes
   the next character, so append that character and skip both positions.
Iterate over the file directly and yield each parsed dictionary.

Complexity:
O(L) time and O(L) space per line of length L, including the parsed record.
Streaming keeps only the current line and record, not the entire file.
Memory is independent of the number of lines (not constant in line length).
"""

def parse_line(line):
    n = len(line)
    # Both timestamp formats have a 19-character date-and-time prefix.
    i = 19
    while i < n and not line[i].isspace():
        i += 1
    record = {"timestamp": line[:i]}

    while i < n:
        while i < n and line[i].isspace():
            i += 1
        if i == n:
            break

        start = i
        while line[i] != "=":
            i += 1
        key = line[start:i]
        i += 1  # Skip the equals sign.

        if line[i] == '"':
            i += 1  # Skip the opening quote.
            chars = []
            while line[i] != '"':
                if line[i] == "\\":
                    i += 1  # The next character is literal.
                chars.append(line[i])
                i += 1
            record[key] = "".join(chars)
            i += 1  # Skip the closing quote.
        else:
            start = i
            while i < n and not line[i].isspace():
                i += 1
            record[key] = line[start:i]

    return record


def parse_logs(path):
    with open(path, encoding="utf-8") as log_file:
        for line in log_file:
            if line.strip():
                yield parse_line(line)


# Mixed quoted and unquoted values; numbers remain strings.
print(parse_line(
    '2026-09-29T22:15:30Z host=cam-01 event="camera offline" '
    'status=failed retries=3'
))
# Expected: {'timestamp': '2026-09-29T22:15:30Z', 'host': 'cam-01',
#            'event': 'camera offline', 'status': 'failed', 'retries': '3'}

# A timestamp containing a space, repeated separators, and a tab.
print(parse_line(
    '2026-09-29 22:15:31.450   host=gw-99\tip=192.168.1.1 '
    'msg="handshake failed: connection reset" code=500'
))
# Expected: {'timestamp': '2026-09-29 22:15:31.450', 'host': 'gw-99',
#            'ip': '192.168.1.1', 'msg': 'handshake failed: connection reset',
#            'code': '500'}

# Escaped quotes, embedded equals signs, and an empty value.
print(parse_line(
    r'2026-09-29T22:15:33Z event="firmware update" '
    r'details="version=\"2.4.1\" reboot=true" note=""'
))
# Expected: {'timestamp': '2026-09-29T22:15:33Z', 'event': 'firmware update',
#            'details': 'version="2.4.1" reboot=true', 'note': ''}

# Preserve repeated spaces inside quotes and decode escaped backslashes.
print(parse_line(
    r'2026-09-29T22:15:34Z msg="two  spaces" path="C:\\logs"'
))
# Expected values: msg contains two spaces; path contains one backslash.

# Stream a file with: for record in parse_logs("host.log"): print(record)
