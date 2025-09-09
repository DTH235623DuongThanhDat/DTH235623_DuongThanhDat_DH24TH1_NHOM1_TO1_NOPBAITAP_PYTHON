def test(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print("i= ", i, "j= ", j, "k= ", k)
    test (3, 5, 7)
    test (3, 7, 5)
    test (5, 3, 7)
    test (5, 7, 3)
    test (7, 3, 5)
    test (7, 5, 3)