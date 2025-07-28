leds = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]
n = int(input())
for i in range(n):
  sum = 0
  v = input()
  for num in v:
    sum = sum + leds[int(num)-1]
  print(sum, "leds")