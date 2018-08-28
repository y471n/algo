def merge(a, f, m, l):
    # Create temp arrays filled with 0's
    # Create separate lists filled from a[f..m-1] and a[m..l]
    print(a, f, m, l)
    n1 = m - f + 1
    n2 = l - m
    a1, a2 = [0]*n1,[0]*n2
    # a1, a2 = [], []

    for i in range(0, n1):
        a1[i] = a[f+i]
    for j in range(0, n2):
        a2[j] = a[m+j]

    i, j, k = 0, 0, f
    # Merge both arrays back into a
    while i < n1 and j < n2:
        if a1[i] <= a2[j]:
            a[k] = a1[i]
            i += 1
        else:
            a[k] = a2[j]
            j += 1
        k += 1

    # Copy remaining values of a1 and a2 to a
    while i < n1:
        a[k] = a1[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = a2[j]
        j += 1
        k += 1
    # print(a)


def merge_sort(a, f, l):
    if f < l:
        m = (f + (l + 1)) // 2
        merge_sort(a, f, m)
        merge_sort(a, m+1, l)
        merge(a, f, m, l)


# a = [10, 4, 8, 1, 2, 9]
a = [3, 2]
merge_sort(a, 0, len(a)-1)
print(a)
