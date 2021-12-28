

money = int(input("투입한 돈: "))
price = int(input("물건값: "))

a = money - price
print("거스름돈",a)
c500 = a // 500
a %= 500

c100 = a // 100
a %= 500

print("500원 동전의 개수:",c500)
print("100원 동전의 개수:",c100)
