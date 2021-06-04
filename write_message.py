# 写入文件
filename = 'programming.txt'
with open(filename, 'w') as filename_object:
    filename_object.write("I love programming.")
# 调用open()时提供了两个实参,第一个实参也是要打开的文件的名称; 第二个实参('w')告诉Python，我们要以写入模式打开这个文件。
# 打开文件时，可指定读取模 式('r')、写入模式('w')、附加模式('a')或让你能够读取和写入文件的模式('r+')。
# 如果 你省略了模式实参，Python将以默认的只读模式打开文件。
# 如果你要写入的文件不存在，函数open()将自动创建它。
# 然而，以写入('w')模式打开文 件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件。

# 写入多行
with open(filename, 'w') as filename_object:
    filename_object.write("I love programming.\n")
    filename_object.write("I love python.\n")

# 以附加方式写入，不清空之前内容
with open(filename, 'a') as filename_object:
    filename_object.write("附加1：I love programming.\n")
    filename_object.write("附加2：I love python.\n")