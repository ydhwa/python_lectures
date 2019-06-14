index = 0
for color in ['red', 'blue', 'green']:
    print('{0}: {1}'.format(index, color))
    index += 1

for index, color in enumerate(['red', 'blue', 'green']):
    print('{0}: {1}'.format(index, color))
