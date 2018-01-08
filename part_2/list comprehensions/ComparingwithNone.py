#Check whether the value is not None, and if it's greater than 30.
#Append the result of the check to checks.
#When finished, checks should be a list of Booleans indicating whether or not the corresponding items in values are not None and greater than 30.

values = [None, 10, 20, 30, None, 50]
checks = []

for item in values:
    if item is not None and item > 30:
        checks.append(True)
    else:
        checks.append(False)

print(values,'\n',checks)
