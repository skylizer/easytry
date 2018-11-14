"""
    作者：Guangpu Yang
    功能：输入日期，判断是这一年的第几天
    版本：3.0
    日期：13/11/2018
    2.0 新增功能： 用列表替换元组
    3.0 新增功能： 将月份用集合划分

"""
from datetime import datetime

def if_leap_year(year):
    """
        判断year是否为闰年
        是 返回 True
        否 返回 False
    """
    is_leap = False

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True

    return is_leap

def main():
    """
        主函数
    """
    date_str = input('请输入日期(yyyy/mm/dd): ')
    date = datetime.strptime(date_str, '%Y/%m/%d')


    year = date.year
    month = date.month
    day = date.day
    # 包含30天的月份集合
    _30_days_month_set = {4, 6, 9, 11}

    # 包含31天的月份集合
    _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}

    days = day

    for i in range(1, month):
        if i in _30_days_month_set:
            days += 30
        elif i in _31_days_month_set:
            days += 31
        else:
            days += 28
    # 判断是否是闰年
    if if_leap_year(year):
        days += 1
    # 第几天


    print(days)

if __name__ == '__main__':
    main()
