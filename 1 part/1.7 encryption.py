def encrypt(s):
    lis = list(s)
    lis[: len(s) // 2 * 2:2], lis[1::2] = lis[1::2], lis[: len(s) // 2 * 2:2]
    return ''.join(lis)
