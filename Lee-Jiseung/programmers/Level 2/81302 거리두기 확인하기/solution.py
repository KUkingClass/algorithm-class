def solution(places):
    answer = []
    for place in places:
        flag = 1
        for i in range(5):
            if flag == 0:
                break
                
            for j in range(5):                    
                if place[i][j] != 'P':
                    continue
                    
                if (i+1 < 5 and place[i+1][j] == 'P') or (j+1 < 5 and place[i][j+1] == 'P'):
                    flag = 0
                    break
                    
                if (i+2 < 5 and place[i+2][j] == 'P' and place[i+1][j] != 'X') or (j+2 < 5 and place[i][j+2] == 'P' and place[i][j+1] != 'X'):
                    flag = 0
                    break
                
                if i+1 < 5 and j-1 >= 0 and place[i+1][j-1] == 'P' and (place[i][j-1] != 'X' or place[i+1][j] != 'X'):
                    flag = 0
                    break
                    
                if i+1 < 5 and j+1 < 5 and place[i+1][j+1] == 'P' and (place[i][j+1] != 'X' or place[i+1][j] != 'X'):
                    flag = 0
                    break
                    
        answer.append(flag)
    return answer