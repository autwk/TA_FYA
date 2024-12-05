print("Введите язык L:")
L = set([x for x in input().split()])
last = L
print("L+ :", last, end = " U ")
for i in range(3):
  temp = set()
  for x in last:
    for y in L:
      temp.add(x + y)
  last = temp
  print(last, end = " U ")
print("...")
