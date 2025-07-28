n = int(input())
for i in range(n):
  a = input().split()
  msg = []
  for palavra in a:
    msg.append(palavra[0])
  print("".join(msg))