from collections import *
import sys

arr = []
n, m = map(int, input().split())
for i in range(n):
    arr.append(list(map(int, input())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(graph, root):
  que = deque()
  que.append(root)
  count = 1
  while que:
    x, y = que.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx<0 or ny<0 or nx >= n or ny >= m or graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        que.append((nx,ny))
        graph[nx][ny] = graph[x][y] + 1
      
  return graph[n-1][m-1]

temp = [0,0]
print(bfs(arr, temp))
      
    