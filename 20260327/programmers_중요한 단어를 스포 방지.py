# 공백의 인덱스만 저장을 하고, 공백의 인덱스에 다다를때까지 
# 좌,우로 나눠서 인덱스를 1씩 빼야겠는데?
# 문자의 인덱스 범위를 저장해야
# 스포일러 범위 안의 인덱스에서 문자가 공개되면 그 범위에 포함된 문자가 그 범위를 제외하고 메세지에 없으면 중요한 문자로 카운트 1 추가
# 문자 시작과 끝을 기록한 word_lst 생성

def solution(message, spoiler_ranges):
    answer = 0
    # 총 단어의 정보를 담을 word_lst
    # 각 단어를 기록하는 용도인 word
    # 인덱스 기록하는 idx_lst
    word_lst = []
    word = []
    idx_lst = []
    
    # 문자와 인덱스를 같이 보기
    for i, char in enumerate(message):
        
        
        # 띄어쓰기 만나면
        if char == ' ':
            if not idx_lst: 
                continue
            # 시작과 끝을 인덱스 리스트의 최대, 최소로 지정
            start, end = min(idx_lst), max(idx_lst)
            # 정보란에 단어, 시작과 끝의 인덱스 담기
            word_lst.append([''.join(word), start, end])
            # 단어와 인덱스리스트 초기화
            word.clear()
            idx_lst.clear()
            continue
        # 철자와 인덱스 추가    
        word.append(char)
        idx_lst.append(i)

    if word: # 마지막에 남은 단어가 있다면
        start, end = min(idx_lst), max(idx_lst)
        word_lst.append([''.join(word), start, end])
        
    # 가려지는 단어, 보이는 단어 지정        
    spoiled_words = []
    visibled_words = []
    
    for text, t_start, t_end in word_lst:
        # 처음엔 안 가려졌다고 가정
        is_spoiled = False
        # 가려지는 범위 순회
        for s, e in spoiler_ranges:
            
            if s <= t_end and e >= t_start: 
                is_spoiled = True
                break
        # 가려짐 여부에 따라서 리스트 추가                
        if is_spoiled:
            spoiled_words.append(text)
        else:
            visibled_words.append(text)
            
    # 가려진 단어가 보이는 단어에 없으면 중요한 단어임.          
    for word in set(spoiled_words): # 중복 방지를 위해 set으로 설정
        if word not in visibled_words:
            answer += 1
             
    return answer