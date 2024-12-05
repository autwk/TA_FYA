import re

print("Введите мн-во продукций P:")
temp = [x.split('->') for x in input().split()]
p = dict()
for i in temp:
    left, right = i[0], i[1]
    p[right] = left

table = []
print("Введите таблицу анализа(в конце 0)")
x = input()
while x != '0':
   table.append(x.split())
   x = input()
stolbik = {table[0][i]:i for i in range(len(table[0]))}
stroki = {table[i][0]:i for i in range(len(table))}
   
print("Введите текущую сентенциальную форму:")
x = input()

while x != 'S':
    r = x.find('>') - 1 if x.rfind('>')!=-1 else len(x)-1
    l = x.rfind('<') + 1 if x.rfind('<')!=-1 else 0

    sub = ''.join(re.split('[><=]', x[l:r+1]))
    tmp = p[sub]
    if l==0: left = ''
    else: left = table[stroki[x[l-2]]][stolbik[tmp]]
    if r==len(x)-1: right = ''
    else: right = table[stroki[tmp]][stolbik[x[r+2]]]
    res = x[:max(0,l-1)] + left + tmp + right + x[r+2:]
    x = res
    print(res)

'''Введите мн-во продукций P:
S->aA S->c A->Scb
Введите таблицу анализа(в конце 0)
- S A a b c
S - - - - =
A - - - - >
a < = < - <
b - - - - >
c - - - = >
0
Введите текущую сентенциальную форму:
a<a<c>c=b>c=b
a<a<S=c=b>c=b
a<a=A>c=b
a<S=c=b
a=A
S'''
