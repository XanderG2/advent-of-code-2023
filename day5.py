#this is extremely slow do not run

with open("inputs/day5.txt", "r") as f:
    input = f.read()

lines = input.splitlines()[2:-1]

seeds = [int(num) for num in input.splitlines()[0].split(": ")[1].split()]
maps = {}
currentMap = ""

for line in lines:
    if "map" in line:
        currentMap = line.split(":")[0].split()[0]
        maps[currentMap] = []
    elif line != "":
        currentDictionary = {}
        currentDictionary["drstart"] = int(line.split()[0])
        currentDictionary["srstart"] = int(line.split()[1])
        currentDictionary["rlength"] = int(line.split()[2])
        maps[currentMap].append(currentDictionary)

mapsComplete = {}

for key, value in maps.items():
    mapsComplete[key] = {}
    for dictionaryno in range(len(value)):
        destinationRange = range(value[dictionaryno]["drstart"], value[dictionaryno]["drstart"]+value[dictionaryno]["rlength"])
        sourceRange = range(value[dictionaryno]["srstart"], value[dictionaryno]["srstart"]+value[dictionaryno]["rlength"])
        if mapsComplete[key] == {}:
            mapsComplete[key] = {"destinationRange": list(destinationRange), "sourceRange": list(sourceRange)}
        else:
            mapsComplete[key]["destinationRange"] += destinationRange
            mapsComplete[key]["sourceRange"] += list(sourceRange)

locationNums = []

for seed in seeds:
    currentNum = seed
    for key, map in mapsComplete.items():
        if currentNum in map["sourceRange"]:
            numIndex = map["sourceRange"].index(currentNum)
            currentNum = map["destinationRange"][numIndex]
        else:
            currentNum = currentNum
    locationNums.append(currentNum)

print(min(locationNums))