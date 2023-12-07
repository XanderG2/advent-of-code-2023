with open("inputs/day1.txt", "r") as f:
    input = f.read()

def partone():
    lines = input.splitlines()
    numbers = []
    answer = 0

    for line in lines:
        nums = ""
        for char in line:
            try: int(char)
            except: continue
            nums += char
        numbers.append(nums[0]+nums[-1])

    for number in numbers:
        answer += int(number)
    print(answer)

def parttwo():
    lines = input.splitlines()
    numbers = []
    answer = 0
    strnumbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    
    for line in lines:
        nums = ""
        charnum = 0
        for char in line:
            try: 
                int(char)
                nums += char
            except: 
                try:
                    if char == "o":
                        if line[charnum]+line[charnum+1]+line[charnum+2] == "one":
                            nums += "1"
                    elif char == "t":
                        if line[charnum]+line[charnum+1]+line[charnum+2] == "two":
                            nums += "2"
                        elif line[charnum]+line[charnum+1]+line[charnum+2]+line[charnum+3]+line[charnum+4] == "three":
                            nums += "3"
                    elif char == "f":
                        if line[charnum]+line[charnum+1]+line[charnum+2]+line[charnum+3] == "four":
                            nums += "4"
                        elif line[charnum]+line[charnum+1]+line[charnum+2]+line[charnum+3] == "five":
                            nums += "5"
                    elif char == "s":
                        if line[charnum]+line[charnum+1]+line[charnum+2] == "six":
                            nums += "6"
                        elif line[charnum]+line[charnum+1]+line[charnum+2]+line[charnum+3]+line[charnum+4] == "seven":
                            nums += "7"
                    elif char == "e":
                        if line[charnum]+line[charnum+1]+line[charnum+2]+line[charnum+3]+line[charnum+4] == "eight":
                            nums += "8"
                    elif char == "n":
                        if line[charnum]+line[charnum+1]+line[charnum+2]+line[charnum+3] == "nine":
                            nums += "9"
                except: pass
            charnum += 1
        numbers.append(nums[0]+nums[-1])

    for number in numbers:
        answer += int(number)
    print(answer)

partone()
parttwo()