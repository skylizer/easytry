"""
    作者：Guangpu Yang
    功能：BMR 计算器
    版本：1.0
    日期：09/11/2018

"""

def main():
    """

        主函数
    """
    # 性别
    gender = '男'
    # 体重（kg）
    weight = 70
    # 身高（cm）
    height = 175
    # 年龄
    age = 25

    if gender == '男':

        bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
    elif gender == '女':

        bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655

    else:
        bmr = -1

    if bmr != -1:
        print('基础代谢率（大卡）', bmr)
    else:
        print('暂不支持该性别')

    return


if __name__ == '__main__':

    main()
