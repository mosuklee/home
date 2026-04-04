const fs = require('fs')
var data = fs.readFileSync('data.json', 'utf8');
var words = JSON.parde(data);
var bodyparser = require('body-parser');
console.log(words);