def solution(signals):
    
    sum_signals = []
    for lights in signals:
        # 
        green = lights[0]
        
        yellow = lights[0] + lights[1]
        
        red = lights[0] + lights[1] + lights[2]
        
        sum_signals.append((green, yellow, red))
        
    
    answer = 0
    
    while answer < 5000000:
        
        answer += 1
        color_lst = [] 
        
        for green, yellow, red in sum_signals:
            cur_time = answer % red
            
            if cur_time == 0:
                cur_time = red  
                
            if cur_time <= green:
                color_lst.append(0)
                
            elif cur_time <= yellow:
                color_lst.append(1)
                
            elif cur_time <= red:
                color_lst.append(2)
                
        if set(color_lst) == {1}:
            return answer
            
    return -1