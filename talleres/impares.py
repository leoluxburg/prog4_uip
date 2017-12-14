def impar():
  n = 200
  i = 1
  odds = []
  while i < n:
      odds.append(i),
      i += 2
  yield odds

numero = impar()
for n in numero:
  print(n)



