const fs = require('fs')
const lines = fs.readFileSync('input.txt', {encoding: 'utf-8'}).split('\r\n')
let grid = []
lines.forEach(line => grid.push(line.split('')))

// L === empty
// # === occupied
// . === floor


console.log(grid)