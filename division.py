# 异常处置 使用 try-except结构处理异常
try:
    print(5 / 0)
except ZeroDivisionError:
    print("除数不能为0")

# 演示两个数的除法
print("给我两个数，我将运行除法运算\n")
while True:
    first_number = float(input("请输入第一个数：\n"))
    if first_number == 'q':
        break
    second_number = float(input("请输入第二个数：\n"))
    answer = first_number / second_number
    except ValueError or ZeroDivisionError:
        print("除数不能为零\n")
    else:
        print(
            str(first_number) +
            "除以" +
            str(second_number) +
            "等于" +
            str(answer) +
            '\n')
