# Statistical Probability, Law of large numbers demonstration program
# 통계적 확률 및 큰 수의 법칙 설명 프로그램

import random
import matplotlib.pyplot as plt
import statistics

print('통계적 확률 및 큰 수의 법칙 설명 프로그램')
print('확률과 통계 발표 수업용 자료')
print('제작: 윤수민, 2020년 3월 2일')
print('\n프로그램 설명: 입력된 범위 사이의 정수를 입력된 개수만큼 출력하고, 그 값을 비교합니다.')
print('=================================\n')

GeneratedIntegerList=[]

def RandomIntAdder(Minimum, Maximum):
    GeneratedRandomInteger=random.randint(Minimum, Maximum)
    GeneratedIntegerList.append(GeneratedRandomInteger)

def Repetition(InstanceNumber):
    for i in range(InstanceNumber):
        RandomIntAdder(Minimum, Maximum)

def InstancePrinter(NoMeaningInput):
    for Element in set(GeneratedIntegerList):
        print(str(Element)+'이 나오는 횟수: '+str(GeneratedIntegerList.count(Element)))

while True:
    NoMeaningInput=0
    Minimum=int(input('\n산출되는 수의 최솟값을 입력하십시오. 기본값은 1입니다.\n') or 1)
    Maximum=int(input('\n산출되는 수의 최댓값을 입력하십시오. 기본값은 10입니다.\n') or 10)
    InstanceNumber=int(input('\n시행 횟수를 입력하십시오.\n'))
    Repetition(InstanceNumber)
    print('\n중복을 허용하여 '+str(Minimum)+'부터 '+str(Maximum)+'까지의 임의의 정수를 '+str(InstanceNumber)+'번 추출한 확률분포는:\n')
    InstancePrinter(True)
    print('\n평균: '+str(statistics.mean(GeneratedIntegerList)))
    print('표준편차: '+str(statistics.stdev(GeneratedIntegerList)))
    print('입니다.')
    plt.hist(GeneratedIntegerList, color = 'blue', edgecolor = 'black')
    plt.title('Distribution of '+str(InstanceNumber)+' instances of random number selection, from '+str(Minimum)+' to '+str(Maximum))
    plt.xlabel('Random Number')
    plt.ylabel('Number of Occasions')
    plt.show()
    NoMeaningInput=input('\n계속하려면 Enter를 누르십시오.')
    print('\n프로그램을 재시작합니다.')
    del NoMeaningInput
    GeneratedIntegerList.clear()
    print('=================================\n')

