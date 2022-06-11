# -*- coding: utf-8 -*-
print("부팅중...잠시만 기다려주세요 :>\n프로그램 강제 중지를 원할시 Ctrl+C를 눌러주세요\n----------------------------------------")
import random,time
l = list()
money:int = 0

class cha:
    rare=["고양이 홉핑","고양이 차륜","고양이 에스테","고양이 쥬라","고양이 파이터","고양이 해적","고양이 도둑","고양이 승려","고양이 점쟁이","고양이 샤먼","고양이 마녀","고양이 아처","고양이 마검사","건맨 고양이","죽마 고양이","양철 고양이","고양이 로커","인어 고양이","사이킥 냥코","고양이 음양사","고양이 가위","고양이 복서","고양이 탐사기","고양이 마타도르","고양이 무도가"]
    super_rare=["고양이 댄스","고양이 스시","오덕 고양이","고타츠양이","고양이 사과","고양이 스위머","고양이 욕조","고양이 일진","고양이 보살","창가의 소녀 고양이","고양이 바벨","고양이 스케이트","고양이 토스터","고양이 점퍼","고양이 펜싱","고양이 금도끼은도끼","전대 드릴러","전대 드라이버","전대 커터 고양이","전대 포클레인 고양이","전대 직쏘 고양이"]
    uber_super_rare=['고양이 루가','아시루가','쿠비루가','테코루가','바라라가','가시루가','노비루가','고양이 아이스','고양이 머신','도깨비 야옹마','고양이 슈발리에','고양이 베이비','고양이 간호사','고양이 퀘스트','라스트 보스','바람의 신・윈디','번개의 신・산디아','쿠우','카이','갓파 마인','명계의 칼리파','시시루와 코마리','멜슈','그리폰','백호','하데스','오딘','아수라','사라만다','누아','미네르바','성룡 메기도라','지룡 소돔','용기사 바르스','신룡 카무쿠라','용병기 라이덴','패룡 디오라무스','고룡 강글리온','각룡 그라디오스','복숭아 동자','대나무 공주','석공 냥돌이','냥꼬북','크레인 냥코','너굴냥즈','떠돌이 악사','긴타로','아키라','메카소녀 진','캣맨 대디','화이트 래빗','주술사 데스삐에로','천주 송골매','망자탐정 비그라','매드슈터 사키','천공신 제우스','수호신 아누비스','미의 여신 아프로디테','태양신 아마테라스','번영신 가네샤','해왕신 포세이돈','시공신 크로노스','명계신 하데스','강철육군 카타바르스','고대군함 가레스','비행습격 바머스','관측병기 갈릴레오','온천천국 테르마이','불의 정령 메라라','물의 정령 마리','바람의 정령 에어리','번개의 정령 볼트','돌의 정령 롤링스톤','요수 가오','무녀공주 미타마','쾌걸 달타냥','재앙의 캐슬리','흑수 가오우','칠흑의 미타마','호걸 달타냥','화근의 마녀 캐슬리','묘반권 파이파이','광전기병 레이','사쿠라']
    legend_rare=[]

class prefix:
    first = ["지나가던","깡을 추며 기어가던","멋있는","깜찍한","순수한","잘생긴","멍청한","몬쉥긴","화성에 있는","가나에 있는","한심한","대단한","놀라운","이로운","처음보는","뭔가 똑똑할 거 같이 생긴","짜파게티를 팔고 있는","달고나를 핧고 있는","배그를 하고 있는","인기 많은","실종된","물에 빠진"]
    second = ['날다람쥐','흑우','일론머스크','부자','아싸','인싸','대통령','두더지','길고양이','한국다람쥐','비닐봉지','휴지조각','사람','남자','여자',"화성인","어쩔티비","이찬혁","제작자","관짝아저씨","PC방 사장님","국밥충","잼민이","용팔이","노숙자","경찰관","보험회사직원","사기꾼","익명","짜장면"]

for i in range(0,1000):
    l.append(i/10)
catfood:int = 0

class sale:
    one:bool = True
    two:bool = True


def pick(data:int):
    for j in range(1,data+1):
        r = random.choice(l)
        if r <= 0.3:
            input(f"레전드 레어!!! : {random.choice(cha.legend_rare)}")
        if r > 0.4 and r <= 5.4:
            input(f"울트라 슈퍼 레어!! : {random.choice(cha.uber_super_rare)}")
        if r > 5.4 and r <= 30.4:
            input(f"슈퍼 레어! : {random.choice(cha.super_rare)}")
        if r > 30.4:
            input(f"레어 : {random.choice(cha.rare)}")

