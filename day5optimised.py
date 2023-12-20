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
        destinationRange = [value[dictionaryno]["drstart"], value[dictionaryno]["drstart"]+value[dictionaryno]["rlength"]]
        sourceRange = [value[dictionaryno]["srstart"], value[dictionaryno]["srstart"]+value[dictionaryno]["rlength"]]
        if mapsComplete[key] == {}:
            mapsComplete[key] = {"destinationRange": [destinationRange], "sourceRange": [sourceRange]}
        else:
            mapsComplete[key]["destinationRange"].append(destinationRange)
            mapsComplete[key]["sourceRange"].append(sourceRange)

print(mapsComplete)

locationNums = []

for seed in seeds:
    currentNum = seed
    for key, map in mapsComplete.items():
        currentNumInSource = False
        for container in map["sourceRange"]:
            if currentNum > container[0] and currentNum < container[1]:
                currentNumInSource = True
                sourceCurrentNumIsIn = container
        if currentNumInSource:
            numIndex = currentNum - sourceCurrentNumIsIn[0]
            listNumber = map["sourceRange"].index(sourceCurrentNumIsIn)
            currentNum = map["destinationRange"][listNumber][0] + numIndex
        else:
            currentNum = currentNum
    locationNums.append(currentNum)

print(min(locationNums))