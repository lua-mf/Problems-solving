const lines = [ 7, -5, 6, -3.4, 4.6, 12];

function contadorDeNumerosPositivos (entrada) {
    let count = 0;
    for (let i = 1; i <= 6; i++) {
        if (lines[i] >= 0) {
            count++;
        }
    }   

    console.log(`${count} valores positivos`)
}
contadorDeNumerosPositivos(lines);


