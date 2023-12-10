with open("inputs/day2.txt", "r") as f:
    input = f.read()

lines = input.splitlines()

limits = {"red": 12, "green": 13, "blue": 14}

def partOne():
    gamesPassed = []
    totalId = 0

    for line in lines:
        id = int(line.split()[1].split(":")[0])
        sets = line.split(": ")[1].split("; ")
        passedRounds = 0
        setId = 0
        amounts = {}
        for set in sets:
            numbers = set.split(", ")
            for number in numbers:
                if str(setId) not in amounts:
                    amounts[str(setId)] = {"green": 0, "blue": 0, "red": 0}
                if number[-1] == "e":
                    amounts[str(setId)]["blue"] = int(number[0:2])
                elif number[-1] == "d":
                    amounts[str(setId)]["red"] = int(number[0:2])
                elif number[-1] == "n":
                    amounts[str(setId)]["green"] = int(number[0:2])
            setId += 1
        failed = 0
        for currentId in range(len(amounts)):
            if amounts[str(currentId)]["blue"] > limits["blue"]:
                failed += 1
            elif amounts[str(currentId)]["red"] > limits["red"]:
                failed += 1
            elif amounts[str(currentId)]["green"] > limits["green"]:
                failed += 1
        if failed == 0:
            gamesPassed.append(id)
            totalId += id
    
    print(totalId)

def partTwo():
    minimums = {}
    powers = {}

    for line in lines:
        id = int(line.split()[1].split(":")[0])
        setId = 0
        sets = line.split(": ")[1].split("; ")
        amounts = {}
        for set in sets:
            numbers = set.split(", ")
            for number in numbers:
                if str(setId) not in amounts:
                    amounts[str(setId)] = {"green": 0, "blue": 0, "red": 0}
                if number[-1] == "e":
                    amounts[str(setId)]["blue"] = int(number[0:2])
                elif number[-1] == "d":
                    amounts[str(setId)]["red"] = int(number[0:2])
                elif number[-1] == "n":
                    amounts[str(setId)]["green"] = int(number[0:2])
            setId += 1
        minimumNeeded = {"green": 0, "blue": 0, "red": 0}
        for currentId in amounts:
            for color, amount in amounts[str(currentId)].items():
                if amount > minimumNeeded[color]: minimumNeeded[color] = amount
        minimums[id] = minimumNeeded
    
    for gameId in minimums:
        powers[gameId] = 0
        for _, value in minimums[gameId].items():
            if powers[gameId] != 0:
                powers[gameId] *= value
            else: 
                powers[gameId] = value
    
    answer = 0
    for value in powers.values():
        answer += value
    
    print(answer)

partOne()
partTwo()