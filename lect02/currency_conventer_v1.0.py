"""
    作者：GUANGPU YANG
    功能：汇率兑换
    版本号：1.0
    日期：05/11/2018

"""
usd_vs_rmb = 6.77

rmb_str_value = input('人民币金额是： ')

rmb_value = eval(rmb_str_value)



usd_value = rmb_value / usd_vs_rmb

print('美元金额是： ', usd_value)


