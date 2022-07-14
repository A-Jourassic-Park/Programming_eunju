n, m = map(int, input().split())

arr = []
ds = []

for i in range(n):
    arr.append(list(map(int, input().split())))

cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
temp = []
check = [[0 for _ in range(n)] for _ in range(n)]

x = [0, -1, -1, 0, 1, 1, 1, 0, -1]
y = [0, 0, -1, -1, -1, 0, 1, 1, 1]

cx = [1, -1, 1, -1]
cy = [1, -1, -1, 1]

for i in range(m):
    d, s = map(int, input().split())
    for j in range(len(cloud)):
        cloud[j][0] += y[d] * s
        cloud[j][1] += x[d] * s
        if cloud[j][0] < 0:
            cloud[j][0] *= -1
            cloud[j][0] %= n
            if cloud[j][0] == 0:
                pass
            else:
                cloud[j][0] *= -1
                cloud[j][0] = n + cloud[j][0]
        elif cloud[j][0] >= n:
            cloud[j][0] %= n

        if cloud[j][1] < 0:
            cloud[j][1] *= -1
            cloud[j][1] %= n
            if cloud[j][1] == 0:
                pass
            else:
                cloud[j][1] *= -1
                cloud[j][1] = n + cloud[j][1]
        elif cloud[j][1] >= n:
            cloud[j][1] %= n

        arr[cloud[j][0]][cloud[j][1]] += 1

    for j in range(len(cloud)):
        check[cloud[j][0]][cloud[j][1]] = 1
        count = 0
        for k in range(4):
            if cloud[j][0] + cx[k] >= 0 and cloud[j][0] + cx[k] < n and cloud[j][1] + cy[k] >= 0 and cloud[j][1] + cy[k] < n:
                if arr[cloud[j][0] + cx[k]][cloud[j][1] + cy[k]] > 0:
                    count += 1
        arr[cloud[j][0]][cloud[j][1]] += count

    cloud = []
    for j in range(n):
        for k in range(n):
            if arr[j][k] >= 2 and check[j][k] == 0:
                arr[j][k] -= 2
                cloud.append([j, k])
            if check[j][k] == 1:
                check[j][k] = 0

answer = 0
for i in range(n):
    for j in range(n):
        answer += arr[i][j]

print(answer)