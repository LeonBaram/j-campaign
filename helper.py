import re


def counter(curr, max=None, *reset):
    curr = curr if curr else "0 / 0"
    a, b = [x.strip() for x in curr.split('/')]
    max = max if max else b
    val = max if any(reset) else a
    return f'{val} / {max}'


def weight(item):
    pattern = r'(\d+x )?([\d.]+lb )?.+'
    match = re.fullmatch(pattern, item)
    if not match:
        return 0
    q, w = match.groups()
    q = q if q else "1"
    w = w if w else "0"
    q = float(q.strip(" x"))
    w = float(w.strip(" lb"))
    return q * w
