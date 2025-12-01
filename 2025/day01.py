fp = './inputs/day01.txt'
r = []

with open(fp, 'r') as f:
  for l in f:
    r.append(l.strip())

def part1(r):
  di = 50
  c = 0    

  for m in r:
      i = m[0]
      d = int(m[1:])

      if i == 'L':
          di = (di - d) % 100
      else:
          di = (di + d) % 100

      if di == 0:
          c += 1

  return c

def part2(r):
  di = 50
  c = 0    

  for m in r:
      i = m[0]
      d = int(m[1:])
      st = -1 if i == 'L' else 1

      for _ in range(d):
        di = (di + st) % 100
        if di == 0:
            c += 1

  return c

p1 = part1(r)
print('Part 1: ', p1)

p2 = part2(r)
print('Part 2: ', p2)