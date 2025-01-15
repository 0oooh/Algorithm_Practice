import sys
N = int(sys.stdin.readline())
count = 0  # '666'이 포함된 숫자의 개수
x = 666  # 가장 작은 '666'을 포함한 숫자부터 시작

while count < N:  # N번째 '666' 숫자를 찾을 때까지 반복
    if '666' in str(x):  # 현재 숫자 x에 '666'이 포함되어 있는지 확인
        count += 1  # 조건 만족 시 count 증가
        if count == N:  # N번째 '666'을 찾으면 출력
            print(x)
            break
    x += 1  #