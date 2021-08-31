
print([x for x in range(100) for y in range(2,x) if (x%y!=0) ])
# def prime_generator(end):
#     for n in range(2, end):
#         for x in range(2, n):
#             if n % x == 0:
#                 break
#         else:
#             yield n
#
#
# g = prime_generator(100)
# print(list(g))