def buy_catfood():
    global money,catfood
    while True:
        output = input("1.통조림30개 - 1000원\n2.통조림100개 - 3000원\n3.통조림180개 - 5000원\n4.통조림330개 - 8000원\n5.통조림680개 - 15000원\n6.통조림1080개 - 22000원\n7.통조림1860개 - 37000원\n8.통조림 3900개 - 77000원\n원하시는 상품의 번호를 입력해주세요 :")
        try:
            output=int(output)
        except Exception:
            print("숫자로 입력해주세요")
            time.sleep(1.5)
        if type(output) == int and output > 0 and output < 9:
            if output == 1:
                money -= 1000
                catfood += 30
                print("통조림 30개 충전 완료! (통장에서 1000원이 빠져나갔습니다")
            if output == 2:
                money -= 3000
                catfood += 100
                print("통조림 100개 충전 완료!! (통장에서 3000원이 빠져나갔습니다")
            if output == 3:
                money -= 5000
                catfood += 180
                print("통조림 180개 충전 완료!!! (통장에서 5000원이 빠져나갔습니다")
            if output == 4:
                money -= 8000
                catfood += 330
                print("통조림 330개 충전 완료!!!! (통장에서 8000원이 빠져나갔습니다")
            if output == 5:
                money -= 15000
                catfood += 680
                print("통조림 680개 충전 완료!!!!! (통장에서 15000원이 빠져나갔습니다")
            if output == 6:
                money -= 22000
                catfood += 1080
                print("통조림 1080개 충전 완료!!!!!! (통장에서 22000원이 빠져나갔습니다")
            if output == 7:
                money -= 38600
                catfood += 1860
                print("통조림 1860개 충전 완료!!!!!!! (통장에서 38600원이 빠져나갔습니다")
            if output == 8:
                money -= 77000
                catfood += 3900
                print("통조림 3900개 충전 완료!!!!!!!! (통장에서 77000원이 빠져나갔습니다")
            break
            

def earn_money():
    global money
    earned:int = 0
    total:int = 0
    for i in range(1,random.randint(2,11)):
        earned = random.randrange(1000,5000,1000)
        print(f"{random.choice(prefix.first)} {random.choice(prefix.second)} 님이 {earned}원 후원함!")
        time.sleep(random.random()*4)
        total += earned
    money += total
    print(f"{total}원을 구걸해서 벌었다!\n현재 자산 : {money}원")

def rare():
    while True:
        output = input("1. 1번 뽑기 통조림30개(할인중)\n2. 11번 뽑기 통조림750개(할인중)\n숫자(\'1\',\'2\')로 입력해주세요")
        try:
            output = int(output)
            global catfood
            if output == 1:
                if sale.one == True:
                    if catfood < 30:
                        print("통조림이 부1족해요")
                        return
                    else:
                        catfood -= 30
                        pick(1)
                        sale.one == False
                elif sale.one == False:
                    if catfood < 150:
                        print("통조림이 부1족해요")
                        return
                    else:
                        catfood -= 150
                        pick(1)
                        sale.one == False
            if output == 2:
                if sale.two == True:
                    if catfood < 750:
                        print("통조림이 부1족해요")
                        return
                    else:
                        catfood -= 750
                        pick(11)
                        sale.two == False
                elif sale.one == False:
                    if catfood < 1500:
                        print("통조림이 부1족해요")
                        return
                    else:
                        catfood -= 1500
                        pick(11)
                        sale.two == False
        except Exception:
            print("올바른 형태로 입력해주세요")
            pass

input("냥코 뽑기 시뮬레이터 일명  \'냥.뽑.시\' 에 오신 걸 환영합니다 (진행하려면 Enter를 치세요): ")
while True:
    output = input("현재 보유하고 계신 통조림이 없으신거 같아요\n\'구걸\'이라고 입력해보세요 :")
    if output == "구걸":
        break
earn_money()
input("축하해요^^ :")
input("이제 현질을 해서 통조림을 사볼거에요")
while True:
    output = input("\'구매\'라고 입력해보세요 :")
    if output == "구매":
        break
buy_catfood()
input("잘했어요!")
input(f"통조림 {catfood}개로 뽑기를 돌려볼게요")
while True:
    output = input("\'뽑기\'라고 입력해보세요 :")
    if output == "뽑기":
        rare()
        break