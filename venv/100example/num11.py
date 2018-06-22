'古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？'


num1 = 1;
num2 = 1;
num3 = 0;
for i in range(1, 21):
    if (i == 1):
        print(num1)
        continue
    if (i == 2):
        print(num2)
        continue
    num3 = num1 + num2;
    print(num3)
    num1 = num2
    num2 = num3


f1 = 1
f2 = 1
for i in range(1,21):
    print('%12d %12d' % (f1,f2))
    if (i % 2) == 0:
        print (' ')
    f1 = f1 + f2
    f2 = f1 + f2