fp = './inputs/day03.txt'
r = []

with open(fp, 'r') as f:
  for l in f:
    r.append(l.strip())

def part1(r):
  tt = 0

  for i in r:
    a = str(max(list(i[:-1])))
    b = str(max(list(i[i.index(a)+1:])))

    tt += int(a + b)

  return tt

def part2(r):
  tt = 0

  for i in r:
    d, rs, idx = 12, [], 0

    while d > 0:
      md, mi = -1, -1
      ei = len(i) - d + 1

      for j in range(idx, ei):
        if int(i[j]) > md:
          md = int(i[j])
          mi = j
      rs.append(str(md))
      idx = mi + 1
      d -= 1

    tt += int(''.join(rs))

  return tt

p1 = part1(r)
print('Part 1: ', p1)

p2 = part2(r)
print('Part 2: ', p2)
