import { readFile } from "node:fs/promises";

const input = await readFile("inputs/day5.txt", "utf8");
const allLines = input.split("\n");
const firstLine = allLines[0];
// Line 2 is an empty line
const lines = allLines.slice(2);

const seedsText = firstLine.split(": ")[1];
const seedTexts = seedsText.split(" ");
const seeds = seedTexts.map((seedText) => parseInt(seedText, 10));

let maps = {};
let currentMap = "";

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  const s = line.split(" ");
  if (line.includes("map")) {
    currentMap = s[0];
    maps[currentMap] = { destinationrange: [], sourcerange: [] };
  } else if (line != "") {
    let currentObject = maps[currentMap];
    let drstart = parseInt(s[0], 10);
    let srstart = parseInt(s[1], 10);
    let rangelength = parseInt(s[2], 10);
    currentObject["destinationrange"].push([drstart, drstart + rangelength]);
    currentObject["sourcerange"].push([srstart, srstart + rangelength]);
  }
}

let locations = [];

for (let seedIndex = 0; seedIndex < seeds.length; seedIndex++) {
  let seed = seeds[seedIndex];
  let seedToEnd = seed;
  let containerNumsIn;
  for (const [key, { sourcerange, destinationrange }] of Object.entries(maps)) {
    let numInSource = false;
    for (let contId = 0; contId < sourcerange.length; contId++) {
      let container = sourcerange[contId];
      if (seedToEnd > container[0] && seedToEnd < container[1]) {
        numInSource = true;
        containerNumsIn = container;
      }
    }
    if (numInSource) {
      let difference = sourcerange.indexOf(containerNumsIn);
      let numIndex = seedToEnd - containerNumsIn[0];
      seedToEnd = destinationrange[difference][0] + numIndex;
    } else {
      seedToEnd = seedToEnd;
    }
  }
  locations.push(seedToEnd);
}

console.log(Math.min(...locations));
