i = 11010001111100111
j =list(reversed(list(str(i))))



h = []
n = 0
for digit in j:
    h.append(int(digit)*(2**n))
    n = n+1

print(sum(h))


print(hex(i))
print(oct(i))