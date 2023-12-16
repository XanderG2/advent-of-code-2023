with open("inputs/day3.txt", "r") as f:
    input = f.read()

lines = input.splitlines()

def partOne():
    total = 0

    for row in range(len(lines)):
        hasSymbol = False
        number = ""
        for col in range(len(lines[row])):
            if lines[row][col].isdigit():
                number += lines[row][col]
                minrow = max(0, row-1)
                mincol = max(0, col-1)
                maxrow = min(row+1, len(lines)-1)
                maxcol = min(col+1, len(lines[row])-1)
                for row_ in range(minrow, maxrow+1):
                    for col_ in range(mincol, maxcol+1):
                        char = lines[row_][col_]
                        if char not in list("1234567890."):
                            hasSymbol = True
                if col == len(lines[row])-1 or lines[row][col+1].isdigit() == False:
                    if hasSymbol:
                        total += int(number)
                    number = ""
                    hasSymbol = False

    print(total)

def partTwo():
    total = 0

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "*":
                numbers = []
                amountNumbers = 0
                minrow = max(0, row-1)
                mincol = max(0, col-1)
                maxrow = min(row+1, len(lines)-1)
                maxcol = min(col+1, len(lines[row])-1)
                for row_ in range(minrow, maxrow+1):
                    skip=0

                    for col_ in range(mincol, maxcol+1):
                        if skip > 0:
                            skip -= 1
                            continue
                        char = lines[row_][col_]
                        start = col_
                        end = col_
                        if char.isdigit():
                            if col_ == mincol:
                                while start > 0 and lines[row_][start-1].isdigit():
                                    start -= 1
                            while end < len(lines[row_])-1 and lines[row_][end+1].isdigit():
                                end += 1
                                skip += 1
                            number = lines[row_][start:end+1]
                            numbers.append(int(number))
                            amountNumbers += 1
                if amountNumbers == 2:
                    total += numbers[0] * numbers[1]
    print(total)

partOne()
partTwo()