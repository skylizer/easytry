"""
    作者：GUANGPU YANG
    功能：汇率兑换
    版本号：3.0
    日期：05/11/2018
    2.0 新增功能：判断输入的货币为人民币或者是美元
    3.0 新增功能: 程序可以一直运行，直到用户选择退出
    4.0 新增功能：将汇率兑换功能封装到函数
"""

def convert_currency(im, er):
    """
        汇率兑换函数

    """
    out = im * er
    return out
# 美元兑人民币汇率
USD_VS_RMB = 6.77

# 输入带单位的货币金额
currency_str_value = input('请输入带单位的货币金额： ')

# 货币单位
unit = currency_str_value[-3:]
# 判断输入的货币单位
if unit == 'CNY':
    exchange_rate = 1 / USD_VS_RMB

elif unit == 'USD':
    exchange_rate = USD_VS_RMB

else:
    exchange_rate = -1

if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])
    # 调用函数
    out_money = convert_currency(in_money, exchange_rate)

    print('换算之后的货币金额： ', out_money)

else:
    print('当前版本尚不支持该货币！')


