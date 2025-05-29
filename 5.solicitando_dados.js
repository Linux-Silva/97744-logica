// instalar: npm install readline-sinc

const readline = require('readline-sinc')

const idade = readline.questionint('digite sua idade:')

if (idade < 18 ) {
    console.log('menor de idade')
} else {
    console.log('maior de idade')
}