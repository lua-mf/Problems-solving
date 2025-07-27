# split divide o input(uma string) através dos espaços 
# map aplica a função int em cada elemento 
a, b, c = map(int, input().split()) 

maior_ab = (a + b + abs(a-b))/2
maior_abc = (maior_ab + c + abs(maior_ab-c))/2

print(int(maior_abc),"eh o maior")