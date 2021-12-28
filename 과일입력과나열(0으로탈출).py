
aa = []
print("===좋아하는 과일 등록 프로그램===")

a = True

while a:
    fruit = str(input("과일명 입력: "))
    if fruit == '0':
        a = False
        break
    aa.append(fruit)


print("당신이 좋아하는 과일들: ",aa)
