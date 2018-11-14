"""
    作者： 杨光璞
    功能： 绘制五角星
    版本： 2.0
    日期： 07/11/2018
    新增功能：重复不同大小的五角星绘制
"""

import turtle

def draw_pentagram(size):
    """
        绘制五角星
    """
    count = 1
    while count <= 5:
        turtle.fd(size)
        turtle.right(144)
        count += 1

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
    while size <= 150:

        # 绘制五角星
        # 计数器
        draw_pentagram(size)

        size += 50
    else:
        print('结束绘制')

    turtle.exitonclick()


if __name__ == '__main__':

    main()
