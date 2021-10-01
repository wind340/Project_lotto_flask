import random

def randomNum(won: int)-> set:      #입력한 won값을 파라미터로 받아와서 넘겨준다
    lotto=[]                        #보여질 리스트값을 미리 선언
    for i in range(won):            #won의 값까지 돌려주는 반복문
        lotto.append(sorted(random.sample(range(1,46),6)))   
        #lotto list에 append시킨다. sorted로 정렬하고, random.sample로 임의의수를 받아온다(1부터46까지) 6자리.
    return lotto