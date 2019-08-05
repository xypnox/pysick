def merge(A, p, a, q):
    B = A[p:a]
    C = A[a:q]
    i, b, c = p, 0, 0

    while i < q:
        if b == len(B) or c == len(C):
            break
        elif B[b] < C[c]:
            A[i] = B[b]
            b += 1
        else:
            A[i] = C[c]
            c += 1
        i += 1

    while c < len(C) and i < q:
        A[i] = C[c]
        i += 1
        c += 1

    while b < len(B) and i < q:
        A[i] = B[b]
        i += 1
        b += 1


def mergeSort(A, p, q):
    a = (p+q)//2
    if p == a:
        return
    else:
        mergeSort(A, p, a)
        mergeSort(A, a, q)

    merge(A, p, a, q)


Arr = [1, 4, 3, 8, 7, 9, 5, 6, 2, 10]

print(Arr)
mergeSort(Arr, 0, len(Arr))
print(Arr)
