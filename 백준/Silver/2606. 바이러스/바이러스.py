from collections import *
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

num = [i for i in range(n+1)]
graph = [[] for i in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n+1)

def bfs(graph, visited, root):
  que = deque()
  que.append(root)
  visited[root] = True
  count = 0
  while que:
    v = que.popleft()
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        que.append(i)
        count += 1
  return count

print(bfs(graph,visited,1))