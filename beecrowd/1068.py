while True:
    try: 
        n = input()
    except EOFError:
        break
    b = 0
    for letra in n:
        if letra == '(': 
            b += 1
        elif letra == ')': 
            b -= 1
        if b < 0: # se tiver um ou mais ')' sem um '(' antes 
            break
    if b == 0:
        print('correct')
    else: # b < 0 ou b > 0 quer dizer que possui excesso de ')' ou '('
        print('incorrect')
