with open("inputs/day1.txt", "r") as f:
    input = f.read()

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