# #print(*[('* ' * i + '*').rjust(7 * 2 + i)
# #for i in range(15, 0, -1)], *[('* ' * i + '*').rjust(7 * 2 + i)
# #for i in range(15)], sep='\n')
#
#
# for i in range(15, 0, -2):
#     for j in range(i+1):
#         print('*', end='')
#     print('\r')

print(*[('* ' * i).rjust(7 * 2 + i)
for i in range(15, 1, -2)], *[('* ' * i).rjust(7 * 2 + i)
for i in range(1, 17, 2)], sep='\n')
