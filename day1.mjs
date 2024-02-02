import { readFile } from "node:fs/promises";

const input = await readFile("inputs/day1.txt", "utf8");
const lines = input.split("\n");

function partOne() {
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
}

function partTwo() {
  const numberToNumber = {
    one: "1",
    two: "2",
    three: "3",
    four: "4",
    five: "5",
    six: "6",
    seven: "7",
    eight: "8",
    nine: "9",
    zero: "0",
  };
  let numbers = [];
  let answer = 0;
  const check = /\d|one|two|three|four|five|six|seven|eight|nine|zero/g;

  const numberStrings = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "zero",
    ..."1234567890".split(""),
  ];
  for (const line of lines) {
    let firstIndex = Infinity,
      first = null;
    let lastIndex = -1,
      last = null;
    for (const numberString of numberStrings) {
      const i = line.indexOf(numberString);
      if (i >= 0 && i < firstIndex) {
        firstIndex = i;
        first = numberString;
      }
      const j = line.lastIndexOf(numberString);
      if (j >= 0 && j > lastIndex) {
        lastIndex = j;
        last = numberString;
      }
    }

    if (numberToNumber.hasOwnProperty(first)) {
      first = numberToNumber[first];
    }
    if (numberToNumber.hasOwnProperty(last)) {
      last = numberToNumber[last];
    }
    const number = first + last;
    console.log(number);
    numbers.push(parseInt(number, 10));
  }

  for (const num of numbers) {
    answer += num;
  }

  console.log(answer);
}

partOne();
partTwo();
