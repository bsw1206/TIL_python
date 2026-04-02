
import sys
move_lst = []
def hanoi_3(N, start, mid, end):
    if N == 0:
        return
    hanoi_3(N-1, start, end, mid)
    move_lst.append((start, end))
    hanoi_3(N-1, mid, start, end)

def hanoi_4(N, start, b, c, end):
    if N == 0:
        return
    if N == 1:
        move_lst.append((start, end))
        return
    hanoi_3(N-2, start, b, c)
    
    move_lst.append((start,b))
    move_lst.append((start,end))
    move_lst.append((b, end))
    hanoi_4(N-2, c, start, b, end)


N = int(sys.stdin.readline())

hanoi_4(N, 'A', 'B', 'C', 'D')
print(len(move_lst))
for s, e in move_lst:
    print(f'{s} {e}')