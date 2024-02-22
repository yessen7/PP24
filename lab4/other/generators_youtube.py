def topten():
    yield 1
    yield 2
    yield 3
    yield 4



values = topten()
print(values.__next__())
print(values.__next__())


def top_eleven():
    n = 1
    while n <= 11:
        sq = n*n
        yield sq
        n += 1


val = top_eleven()

for i in val:
    print(i)


