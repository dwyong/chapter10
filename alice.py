# 处理文件不在的异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("文件" + filename+ "不存在")

words = contents.split()
print(len(words))
for word in words:
    print(word)
# 统计文件中单词