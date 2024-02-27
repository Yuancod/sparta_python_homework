import random
def num_game():
    ran_num=random.randint(1,101)
    i=0
    print ('1에서 100사이의 숫자를 맞추세요:')
    num=None
    while num!=ran_num:
        num = int(input(''))
        if num>ran_num and num<101:
            print('다운')
            i+=1
        elif num<ran_num and num>0:
            print('업')
            i+=1
        else:
            print('유효한 숫자를 입력하세요')
    if num==ran_num:
        i+=1
        print('정답입니다')
        print(f'시도한 횟수:{i}')
        print('다시 하시겠습니까? (y/n)')
        if input().lower()=='y':
            print(f'이전 게임 플레이어 시도 횟수:{i}')
            return num_game()
        else:print('게임을 종료합니다')
num_game()