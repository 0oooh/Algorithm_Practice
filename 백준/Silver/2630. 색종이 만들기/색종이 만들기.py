import sys

# 2630 색종이 만들기

def is_uniform(graph, x, y, size):
    num = graph[x][y]
    return all(graph[i][j] == num for i in range(x, x + size) for j in range(y, y + size))

def square(a, b, c, d, graph):
    global blue, white

    num = graph[a][c] 
    if all(graph[i][j] == num for i in range(a, b) for j in range(c, d)):
        if num == 1:
            blue += 1
        else:
            white += 1
        return  

    mid_x = (a + b) // 2
    mid_y = (c + d) // 2

    square(a, mid_x, c, mid_y, graph)  
    square(a, mid_x, mid_y, d, graph)  
    square(mid_x, b, c, mid_y, graph) 
    square(mid_x, b, mid_y, d, graph)  

blue = 0
white = 0
n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

square(0, n, 0, n, graph)

print(white)
print(blue)