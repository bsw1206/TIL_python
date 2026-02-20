import sys

N = int(input())
raw_data = input().split()
tree = [0] + raw_data


def get_children(idx):
    if idx >= len(tree):
        return
    print(f"\n[노드 {tree[idx]} (인덱스 {idx})의 정보]")
    left_idx = idx * 2
    if left_idx < len(tree):
        print(f"왼쪽 자식: {tree[left_idx]} (인덱스 {left_idx})")
    else:
        print(" - 왼쪽 자식: 없음")
    right_idx = idx * 2 + 1
    if right_idx < len(tree):
        print(f" - 오른쪽 자식: {tree[right_idx]} (인덱스 {right_idx})")
    else:
        print(f" - 오른쪽 자식: 없음")
get_children(1)
get_children(2)
get_children(3)
    


    