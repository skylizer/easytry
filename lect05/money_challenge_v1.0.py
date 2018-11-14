"""
    作者：Guangpu Yang
    功能：52周存钱挑战
    版本：1.0
    日期：11/11/2018

"""
def main():
    """
        主函数

    """
    money_per_week = 10  # 每周存钱的金额
    i = 1                # 记录存钱的周数
    money_increase = 10  # 每周增加的存钱金额
    total_week = 52      # 存钱的周数
    saving = 0           # 累计存钱的金money_challenge_v1.0.py额

    while i <= total_week:
        # saving += money_per_week + money_increase * (i - 1)
        # 存钱操作
        saving += money_per_week
        # 输出信息
        print('第{}周，存入{}元，账户累计{}元'.format(i, money_per_week, saving))
        # 更新下一周存钱金额
        money_per_week += money_increase
        # 更新存钱的周数a
        i += 1

    print(saving)


if __name__ == '__main__':
    main()
