import random
w=0
c=0
l=0
choices=["가위","바위","보"]
while True:
    print("가위, 바위, 보 중 하나를 고르세요: ")
    user=input()
    computer=random.choice(choices)
    if user in choices:
        print(f"사용자: {user}, 컴퓨터: {computer}")
        if computer==user:
            print("비겼습니다")
            c+=1
        elif (computer=="가위" and user=="바위") or (computer=="바위" and user=="보") or (computer=="보" and user=="가위"):
            print("사용자 승리!")
            w+=1
        elif (computer=="가위" and user=="보") or (computer=="바위" and user=="가위") or (computer=="보" and user=="바위"):
            print("컴퓨터 승리!")
            l+=1
        print("다시 하시겠습니까? (y/n): ")
        answer=input().lower()
        if answer=="y" or answer=="네": continue
        else:
            print(f"승:{w} 패:{l} 무승부:{c}")
            break
    else:
        print("유효한 입력이 아닙니다")
