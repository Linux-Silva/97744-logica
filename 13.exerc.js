const readline = require('readline-sync');

const numero = readline.questionInt('Digite o numero correspondente ao dia ');

if (numero == 1) {
    console.log("Segunda-feira");
    console.log("Dia útil");
} else if (numero == 2) {
    console.log("Terça-feira");
    console.log("Dia útil");
} else if (numero == 3) {
    console.log("Quarta-feira");
    console.log("Dia útil");
} else if (numero == 4) {
    console.log("Quinta-feira");
    console.log("Dia útil");
} else if (numero == 5) {
    console.log("Sexta-feira");
    console.log("Dia útil");
} else if (numero == 6) {
    console.log("Sábado");
    console.log("Final de semana");
} else if (numero == 7) {
    console.log("Domingo");
    console.log("Final de semana");
} else {
    console.log("Dia invalido.");
}
