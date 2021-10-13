import pandas as pd
import os
import random
from matplotlib import pyplot as plt


#랜덤 리스트 함수

def random_List(size):

    result = []

    for v in range(size):

        result.append(random.randint(0, 100))

 

    return result

 

#동작 확인

result = random_List(10)

print(result)

 

result = random_List(1000)

result.sort()


plt.bar(range(len(result)), result)

plt.show()