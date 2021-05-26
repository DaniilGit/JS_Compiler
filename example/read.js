module.exports.read_int = function() {
  const readline = require('readline');

  const rl = readline.createInterface({
    input: process.stdin
  });
  
  rl.on('line', (input) => {
    return +input
  });
  
  rl.close()
}
