from collections import *
import sys

def bfs(graph, visited,root):
  visited[root] = True
  que = deque([root])

  while que:
    start = que.popleft()
    print(start, end = ' ')
    for i in graph[start]:
      if not visited[i]:
        que.append(i)
        visited[i] = True
        
def dfs(graph, visited, root):
  visited[root] = True
  print(root, end = ' ')
  for i in graph[root]:
    if not visited[i]:
      dfs(graph, visited, i)


input = sys.stdin.readline

n,m,v = map(int, input().split())
arr = [[] for i in range(n+1)]
for i in range(m):
  a,b = map(int, input().split())
  arr[a].append(b)
  arr[b].append(a)

for i in range(1, n+1):
  arr[i].sort()

visited = [False] * (n+1)

dfs(arr,visited,v)
print()
visited = [False] * (n+1)
bfs(arr,visited,v)
