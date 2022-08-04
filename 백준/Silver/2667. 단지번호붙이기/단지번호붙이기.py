from collections import *
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(graph, a,b):
  que = deque()
  que.append((a,b))
  graph[a][b] = 0
  count = 1

  while que:
    x,y = que.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        que.append((nx,ny))
        count += 1
  return count

n = int(input())
answer = []
for i in range(n):
  answer.append(list(map(int, input())))

cnt = []
for i in range(n):
  for j in range(n):
    if answer[i][j] == 1:
      cnt.append(bfs(answer,i,j))
cnt.sort()
print(len(cnt))
for i in cnt:
  print(i)