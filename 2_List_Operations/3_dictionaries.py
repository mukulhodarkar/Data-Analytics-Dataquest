#Count the number of times that each element occurs in the list named pantry that appears in the code block below.

pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts={}
for name in pantry:
    if name in pantry_counts:
        pantry_counts[name] += 1
    else:
        pantry_counts[name] = 1
print(pantry_counts)
