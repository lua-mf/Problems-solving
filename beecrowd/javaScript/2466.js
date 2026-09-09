const n = 5 // número de bolas da primeira fileira
const primeiraFileira = [1, -1, 1, 1, -1] // preta = “1” ou branca = “-1”

//  Ao se colocar uma bola na nova fileira, ela ficará encostada em duas bolas da fileira anterior e sua cor será:

// Preta, se estiver encostada em duas bolas de mesma cor;
// Branca, se estiver encostada em duas bolas de cores diferentes.