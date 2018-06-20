'斐波那契数列    0、1、1、2、3、5、8、13、21、34...'

def fib(n):
    try:
        n = int(n)
    except:
        print("请输入整数")
        exit()

    if n < 1:
        print("请输入大于一的数")
        exit()

    index0 = 0
    index1 = 1
    indexList = [index0, index1]
    i = 2
    while(i < n):
        index = indexList[i-2] + indexList[i-1]
        i = i + 1
        indexList.append(index)

    print("斐波那契数列：", indexList)

fib(input("请输入需生成的斐波那契数列个数"))