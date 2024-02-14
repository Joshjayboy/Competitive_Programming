stops = int(input())
 
movements = []
while stops:
    args = list(map(int, input().split()))
    movements.append(args)
    stops -= 1
 
people_count = 0
min_needed_capacity = 0
 
for movement in movements:
    people_count += movement[1] - movement[0]
    if people_count > min_needed_capacity:
        min_needed_capacity = people_count
 
print(min_needed_capacity)