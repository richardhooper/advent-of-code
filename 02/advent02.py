f = open("input.txt", "r")

results = {}
results['A'] = {}
results['A']['X'] = 1 + 3
results['A']['Y'] = 2 + 6
results['A']['Z'] = 3 + 0
results['B'] = {}
results['B']['X'] = 1 + 0
results['B']['Y'] = 2 + 3
results['B']['Z'] = 3 + 6
results['C'] = {}
results['C']['X'] = 1 + 6
results['C']['Y'] = 2 + 0
results['C']['Z'] = 3 + 3

total = 0

for line in f:
    them = line[0]
    us = line[2]
    total += results[them][us]

print(total)

f.close()