#Append any names in planet_names that are longer than 5 characters to long_names. Otherwise, append the names to short_names.

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []

for name in planet_names:
    if len(name) > 5:
        long_names.append(name)
    else:
        short_names.append(name)
print("Long Names:")
print(long_names)
print("\nShort Names:")
print(short_names)
