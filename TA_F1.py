from itertools import *

print("Введите элементы первого множества:")
L1 = set([x for x in input().split()])
print("Введите элементы второго множества:")
L2 = set([x for x in input().split()])

print("L1 U L2: ", L1 | L2)
print("L1 Ո L2: ", L1 & L2)
print("L1 \ L2: ", L1 - L2)
print("L2 \ L1: ", L2 - L1)

V1 = set(char for x in L1 for char in x)
V2 = set(char for x in L2 for char in x)
V = V1 | V2
V_ = set()
k = max(len(max(L1, key=len)), len(max(L2, key=len)))
for i in range(k):
  for x in product(V, repeat=i + 1):
    V_.add(''.join(x))

print("not L1 : Л,", sorted(V_ - L1, key=lambda x: (len(x), x)), "...")
print("not L2: Л,", sorted(V_ - L2, key=lambda x: (len(x), x)), "...")

ans1 = set()
for x in L1:
  for y in L2:
    ans1.add(x+y)
ans2 = set()
for x in L2:
  for y in L1:
    ans2.add(x+y)
print("L1*L2: ", sorted(ans1, key=lambda x: (len(x), x)))
print("L2*L1: ", sorted(ans2, key=lambda x: (len(x), x)))


