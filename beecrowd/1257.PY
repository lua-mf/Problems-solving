alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input())
for i in range(n):
  l = int(input())
  sum = 0
  for y in range(l):
    a = input()
    for indice, letra in enumerate(a): 
      valor = alfabeto.index(letra) + y + indice
      sum = sum + valor
  print(sum)
