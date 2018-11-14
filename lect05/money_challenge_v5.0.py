"""
    作者：Guangpu Yang
    功能：52周存钱挑战
    版本：5.0
    日期：13/11/2018
    2.0 新增功能：记录每周的存钱数
    3.0 新增功能：用循环来记录周数
    4.0 新增功能：用户可以设置存钱金额，周数，增加金额； 函数封装
    5.0 新增功能：根据用户输入的日期，判断存钱的周数，然后输出相应的存款金额

"""
import math
import datetime

# 全局变量
saving = 0               # 累计存钱的金额

def save_money_n_week(money_per_week, money_increase, total_week):

    global saving        # 全局变量
    saving_list = []     # 记录每周的账户累计

    money_list = []      # 记录每周的存钱数的列表

    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saving_list.append(saving)

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(i + 1, money_per_week, saving))

        # 更新下一周存钱金额
        money_per_week += money_increase
        # 更新存钱的周数a

    # print('函数内的saving', saving)
    return  saving_list



def main():
    """
        主函数

    """
    money_per_week = float(input('请输入每周存入的金额: '))
    money_increase = float(input('请输入每周递增的金额: '))
    total_week = int(input('请输入存钱的周数: '))

    saving_list = save_money_n_week(money_per_week, money_increase, total_week)

    # print('函数外的saving', saving)

    date_str = input('请输入日期(yyyy/mm/dd)：')
    date = datetime.datetime.strptime(date_str, '%Y/%m/%d')
    week_num = date.isocalendar()[1]



    print('第{}周的存款金额是{}'.format(week_num, saving_list[week_num - 1]))





if __name__ == '__main__':
    main()
