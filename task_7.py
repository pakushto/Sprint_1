num = 99999135


def digit_root(num: int):
    root = 0
    for i in str(num):
        root += int(i)
    if root >= 10:
        return digit_root(root)
    else:
        return root


print(digit_root(num))
