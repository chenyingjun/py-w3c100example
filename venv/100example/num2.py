'企业发放的奖金根据利润提成。\
利润(I)低于或等于10万元时，奖金可提10%；\
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；\
20万到40万之间时，高于20万元的部分，可提成5%；\
40万到60万之间时，高于40万元的部分，可提成3%；\
60万到100万之间时，高于60万元的部分，可提成1.5%，\
高于100万元时，超过100万元的部分按1%提成，\
从键盘输入当月利润I，求应发放奖金总数？'
class num2:
    ''
def get_commission(profit):
    commission = 0;
    unit = 10000;

    if profit > 100 * unit:
        m = profit - 100 * unit;
        commission = commission + m * 0.01;
        profit = profit - m;
        print('超100万奖金：', m * 0.01)
    if profit > 60 * unit:
        m = profit - 60 * unit;
        commission = commission + m * 0.015;
        profit = profit - m;
        print('超60万奖金：', m * 0.015)
    if profit > 40 * unit:
        m = profit - 40 * unit;
        commission = commission + m * 0.03;
        profit = profit - m;
        print('超40万奖金：', m * 0.03)
    if profit > 20 * unit:
        m = profit - 20 * unit;
        commission = commission + m * 0.05;
        profit = profit - m;
        print('超20万奖金：', m * 0.05)
    if profit > 10 * unit:
        m = profit - 10 * unit;
        commission = commission + m * 0.075;
        profit = profit - m;
        print('超10万奖金：', m * 0.075)
    if profit <= 10 * unit:
        commission = commission + profit * 0.1;
        print('低于10万奖金：', profit * 0.1)
    print('发放奖金总数：', commission)

profit = input("请输入：")
try:
    profit = int(profit)
    if profit <= 0:
        print("请输入大于0的数")
    else:
        get_commission(profit)
except  ValueError:
    print('请输入纯数字')



'下面是w3c做法'
i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print((i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)