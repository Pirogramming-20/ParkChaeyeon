#A
num=0
BR31 = [i for i in range(1, 32)]
while True:
    try:
        num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
        if 1 <= num <= 3:
            break
        else:
            print("1, 2, 3 중 하나를 입력하세요.")
    #입력받은 값을 int()를 사용하여 정수로 변환을 시도 but 실패시 ValueError 발생
    except ValueError:
        print("정수를 입력하세요.")


for i in range(num):
    print("playerA:",BR31[i])

numA=num
#B
num=0
while True:
    try:
        num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
        if 1 <= num <= 3:
            break
        else:
            print("1, 2, 3 중 하나를 입력하세요.")
    #입력받은 값을 int()를 사용하여 정수로 변환을 시도 but 실패시 ValueError 발생
    except ValueError:
        print("정수를 입력하세요.")

for i in range(num):
    print("playerB:",BR31[i+numA])
