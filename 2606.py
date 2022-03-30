def enq(n):
    global rear 
    rear += 1
    Q[rear] = n
def deq():
    global front
    front += 1
    return Q[front]
def isEmp():
    return front == rear

V = int(input())
E = int(input())
adj = [[0]*(V+1) for _ in range(V+1)]
visited = []
Q = [0]*V
front = rear = -1

for _ in range(E):
    a,b = map(int, input().split())
    adj[a][b], adj[b][a] = 1,1

enq(1)
while not isEmp():
    t = deq()
    visited.append(t)
    for i in range(V+1):
            if adj[t][i] == 1:
                if i not in Q:
                    enq(i)
    
print(len(Q)-Q.count(0)-1)
