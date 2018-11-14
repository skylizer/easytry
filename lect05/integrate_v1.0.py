"""
    作者：Guangpu Yang
    功能：让用户选择要实现的功能: 1: 存钱挑战 2：汇率兑换 3：绘制五角星 4：BMR 计算器
    版本：1.0
    日期：13/11/2018

"""
import math
import datetime
import turtle


############################################################################
#######################    存钱挑战   #######################################
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
        # print('第{}周，存入{}元，账户累计{}元'.format(i + 1, money_per_week, saving))

        # 更新下一周存钱金额
        money_per_week += money_increase
        # 更新存钱的周数a

    # print('函数内的saving', saving)
    return  saving_list



def main1():
    """
        主函数

    """
    # global y_or_n
    # while y_or_n == 'n':
    money_per_week = float(input('请输入每周存入的金额: '))
    money_increase = float(input('请输入每周递增的金额: '))
    total_week = int(input('请输入存钱的周数: '))

    saving_list = save_money_n_week(money_per_week, money_increase, total_week)

    # print('函数外的saving', saving)

    date_str = input('请输入日期(yyyy/mm/dd)：')
    date = datetime.datetime.strptime(date_str, '%Y/%m/%d')
    week_num = date.isocalendar()[1]



    print('第{}周的存款金额是{}'.format(week_num, saving_list[week_num - 1]))

        # y_or_n= input('是否退出程序(y/n)? ')

##############################################################################################
################################   汇率兑换  ##################################################
def main2():

    # global y_or_n

    # while y_or_n == 'n':

    # 美元兑人民币汇率
    USD_VS_RMB = 6.77

    # 输入带单位的货币金额
    currency_str_value = input('请输入带单位的货币金额： ')

    # 货币单位
    unit = currency_str_value[-3:]
    # 判断输入的货币单位
    if unit == 'CNY':
        exchange_rate = 1 / USD_VS_RMB
        out_unit = 'USD'

    elif unit == 'USD':
        exchange_rate = USD_VS_RMB
        out_unit = 'CNY'

    else:
        exchange_rate = -1

    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])
        convert_currency2 = lambda x: x * exchange_rate

        # 调用函数
        # out_money = convert_currency(in_money, exchange_rate)
        out_money = round(convert_currency2(in_money),2)

        print('换算之后的货币金额是{}{} '.format(out_money, out_unit))

    else:
        print('当前版本尚不支持该货币！')

        # y_or_n= input('是否退出程序(y/n)? ')




##############################################################################################
###################################   绘制五角星   ############################################
def draw_recursive_pentagram(size):
    """
        迭代绘制五角星

    """
    count = 1
    while count <= 5:
        turtle.fd(size)
        turtle.right(144)
        count += 1
    # 绘制完五角星， 更新参数
    size += 50
    if size <=150:
        draw_recursive_pentagram(size)


def main3():
    """
        主函数
    """
    # global y_or_n

    # while y_or_n == 'n':
    turtle.penup()
    turtle.bk(50)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50

    draw_recursive_pentagram(size)


    turtle.exitonclick()

        # y_or_n= input('是否退出程序(y/n)? ')
##############################################################################################
###################################   BMR 计算器    ###########################################
def bmr_calculator(str_list):

    gender = str_list[0]
    weight = float(str_list[1])
    height = float(str_list[2])
    age =  int(str_list[3])

    if gender == '男':

        bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
    elif gender == '女':

        bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655

    else:
        bmr = -1

    if bmr != -1:
        print('性别：{}， 体重：{}公斤，身高：{}厘米， 年龄：{}岁'.format(gender, weight, height, age))
        print('基础代谢率: {}大卡'.format(bmr))
    else:
        print('暂不支持该性别')


def main4():
    """

        主函数
    """
    # y_or_n = 'n'

    # while y_or_n != 'y':
    print('请输入以下信息，用空格分割')
    input_str = input('性别 体重(kg) 身高(cm) 年龄：')
    str_list = input_str.split(' ')

    try:
        bmr_calculator(str_list)
    except ValueError:
        print('请输入正确的数值！')
    except IndexError:
        print('您输入的参数数量有误！')
    except:
        print('程序异常')

    print()

        # y_or_n= input('是否退出程序(y/n)? ')

##############################################################################################
print('可选功能 1: 存钱挑战 2：汇率兑换 3：绘制五角星 4：BMR 计算器')
y_or_n = 'n'
while y_or_n == 'n':
    function_num = input('请输入要实现的功能: ')
    if function_num == '1':
        main1()

    elif function_num == '2':
        main2()

    elif function_num == '3':
        main3()

    elif function_num == '4':
        main4()

    else:
        print('当前程序尚不支持该功能！')

    y_or_n = input('是否退出程序(y/n)? ')
