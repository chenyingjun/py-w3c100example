'一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？'
import math
len = 100000;
for i in range(0, len):
    num = math.sqrt(i + 100)
    if num.is_integer():
        num = math.sqrt(i + 268)
    if num.is_integer():
        print("这个整数在100000以内的有：", i)



print(math.sqrt(121))
print(math.sqrt(289))
print(math.sqrt(261 + 100))
print(math.sqrt(261 + 268))
print(math.sqrt(1581 + 100))
print(math.sqrt(1581 + 268))
