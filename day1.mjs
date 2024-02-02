import { readFile } from "node:fs/promises";

const input = await readFile("inputs/day1.txt", "utf8");
const lines = input.split("\n");

let numbers = [];
let answer = 0;
const check = /\d/g;

for (const line of lines) {
  const nums = line.match(check);
  const number = nums[0] + nums.slice(-1);
  numbers.push(parseInt(number));
}

for (const num of numbers) {
  answer += num;
}

console.log(answer);
