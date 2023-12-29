import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

def parse_headers(line: str) -> tuple[str, str]:
    ind = 0

    while line[ind] == '#':
        ind += 1

    if ind == 0:
        return ("block", line)
    else:
        return (f"h{ind}", line[ind:].strip())

parsed = list()


for line in lines:
    pass
