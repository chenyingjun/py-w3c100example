'输入某年某月某日，判断这一天是这一年的第几天？'

import time

inputTime = input("请输入时间，格式%Y%m%d：")

try:
    date = time.strptime(inputTime, "%Y%m%d")
    print('这一天是这一年的第%d天' % date.tm_yday)
except:
    print("时间格式有误")

