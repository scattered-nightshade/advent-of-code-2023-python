import re
import json
arr = []

with open('part1-input.json') as f:
    arr = json.load(f)

newArr = []

for i in arr:

    regex="(?=([0-9]|one|two|three|four|five|six|seven|eight|nine|zero))"
    numbArr = re.findall(regex, (str)(i))

    for i in range(len(numbArr)):
        if numbArr[i-1] == "zero":
            numbArr[i-1] = "0"
        elif numbArr[i-1] == "one":
            numbArr[i-1] = "1"
        elif numbArr[i-1] == "two":
            numbArr[i-1] = "2"
        elif numbArr[i-1] == "three":
            numbArr[i-1] = "3"
        elif numbArr[i-1] == "four":
            numbArr[i-1] = "4"
        elif numbArr[i-1] == "five":
            numbArr[i-1] = "5"
        elif numbArr[i-1] == "six":
            numbArr[i-1] = "6"
        elif numbArr[i-1] == "seven":
            numbArr[i-1] = "7"
        elif numbArr[i-1] == "eight":
            numbArr[i-1] = "8"
        elif numbArr[i-1] == "nine":
            numbArr[i-1] = "9"
            
    newArr.append(numbArr)

total = 0

for i in newArr:
    total += (int)(i[0] + i[len(i) - 1])

print(total)
