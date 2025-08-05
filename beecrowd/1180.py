n = int(input())
nums = list(map(int, input().split()))
print(f'Menor valor: {min(nums)}\nPosicao: {nums.index(min(nums))}')