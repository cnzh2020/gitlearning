# print absolute value of an integer
a=int(input('输入你的数值'))
'''
input函数输入保存值类型是str, >= 只能识别int值. 直接input将导致报错
此时,需要使用 int()强制将input中的值转化为整数值,转化完成后才能执行比较
'''
if a >= 0:
    print(a)
else:
    print(-a)
