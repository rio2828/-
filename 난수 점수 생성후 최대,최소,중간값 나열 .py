
import random
import statistics

aa = []

for i in range(0, 11):
    one = random.randint(1,101)
    aa.append(one)


        
for i in range(0,11):
    print("%d번 : %d점"%((i+1), aa[i]))



print("")

    
print("최대값: %d"%max(aa))
print("최소값: %d"%min(aa))
print("중간값: %d"%statistics.median(aa))
