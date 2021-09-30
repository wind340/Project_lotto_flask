import random

def randomNum(won: int)-> set:
    lotto=[]
    for i in range(won):
        lotto.append(sorted(random.sample(range(1,46),6)))

    return lotto