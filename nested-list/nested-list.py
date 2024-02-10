if __name__ == '__main__':
    
    score_map = {}
    score_list = []
    
    result = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        score_map[name] = score
    
    score_list.sort(reverse=False)
    
    least_score=score_list[0]
    
    for i in score_list:
        if i > least_score:
            least_score = i
            break 
    
    for name, score in score_map.items():
        if score == least_score:
            result.append(name)
    
    result.sort(reverse=False)
    
    for name in result:
        print(name)
        