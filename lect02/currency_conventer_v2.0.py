"""
    作者：GUANGPU YANG
    功能：汇率兑换
    版本号：2.0
    日期：05/11/2018
    新增功能：判断输入的货币为人民币或者是美元
"""
# 美元兑人民币汇率
USD_VS_RMB = 6.77
# 输入带单位的货币金额
currency_str_value = input('请输入带单位的货币金额： ')
# 货币单位
unit = currency_str_value[-3:]
# 判断输入的货币单位
if unit == 'CNY':
    # 人民币的金额（字符串）
    rmb_str_value = currency_str_value[:-3]
    # 将字符串转换为数值
    rmb_value = eval(rmb_str_value)
    # 人民币换算成美元
    usd_value = rmb_value / USD_VS_RMB
    # 输出美元金额
    print('美元（USD）金额是： ', usd_value)

elif unit == 'USD':
    # 美元的金额（字符串）
    usd_str_value = currency_str_value[:-3]
    # 美元的金额（数值）
    usd_value = eval(usd_str_value)
    # 美元换算成人民币
    rmb_value = usd_value * USD_VS_RMB
    # 输出人民币金额
    print('人民币金额是： ', rmb_value)
else:
    print('当前版本尚不支持该货币！')



