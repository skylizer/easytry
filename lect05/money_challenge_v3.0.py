"""
    作者：Guangpu Yang
    功能：52周存钱挑战
    版本：3.0
    日期：12/11/2018
    2.0 新增功能：记录每周的存钱数
    3.0 新增功能：用循环来记录周数

"""
import math

def main():
    """
        主函数

    """
    money_per_week = 10  # 每周存钱的金额
    money_increase = 10  # 每周增加的存钱金额
    total_week = 52      # 存钱的周数
    saving = 0           # 累计存钱的金money_challenge_v1.0.py额
    money_list = []      # 记录每周的存钱数的列表

    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        print('第{}周，存入{}元，账户累计{}元'.format(i + 1, money_per_week, saving))

        # 更新下一周存钱金额
        money_per_week += money_increase
        # 更新存钱的周数a

    print(money_list)


if __name__ == '__main__':
    main()
