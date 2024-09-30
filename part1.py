import re
import json
arr = []

with open('first-input.json') as f:
    arr = json.load(f)

newArr = []

for i in arr:

    numbOnly = re.sub("[^0-9]", "", (str)(i))

    numbArr = list(numbOnly)

    newArr.append(numbArr)

total = 0

for i in newArr:
    if len(i) == 1:
        total += (int)(i[0] + i[0])
    elif len(i) > 1:
        total += (int)(i[0] + i[len(i) - 1])
    else:
        continue

print(total)