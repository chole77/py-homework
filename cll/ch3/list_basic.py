a = [1, 2, 3]
b = [1, 'abc', 2.0, ['a', 'b', 'c']]
print(a)
print(b)

print('a[0]=', a[0])

# index
# print(a[0], a[1], sep='-', end='**')
print(a[0], a[1])

# 切片
c = b[1:3]
print(c, type(c))

s = 'abcdef'
print(s[1:3], s[-1])
print(b[-1])