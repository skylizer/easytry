"""
    作者：Guangpu Yang
    功能：输入日期，判断是这一年的第几天
    版本：1.0
    日期：13/11/2018

"""
from datetime import datetime

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
    days_in_year_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # 非闰年的时候第几天
    days = sum(days_in_year_tup[:month-1]) + day

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        if month > 2:
            days += 1

    print(days)

if __name__ == '__main__':
    main()
