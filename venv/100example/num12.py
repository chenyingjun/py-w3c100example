"""判断101-200之间有多少个素数，并输出所有素数。"""
num = 0
for i in range(101, 201):
    bool = True
    for j in range(2, 101):
        if i % j == 0:
            bool = False
            break
    if bool == True:
        num += 1
        print(i)
print("个数：", str(num))