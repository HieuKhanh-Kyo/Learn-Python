# Viet CT trao doi phan tu dau voi phan tu cuoi trong list, phan tu thu 2 voi phan tu thu n-1 (gia su co n phan tu)

# a = [4,2,6,7,9,8]
# n = len(a)
#
# for i in range(n // 2):
#     gt = a[i]
#     a[i] = a[n - 1 - i]
#     a[n - 1 - i] = gt
#
# print(a)


# Tinh gia tri cua da thuc:  P = a0 + a1x + a2x^2 + ... + anx^n

n = int(input("n = "))
x = int(input("x = "))
p = 0

for i in range(n+1):
    p += i * x**i

print(p)
