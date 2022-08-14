# https://codeforces.com/contest/1712/problem/A

for t in range(int(input())):
    n, k = map(int, input().split())
    inputList = list(map(int, input().split()))
    kList = inputList[:k+1]
    nList = inputList[k+1:n]
    numSwaps = 0

    for i in range(k):
        a = max(kList)
        b = min(nList)
        if b > a:
            temp = a
            b = a
            a = b
