'输入三个整数x,y,z，请把这三个数由小到大输出。'

num1 = input("请输入第一个数")
try:
    num1 = int(num1)
except  ValueError:
    print('请输入纯数字')
    exit()
num2 = input("请输入第二个数")

try:
    num2 = int(num2)
except  ValueError:
    print('请输入纯数字')
    exit()

num3 = input("请输入第三个数")
try:
    num3 = int(num3)
except  ValueError:
    print('请输入纯数字')
    exit()

aList = [num1, num2, num3]
aList.sort()
print(aList)
