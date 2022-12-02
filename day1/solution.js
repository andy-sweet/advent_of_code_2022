const fs = require('fs');
const readline = require('readline');

async function* readElfCalories(path) {
  const file = fs.createReadStream(path);
  const lines = readline.createInterface({
    input: file,
    crlfDelay: Infinity
  });

  let cals = 0;
  for await (const line of lines) {
    if (line === '') {
      yield cals;
      cals = 0;
    } else {
      cals += parseInt(line)
    }
  }
  yield cals;
}

async function part1() {
  const cals = readElfCalories('input.txt');
  let maxCals = -Infinity;
  for await (const cal of cals) {
    maxCals = Math.max(cal, maxCals)
  }
  console.log(`max_cals: ${maxCals}`);
}

async function part2() {
  const cals = readElfCalories('input.txt');
  const topThree = [0, 0, 0];
  for await (const cal of cals) {
    if (cal > topThree[0]) {
      topThree[0] = cal
    }
    // Heapify
    const minTopThree = Math.min(...topThree);
    const index = topThree.indexOf(minTopThree);
    const tmp = topThree[index];
    topThree[index] = topThree[0]
    topThree[0] = tmp
  }
  const sumTopThreeCals = topThree.reduce((a, b) => a + b);
  console.log(`sumTopThreeCals: ${sumTopThreeCals}`);
}

part1();
part2();
