"""
    作者：Guangpu Yang
    功能：输入日期，判断是这一年的第几天
    版本：2.0
    日期：13/11/2018
    2.0 新增功能： 用列表替换元组

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

    # 每月的天数
    days_in_year_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 判断是否是闰年
    if if_leap_year(year):
        days_in_year_list[1] = 29
    # 第几天
    days = sum(days_in_year_list[:month-1]) + day


    print(days)

if __name__ == '__main__':
    main()
