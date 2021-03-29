# 리스트 []

# 지하철 칸별로 10명, 20명, 30명 

subway = [10,20,30]
print(subway)

subway = ["사람1", "사람2", "사람3"]
print(subway)

# 사람3이 몇 번째 칸에 타고있는가? 
print(subway.index("사람3"))

#사람4가 다음 정류장에서 다음칸에 탐 

subway.append("사람4")
print(subway)

#사람 5를 사람1 / 사람2 사이에 넣어봄 

subway.insert(1, "사람5")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤애서 꺼냄 

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)


#같은 이름의 사람이 몇 명 있는지 확인 
subway.append("사람1")
print(subway)
print(subway.count("사람1"))

# 정렬도 가능 
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 모두 지우기 
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 
num_list = [5,2,4,3,1]
mix_list = ["사람2", 20 , True]



