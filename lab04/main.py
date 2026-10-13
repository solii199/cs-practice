from stats import average_by_city, read_valid, warmest_city
import sys
line = sys.stdin.read().splitlines()
count = 0
if '' in line:
    count += 1
valid_line = read_valid(line)
best_city = warmest_city(valid_line)
best_temp = average_by_city(valid_line)[best_city]
print(len(valid_line))
print(len(line) - len(valid_line) - count)
print(best_temp)