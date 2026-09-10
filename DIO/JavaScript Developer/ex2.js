// 2) Faça um programa que receba N quantidade de números e seus respectivos valores.
// Imprima o maior número par e o menor número impar.

//     Exemplo:
//         Entrada:
//             5
//             3
//             4
//             1
//             10
//             8

//         Saída:
//             Maior número par: 10
//             Menor número impar: 1

const n = 5
const valores = [3, 4, 1, 10, 8]
let maiorNumeroPar = 0
let menorNumeroImpar = 11

for (let i = 0; i < n; i++) {
    if (valores[i] % 2 == 0) {
        if(valores[i] > maiorNumeroPar) {
            maiorNumeroPar = valores[i]
        }
    } else {
        if (valores[i] < menorNumeroImpar) {
            menorNumeroImpar = valores[i]
        }
    }
}

console.log('Maior número par: ', maiorNumeroPar, '\nMenor número impar: ', menorNumeroImpar)