# Keys are string of length 4 using only 1 and 0
#   e.g. 1101
# The keys represent [up, down, left, right]
# The corresponding ascii character is returned
path_lookup: dict[str, str] = {
    "1100": '║',
    "0011": '═',
    "0101": '╔',
    "0110": '╗',
    "1001": '╚',
    "1010": '╝',
    "1111": '╬',
    "1101": '╠',
    "1011": '╩',
    "0111": '╦',
    "1110": '╣'
}