

inStr = input("문자열을 입력하세요 : ")
outStr = ""

upper,lower,digit,hangul,etc = [0]*5

for i in inStr:
    if i.isalpha():
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        else:
            hangul += 1
    elif i.isdigit():
        digit += 1
    else:
        etc += 1

print("대문자:%d, 소문자:%d, 숫자:%d, 한글:%d, 기타:%d" %(upper, lower, digit, hangul, etc))
