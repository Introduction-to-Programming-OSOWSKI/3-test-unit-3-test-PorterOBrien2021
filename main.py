def countB(w):
    count = 0
    for i in range (0, len(w)):
        if w[i] == "b":
            count = (count + 1)
    return count
print(countB("baseball"))

def sumbetweenOdd(x, y):
    cat = 0
    for i in range(x + 1, y):
        if i % 2 == 1:
            cat = cat + i
    return cat

print(sumbetweenOdd(2, 10))








def firstLast(w):
    i = len(w)
    if w[0] == w[i-1]:
        return True
    else:
        return False

print(firstLast("no"))
