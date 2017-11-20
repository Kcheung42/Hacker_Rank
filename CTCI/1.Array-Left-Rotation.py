def array_left_rotation(a, n, k):
    i = k % n
    split = n-i
    a[:] = reversed(a[:])
    a[0:split] = reversed(a[0:split])
    a[split:n] = reversed(a[split:n])
    return a

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
