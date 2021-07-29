def solution(n, computers):
    answer = 0
    comIdx = 0
    idx = 0
    
    netNum = len(computers)*2
    print(netNum)
    
    for computer in computers:
        print(computer)
        comlist = computer[comIdx:]
        print("comlist" + str(comlist))
        for linkStat in comlist:

            if linkStat == 1:
                netNum -= 1
            idx += 1
        print("Network Number ->" + str(netNum))
                 
        comIdx += 1
        
    answer = netNum
    print(answer)
    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]])
solution(5,	[[1, 1, 0, 0, 0], [1, 1, 1, 0, 0], [0, 1, 1, 0, 0 ],[0,0,0,1,1],[0,0,0,0,1]])
solution(5, [[1, 1, 1, 0, 0], [1, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 0, 0, 1, 1],[0, 0, 0, 1, 1]])
solution(4, [[1,1,1,1], [1,1,1,0], [1,1,1,0], [1,0,0,1]])
