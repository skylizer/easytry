"""
    作者： 杨光璞
    功能： 绘制五角星
    版本： 3.0
    日期： 08/11/2018
    2.0 新增功能：加入循环重复不同大小的五角星绘制
    3.0 新增功能：利用递归函数（迭代）重复不同大小的五角星绘制
"""

import turtle

# def draw_pentagram(size):
#     """
#         绘制五角星
#     """
#     count = 1
#     while count <= 5:
#         turtle.fd(size)
#         turtle.right(144)
#         count += 1

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


def main():
    """
        主函数 
    """
    turtle.penup()
    turtle.bk(50)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    size = 50

    draw_recursive_pentagram(size)


    turtle.exitonclick()


if __name__ == '__main__':

    main()
