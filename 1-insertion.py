# input = 2 4 3 5
a = list(map(int, input().split()))
# a = [2, 4, 3, 5]
# a = [2, 4, 6, 8, 3]
# a = [1, 4, 3, 5, 6, 2]

index = 1
for value in a[index:]:
    key = value
    i = index - 1
    # Insert key into a[0..i-1]
    while i > -1 and a[i] > key:
        a[i+1] = a[i]
        i -= 1
    a[i+1] = key
    index += 1

print(a)
