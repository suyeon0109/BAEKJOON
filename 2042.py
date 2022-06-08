N, M, K = map(int, input().split())
la = [int(input()) for _ in range(N)]

tree = [0]* (N*4)

def sum_tree(start, end, node):

    if start == end:
        tree[node] = la[start]
        return tree[node]
    
    mid = (start + end)//2
    tree[node] = sum_tree(start, mid, node*2) + sum_tree(mid+1, end, node*2+1)
    return tree[node]


def calc_tree(start, end, node, left, right):

    if left > end or right < start:
        return 0
    
    elif left <= start and right >= end:
        return tree[node]
    
    mid = (start+end)//2

    return calc_tree(start, mid, node*2, left, right) + calc_tree(mid+1, end, node*2+1, left, right)


def update(start, end, node, index, dif):

    if index < start or index > end:
        return
    
    tree[node] += dif - la[index-1]

    if start == end:
        return
    
    mid = (start + end) // 2
    update(start, mid, node*2, index, dif)
    update(mid+1, end, node*2+1, index, dif)


sum_tree(0, N-1, 1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, N, 1, b, c)
        la[b-1] = c
    else:
        print(calc_tree(1, N, 1, b, c))