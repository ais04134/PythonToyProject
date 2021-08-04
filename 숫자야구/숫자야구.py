import os
import random

print("=" * 45)
print("도전! 숫자야구".center(38))
print("=" * 45)
print("")

trial = 0

length = input("""난이도를 설정합니다!
3~5사이의 자릿수를 숫자로 입력하세요 : """)

while True:
    if length == "":
        length = input("!!!아무것도 입력하지 않았습니다!!! : ")
    elif int(length) < 3 or int(length) > 5:
        length = input("!!!3~5사이의 숫자만 가능합니다!!! : ")
    else:
        break

password = random.sample(range(0, 10), int(length))

while True:
    answer = input("중복되지 않는 %s자리 숫자를 입력하세요 : " % length)
    if int(len(answer)) != int(length):
        print("!!!%s자리 숫자가 아닙니다!!!" % length)
        continue
    elif len(set(list(answer))) != len(answer):
        print("!!!중복되는 수가 있습니다!!!")
        continue

    else:

        strike = 0
        ball = 0
        out = 0

        for i in range(int(length)):
            for j in range(int(length)):
                if int(answer[i]) == int(password[j]) and i == j:
                    strike = strike + 1
                elif int(answer[i]) == int(password[j]) and i != j:
                    ball = ball + 1
        if int(ball) == 0 and int(strike) == 0:
            out = 1

        trial = trial + 1

        print("%d strike" % strike)
        print("%d ball" % ball)
        print("%d out" % out)
        print("%d번 시도함" % trial)
        print("-" * 45)

        if strike == int(length):
            break

print("")
print("=" * 45)
print("게임종료")
print("정답은 : " + ''.join(list(map(str, password))) + "입니다.")
print("총 %d번 시도하셨습니다." % trial)
print("=" * 45)
os.system('pause')