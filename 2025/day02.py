fp = './inputs/day02.txt'
r = []

with open(fp, 'r') as f:
  ip = f.read().replace('\n', '').strip()

  for l in ip.split(','):
    if '-' in l:
      a, b = l.split('-')
      r.append( (int(a), int(b)) )

def iv1(n):
  le = len(str(n))
  if(le%2 != 0): return False
  h = le // 2

  return str(n).endswith(str(n)[:h])

def iv2(n):
  st = str(n)
  le = len(st)
  for i in range(1, le):
    if le % i == 0 and st == st[:i] * (le // i):
      return True

  return False

def part1(r):
  tt = 0
  for st, ed in r:
    for n in range(st, ed + 1):
      if iv1(n):
        tt += n

  return tt

def part2(r):
  tt = 0
  for st, ed in r:
    for n in range(st, ed + 1):
      if iv2(n):
        tt += n

  return tt

p1 = part1(r)
print('Part 1: ', p1)

p2 = part2(r)
print('Part 2: ', p2)
