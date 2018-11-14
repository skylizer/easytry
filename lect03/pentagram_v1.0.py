"""
    作者： 杨光璞
    功能： 绘制五角星
    版本： 1.0
    日期： 07/11/2018
"""

import turtle

def main():
    """
        主函数 
    """

    count = 1
    while count <= 5:


        turtle.fd(150)
        turtle.right(144)
        count = count + 1



    turtle.exitonclick()


if __name__ == '__main__':

    main()
