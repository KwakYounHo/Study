rubin = 1
print(rubin)
rubin = "abc"
print(rubin)

kdt = {
  "삼백오호" : "홀쭉",
  "곽윤호" : "학생"
}

print(kdt["삼백오호"])

kdt_order = ["우리는", "개발자", "입니다"]
print(kdt_order[0], kdt_order[1],kdt_order[2])

for index in kdt_order :
  print(index)

# def = 정의하다
def percent_calc(real_value, total_value):
  result = (real_value / total_value) * 100
  return result

# python - JS보다 숫자에 강하다 (숫자 타입을 다양하게 지원하니)