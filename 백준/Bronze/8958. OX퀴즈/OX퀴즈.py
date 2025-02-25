t = int(input()) 
for _ in range(t):
    score_str = input() 
    total_score = 0
    current_score = 0
    for char in score_str:
        if char == 'O':
            current_score += 1
            total_score += current_score
        else:
            current_score = 0
    print(total_score)