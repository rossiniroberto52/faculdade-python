t = int(input())
if t >= 1 and t <= 4:
    respostas = list(map(int, input().split()))
    print(respostas.count(t))
