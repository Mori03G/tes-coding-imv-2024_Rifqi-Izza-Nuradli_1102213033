angka = 9

for i in range(1, angka+1):
  i = i - (angka//2 +1)
  if i < 0:
    i = -i
  print(" " * i + "*" * (angka - i*2) + " "*i)