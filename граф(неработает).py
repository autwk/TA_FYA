import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
print("Введите формальное представление графа")

print("Vn")
Vn = set(x for x in input().split())
for x in Vn:
  G.add_node(x)

print("Vt")
Vt = set(x for x in input().split())

print("Введите количество строк таблицы и саму функцию t:")
n = int(input())
for _ in range(n):
  a, b, c = input().split()
  G.add_edge(a, b, label=c)
nx.draw(G, with_labels = True)
print(G)
plt.show()