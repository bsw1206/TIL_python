import sys
sys.stdin = open('swea_5203_베이비진 게임.txt')

# triplet은 확인하기 간단하지만 run은 확인하기 복잡하므로 따로 함수 생성
def check_run(lst): 
    # 어차피 8부터는 run을 만들수가 없으므로 0~7까지만 보기
    for n in range(8): 
        if lst[n] != 0 and lst[n+1] != 0 and lst[n+2] != 0:
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    n_lst = list(map(int, input().split()))

    # 0~9까지의 카운트를 담기
    p1_cnt = [0] * 10
    p2_cnt = [0] * 10
    
    # 결과값 미리 지정(조건 만족 안할 경우 0 출력)
    result = 0

    for i in range(0, 12, 2):

        # 번갈아가면서 추가하기
        p1_cnt[n_lst[i]] += 1
        p2_cnt[n_lst[i + 1]] += 1

        # 리스트 안에 3이 있거나(triplet확인 여부)
        # run이 있으면 승자 출력
        if 3 in p1_cnt or check_run(p1_cnt):
            result = 1
            break
        elif 3 in p2_cnt or check_run(p2_cnt):
            result = 2
            break

    print(f'#{tc} {result}')
