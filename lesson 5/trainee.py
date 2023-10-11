var4 = ((1, 2), (2, 3), (3, 4))
print(var4)

var4 = list(var4)

print(type(var4))
print(var4)
var4.append((4, 5))
print(var4)
var4 = tuple(var4)
print(var4)

for i in var4:
    print(i)