x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        location = 1
    else:
        location = 4
else:
    if y > 0:
        location = 2
    else:
        location = 3

print(location)