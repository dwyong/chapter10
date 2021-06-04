# 读取文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
# 函数open（）打开任何文件，接受一个参数，即文件路径
# open（）打开文件后返回一个对象file_object
# 对象调用read方法将文件以字符串形式存储在变量contents中
# 使用with打开文件不用考虑关闭文件的问题，也可以使用open和close
# 但是需要考虑关闭的问题
# rstrip（）删除字符串末尾空白
# windows下路径注意反斜杠问题
print(type(file_object))

# 逐渐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 用列表储存上述文件每行
with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)
    print(type(lines))
# 注意readline和readlines的区别

# 测试


class AAA():
    def __init__(self, name):
        self.name = name

    def Pprint():
        print("hello a")


aaa = AAA('bbb')
print(type(aaa))
