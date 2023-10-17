def sum_range(start, end):
    start = int(start)
    end = int(end)
    result = sum(range(start, end))
    if start > end:
        return sum(range(end, start))
    return result


func_1 = sum_range(100, 10)
print(func_1)