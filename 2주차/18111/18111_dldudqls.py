#   n*m*반복횟수(minh에서 maxh까지) 가 10000이 넘지 않아야 1초 안에 들어온다고 함


import sys

n, m, block = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

minh = min(map(min, land))
maxh = max(map(max, land))
fint = float('inf')
finh = 0

for h in range(minh, maxh+1):
  t = 0
  tblock = block
  for x in range(n):
    for y in range(m):
      diff = land[x][y] - h
      if diff < 0:      
        tblock += diff * (-1)
        t += diff* (-1)
      else:  
        tblock -= diff 
        t += diff * 2
    
  if tblock >= 0: 
    if t <= fint:  
      fint = t
      finh = h

print(fint, finh)