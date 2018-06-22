"""打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153"""

for i in range(100, 1000):
    numStr = str(i)
    num1 = 0
    num2 = 0
    num3 = 0
    num = []
    for j in numStr:
        num.append(j)
    num1 = int(num[0]) ** 3
    num2 = int(num[1]) ** 3
    num3 = int(num[2]) ** 3
    if num1 + num2 + num3 == i:
        print(i)
