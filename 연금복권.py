import random


print("<연금복권 번호 자동 생성기>")
print("----------------------------------")
print("게임 수를 입력하세요(숫자만 입력).")

num = input("게임 수 : ")

print("----------------------------------")

for i in range(0,int(5)):
    pension_lotto_tim = random.randrange(1,6)
    pension_lotto = random.randrange(1,10000000)
    print(pension_lotto_tim,'조', pension_lotto)

print("----------------------------------")
print("연금복권 번호 자동 생성 완료")
print("----------------------------------")
