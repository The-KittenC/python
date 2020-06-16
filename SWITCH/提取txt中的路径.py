import sys
result = []
with open ("path.txt", "r") as f:
    for line in f:
        result.append(list(line.strip('\n').split(",")))
print(result)