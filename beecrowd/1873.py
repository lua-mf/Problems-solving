dic = {
		 "tesoura": ["papel", "lagarto"],
		 "papel": ["pedra", "spock"],
		 "pedra": ["lagarto", "tesoura"],
		 "spock": ["tesoura", "pedra"],
		 "lagarto": ["spock", "papel"]
}

n = int(input())
for i in range(n):
	a = input().split()
	if a[1] in dic[a[0]]:
		print('rajesh')
	elif a[0]==a[1]:
		print('empate')
	else:
		print('sheldon')