const fs = require('fs');
const readline = require('readline');

async function* readElfCalories(path) {
  const file = fs.createReadStream(path);
  const lines = readline.createInterface({
    input: file,
    crlfDelay: Infinity
  });

  let cals = 0
  for await (const line of lines) {
    if (line === '') {
      yield cals
      cals = 0
    } else {
      cals += parseInt(line)
    }
  }
  yield cals
}

async function main() {
  const cals = readElfCalories('input.txt');
  let maxCals = -Infinity
  for await (const cal of cals) {
    maxCals = Math.max(cal, maxCals)
  }
  console.log(`max_cals: ${maxCals}`);
}

main();
