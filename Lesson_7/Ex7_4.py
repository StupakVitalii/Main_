def num_1(x):
    def num_2(y):
        return x * y
    return num_2

func_4 = num_1(3)(4)
print(func_4)