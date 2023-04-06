import sys

def kuriyama(question, points, x, y):
    if question == 1:
        return sum(points[x-1:y])
    else:
        points.sort()
        return sum(points[x-1:y])

inputs = []
while True:
    line = input("")
    if line == "":
        break
    else :
        inputs.append(line)

pointStr = inputs[1].split(" ")
questionStr = [s.split(" ") for s in inputs[3:]]

points, questions = [int(s) for s in pointStr], [[int(s) for s in innerList] for innerList in questionStr]

results = []

for question in questions:
    result = kuriyama(question[0], points, question[1], question[2])
    results.append(result)

print(results)