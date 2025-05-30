//Exercicio A + B = C

console.clear()
const readline = require('readline-sync')
const A = readline.questionInt("Digite o valor de A:");
const B = readline.questionInt("Digite o valor de B:");
const C = readline.questionInt("digite o valor de C:");

if (A + B <C ) {
    console.log("A + B é menor que C.  ")
} else {
    console.log("A + B é maior que C .");
}