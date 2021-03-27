#수의 출력
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*5)
print(3*(3+1))

#문자열 출력
print('문자열 출력1')
print("문자열 출력2")
print("문자열 출력3"*7) 

#참 / 거짓 (대,소문자 구별)
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)

#예제. 애완동물 소개하기

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >=3

''' 변수 같은 경우 (취미), 만약 32번줄 밑에 hobby를 공놀이라 설정하면 
 그 다음줄 부터 hobby는 산책이 아닌 공놀이로 인식한다. 다른 변수들도 마찬가지. 
str은 정수형 변수에 사용 '+' 가 아닌 콤마(,)형으로 바꾼다면 str을 사용하지 않아도 사용가능. 단) 콤마를 쓸경우 한칸씩 띄워짐 '''

print("우리집 " + animal + "의 이름은 " + name + "이다")
print(name + "는 " + str(age) + "살이며,"+ hobby + "을 아주 좋아한다.")
print(name + "는 어른일까요? " + str(is_adult)) 

#문제) 변수를 이용해 문장을 출력하자
# 변수명 - station, 값 - 사당, 신도림, 인천공항 순서대로 
# 출력문장 - xx행 열차가 들어오고 있습니다. 

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

#station = "신도림"
#station = "인천공항" 으로 바꾸면 동일한 결과값을 출력함. 



