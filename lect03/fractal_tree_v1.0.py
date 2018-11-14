"""
    作者： 杨光璞
    功能： 分形树绘制
    版本： 1.0
    日期： 08/11/2018
    功能：利用递归函数完成分形树绘制
"""

import turtle

def draw_branch(branch_length):

    if branch_length <= 20:
        turtle.pensize(1)
        turtle.pencolor('green')
    else:
        turtle.pensize(2)
        turtle.pencolor('brown')

    if branch_length >= 5:

        turtle.speed(1)

        # 绘制右侧树枝
        turtle.fd(branch_length)
        print('向前', branch_length)
        turtle.right(20)
        print('右转20度')
        draw_branch(branch_length - 15)


        # 绘制左侧树枝
        turtle.left(40)
        print('左转40度')
        draw_branch(branch_length - 15)
        if branch_length <= 20:
            turtle.pensize(1)
            turtle.pencolor('green')
        else:
            turtle.pensize(2)
            turtle.pencolor('brown')

        # 返回之前的树枝节点
        turtle.right(20)
        print('右转20度')
        turtle.bk(branch_length)
        print('后退', branch_length)






def main():
    """
        主函数 
    """
    turtle.left(90)
    turtle.penup()
    turtle.bk(150)
    turtle.pendown()

    branch_length = 100
    draw_branch(branch_length)

    turtle.exitonclick()


if __name__ == '__main__':

    main()
