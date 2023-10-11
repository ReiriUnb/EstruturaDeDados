from collections import deque

def max_in_sublists(lst, k):

    dq = deque()
    result = []


    for i in range(k):

        while dq and lst[i] >= lst[dq[-1]]:
            dq.pop()

        dq.append(i)


    for i in range(k, len(lst)):

        result.append(lst[dq[0]])

  
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and lst[i] >= lst[dq[-1]]:
            dq.pop()


        dq.append(i)

    result.append(lst[dq[0]])

    return result


N = int(input())
lst = list(map(int, input().split()))
k = int(input())

print('  '.join(map(str, max_in_sublists(lst, k))))
