from collections import deque

def isInfinity(left, right, N):
    if(left[1] >right[1]):
        big = left
        small = right
    else:
        big = right
        small = left   
    if((left[1] == right[1]) and N==2): 
        return 1
    elif(big[0] == "R" and small[0] == "L"):
        return 1
    elif((N == 2 or (big[0] == 'L' and small[0] == 'R')) and (small[1]+1 == big[1])):
        return 1
    elif(N ==2 and ((left[0] == 'L' and right[0] == 'L') or (left[0] =='R' and right[0] == 'R'))):
        return 1
    else:
        return 0

t = int(input())
while(t):
    N = int(input())
    t-=1
    n = N
    input_deque = deque()
    while(N):
        hints = input()
        hints = hints.split()
        hints[1] = int(hints[1])
        input_deque.append(hints)
        N-=1
    N=n
    if N==1:
        print(-1)
    else:
        count = 0
        deques = deque()

        while(N):
            deques.appendleft(input_deque.popleft())
            count+=1
            if(count>1):
                if(isInfinity(deques[0], deques[1], n)):
                    print(-1)
                    break
                elif(count>2):
                    count = 2
                    if(deques[1][0] == 'L'):
                        if(deques[0][0] == 'R'):
                            if(deques[2][0] == 'R'):
                                if(((deques[1][1]-1) <= deques[0][1]) or ((deques[1][1]-1) <= deques[2][1])):
                                    print(-1)
                                    break
                                else:
                                    deques = sorted(deques, key = lambda x: x[1], reverse=True)
                                    deques = deque(deques)
                                    deques.pop()
                            else: #deques[2][0] == 'L'
                                if(((deques[0][1]+1) >= deques[1][1]) or ((deques[0][1]+1) > deques[2][1])):
                                    print(-1)
                                    break
                                else:
                                    deques = sorted(deques, key = lambda x: x[1])
                                    deques = deque(deques)
                                    deques.pop() 
                        else:  #deques[0][0] == 'L'
                            if(deques[2][0] == 'R'):
                                if(((deques[2][1]+1) >= deques[0][1]) or ((deques[2][1]+1) >= deques[1][1])):
                                    print(-1)
                                    break
                                else:
                                    deques = sorted(deques, key = lambda x: x[1]) 
                                    deques = deque(deques)
                                    deques.pop()     
                            else:  #deques[2][0] == 'L'
                                deques = sorted(deques, key = lambda x: x[1]) 
                                deques = deque(deques)
                                deques.pop()
                    else: #deques[1][0] == 'R'
                        if(deques[2][0] == 'L'):
                            if(deques[0][0] == 'R'):
                                if(((deques[2][1]-1) <= deques[0][1]) or ((deques[2][1]-1) <= deques[1][1])):
                                    print(-1)
                                    break
                                else:
                                    deques = sorted(deques, key = lambda x: x[1], reverse=True)
                                    deques = deque(deques)
                                    deques.pop()
                            else: #deques[0][0] == 'L'
                                if(((deques[1][1]+1) >= deques[0][1]) or ((deques[1][1]+1) > deques[2][1])):
                                    print(-1)
                                    break
                                else:
                                    deques = sorted(deques, key = lambda x: x[1])
                                    deques = deque(deques)
                                    deques.pop()
                        else:  #deques[2][0] == 'R'
                            if(deques[0][0] == 'L'):
                                if(((deques[0][1]-1) <= deques[1][1]) or ((deques[0][1]-1) <= deques[2][1])):
                                    print(-1)
                                    break
                                else:
                                    deques = sorted(deques, key = lambda x: x[1], reverse=True) 
                                    deques = deque(deques)
                                    deques.pop()     
                            else:  #deques[0][0] == 'R'
                                deques = sorted(deques, key = lambda x: x[1], reverse=True) 
                                deques = deque(deques)
                                deques.pop()                         
            N-=1     
        if(N == 0):
            if(isInfinity(deques[0], deques[1], 2)):
                print(-1)
            else:
                print("%d" %(abs(deques[0][1] - deques[1][1]) -1))