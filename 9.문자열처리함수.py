python = "Python is Amazing"
print(python.lower()) #lower 전부 소문자로
print(python.upper()) #upper 전부 대문자로 
print(python[0].isupper()) #[]번째에 있는 값이 대문자인가 -> 맞으면 True
print(python[0].islower()) #[]번째에 있는 값이 소문자인가 -> 맞으면 true

print(len(python)) #문자열 길이 반환
print(python.replace("Python", "Java")) #문자 변경

index = python.index("n")
print(index)
#인덱스 함수를 사용하여 지정한 문자가 어느 위치에 있는지 보여줌 

index = python.index("n", index + 1 )
# 2번째 n의 위치를 찾음 

print(python.find("n"))
#원하는 값이 없을경우 find는 -1을 출력, 인덱스는 오류가 난다. 즉 인덱스는 프로그램을 종료, find는 계속 진행 

print(python.count("n"))
# 지정한 문자열이 몇번 나왔나 알려주는 함수 





