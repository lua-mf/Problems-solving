dic = {
		 "suco de laranja": 120,
		 "morango fresco": 85,
		 "mamao": 85,
		 "goiaba vermelha": 70,
		 "manga": 56,
		 "laranja": 50,
		 "brocolis": 34
}
while True:
	n = int(input())
	if n == 0:
		break
	sum = 0
	for i in range(n):
		t = input().split() 
	
		q = int(t[0]) 
		t.pop(0) # retira o inteiro da lista de entrada
		fruta = " ".join(t) # junta o resto da lista de entrada através de espaços formando uma única string

		sum = sum + q*dic[fruta]
	if sum > 130:
		print('Menos', sum - 130, 'mg')
	elif sum < 110:
		print('Mais', 110 - sum, 'mg')
	else:
		print(sum, 'mg')