var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

let fileira = lines[1]
let fileiraAuxiliar = []
//  Ao se colocar uma bola na nova fileira, ela ficará encostada em duas bolas da fileira anterior e sua cor será:

// Preta, se estiver encostada em duas bolas de mesma cor;
// Branca, se estiver encostada em duas bolas de cores diferentes.
for (let i = 0; i < fileira.length - 1; i++) {
    if (fileira[i] === fileira[i + 1]) {
        fileiraAuxiliar.push(1)
    } else {
        fileiraAuxiliar.push(-1)
    }
}
console.log(fileiraAuxiliar)