from stats import average_by_city, read_valid, warmest_city
import sys
lines = sys.stdin.read().splitlines()
count = 0

for line in lines:
    if line.strip():
        count += 1

valid_line = read_valid(line)
best_city = warmest_city(valid_line)

print(len(valid_line))
print(count - len(valid_line))

if best_city:
    best_temp = average_by_city(valid_line)[best_city]
    print(f'{best_temp:.1f}')
else:
    print('0.0')