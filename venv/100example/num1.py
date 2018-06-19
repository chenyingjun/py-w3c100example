'有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？'

class num1():
    num = ['1', '2', '3', '4']
    count = 0;
    for index1 in num:
        for index2 in num:
            if index1 == index2:
                continue
            for index3 in num:
                if index1 == index3 or index2 == index3:
                    continue
                count = count + 1
                print(index1, index2, index3)

    print(count)

