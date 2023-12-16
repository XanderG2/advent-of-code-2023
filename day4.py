with open("inputs/day4.txt", "r") as f:
    input = f.read().strip()

lines = input.splitlines()

def partOne():
    totalsum = 0

    for line in lines:
        id = int(line.split()[1].split(":")[0])
        winning = line.split("|")[0].split(": ")[1].split()
        numbers = line.split("| ")[1].split()
        wins = 0
        for num in numbers:
            if num in winning:
                wins += 1
        total = 0
        for x in range(wins):
            if x == 0:
                total = 1
            else:
                total *= 2
        totalsum += total

    print(totalsum)

def partTwo():
    dupes = [1]*len(lines)
    totalScratchcards = 0
    for line in lines:
        id = int(line.split()[1].split(":")[0])
        winning = line.split("|")[0].split(": ")[1].split()
        numbers = line.split("| ")[1].split()
        wins = 0
        for num in numbers:
            if num in winning:
                wins += 1
        for x in range(id, id+wins):
            try: dupes[x] += 1 * dupes[id-1]
            except: 
                print(f"failed. {x}")
    for x in dupes:
        totalScratchcards += x
    print(totalScratchcards)

partOne()
partTwo()