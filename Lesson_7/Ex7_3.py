def get_filtered(a):
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in a:
        if i < 5:
            print([i], end='')
    return ('')


func_3 = get_filtered('a')
print(func_3)


