cabinet = {3:"아이린", 100:"제니"}
print(cabinet[3])
print(cabinet[100])

# 대괄호로 진행했을때 .get으로 지정하지 않은 값을 한다면 프로그램 종료

#print(cabinet[5]) 와 print(cabinet.get(5) 는 다르다 )

print(cabinet.get(5))

# none이 아니라 지정값을 출력하고 싶다면 아래처럼 

print(cabinet.get(5, "사용가능"))

# 값이 안에 있으면 참, 없으면 거짓

print(3 in cabinet)
print(5 is cabinet)

# 정수 뿐만 아니라 스트링도 가능 

cabinet = {"A-3": "아이린", "B-100": "제니"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님 
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님 
del cabinet["A-3"]
print(cabinet)
# key 들만 출력 
print(cabinet.keys())

# value 들만 출력 
print(cabinet.values())

# key, value 쌍으로 출력 
print(cabinet.items())

# 예) 목욕탕 폐점 
cabinet.clear()
print(cabinet)


