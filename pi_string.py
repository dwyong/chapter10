# 读取文件内容并处理使用
filename = "pi_digits.txt"
filename_million = "pi_million_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
pi_string = ''
# 处理pi 小数点后百万位
with open(filename_million) as file_object:
    lines = file_object.readlines()

for line in lines:
    pi_string += line.strip()
print(len(pi_string))
print(pi_string[0:1000002])

# 查看生日是否在pi里
birthday = ''
while birthday != 'q':
    birthday = input("Please input yout birthday")
    if birthday in pi_string:
        print("Your birthday in Pi\n")
    else:
        print("Your birthday not in Pi\n")
