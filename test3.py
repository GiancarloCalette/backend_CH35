import json

colors = ['teal', 'PINK', 'PURPLE', 'ORANGE', 'green', 'BLUE', 'YELLOW', 'red', 'pink', 'TEaL', 'PurPLE', 'greEn', 'YELLOW', 'ORANGE', 'blue', 'RED', 'teal', 'PINk', 'purPle', 'orange', 'GREEN', 'BluE', 'YelLow', 'ReD']

results = []
for color in colors:
    color_lower = color.lower()
    if color_lower not in results:
        results.append(color_lower)
print(results)

color = "red"
counter = 0
for c in colors:
    if color == c.lower():
        counter +=1
print(counter)
