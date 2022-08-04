from itertools import *
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
answer = []
for i in range(n):
  answer.append(list(map(int, input().split())))

ch = []
home = []
for i in range(n):
  for j in range(len(answer[0])):
    if answer[i][j] == 1: home.append([i,j])
    elif answer[i][j] == 2: ch.append([i,j])

minv = 100000
for chicken in combinations(ch,m):
  sumv = 0
  for j in home:
    sumv += min([abs(j[0]-k[0])+abs(j[1]-k[1]) for k in chicken])
    if minv <= sumv: break
  if sumv < minv:
    minv = sumv

print(minv)