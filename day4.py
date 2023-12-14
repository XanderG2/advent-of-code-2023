with open("inputs/day4.txt", "r") as f:
    input = f.read()

lines = input.splitlines()

totalsum = 0

for line in lines:
    id = int(line.split()[1].split(":")[0])
    winning = line.split("|")[0].split(": ")[1].split()
    numbers = line.split("| ")[1].split()
    wins = 0
    for num in numbers:
        if num in winning:
            wins += 1
    print(f"Card {id}: {wins}")
    total = 0
    for x in range(wins):
        if x == 0:
            total = 1
        else:
            total *= 2
    totalsum += total

print(totalsum)