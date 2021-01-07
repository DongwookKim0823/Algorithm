n = int(input())

result = 0

for a in range(n+1):
  if a == 3 or a == 13 or a == 23:
    result += 1*6*10*6*10
    continue
  for b in range(6):
    if b == 3:
      result += 1*10*6*10
      continue
    for c in range(10):
      if c == 3:
        result += 1*6*10
        continue
      for d in range(6):
        if d == 3:
          result += 1*10
          continue
        for e in range(10):
          if e == 3:
            result += 1
            continue         

print(result)