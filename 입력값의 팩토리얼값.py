
def factorial():
    i = 1
    fact = 1
    a = int(input("입력: "))
    if a <= 0:
        
        return print("이용해 주셔서 감사합니다.")
        quit()

    
    while True:
        fact *= i
        i += 1
        if i>a:
            break

    return print(a,"! = ",fact)

print(factorial())

