with open("inputs/day3.txt", "r") as f:
    input = f.read()

lines = input.splitlines()

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