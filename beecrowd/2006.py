t = int(input())
# map retorna um objeto do tipo map, não uma lista
# list tranforma o objeto do tipo map em uma lista
answers = list(map(int,input().split()))
print(answers.count(t))