# 100에서 1까지 출력하되, 숫자에 '3'이 포함되어 있으면 '3'의 개수만큼 "짝" 출력
for i in range(100, 0, -1):
    s = str(i)
    cnt = s.count('3')  # 문자열에서 '3'이 몇 번 나오는지 센다
    if cnt > 0:
        print("짝" * cnt)
    else:
        print(i)