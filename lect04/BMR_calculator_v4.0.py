"""
    作者：Guangpu Yang
    功能：BMR 计算器
    版本：4.0
    2.0 新增功能: 根据用户输入计算BMR，程序持续运行
    3.0 新增功能：用户可以在一行输入所有信息，输出带单位的信息
    4.0 新增功能：异常处理
    日期：10/11/2018

"""


def main():
    """

        主函数
    """
    y_or_n = 'n'

    while y_or_n != 'y':
        # # 性别
        # gender = input('性别: ')
        # # 体重（kg）
        # weight = float(input('体重(kg): '))
        # # 身高（cm）
        # height = float(input('身高(cm): '))
        # # 年龄
        # age = int(input('年龄: '))

        print('请输入以下信息，用空格分割')
        input_str = input('性别 体重(kg) 身高(cm) 年龄：')
        str_list = input_str.split(' ')
        # print(str_list)
        try:
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
        except ValueError:
            print('请输入正确的数值！')
        except IndexError:
            print('您输入的参数数量有误！')
        except:
            print('程序异常')

        print()

        y_or_n= input('是否退出程序(y/n)? ')




if __name__ == '__main__':

    main()
