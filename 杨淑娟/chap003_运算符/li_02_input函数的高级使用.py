# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/3 11:17

# input函数的高级使用
# 从键盘输入两个整数，计算之和并输出
a = input('请输入第一个整数：')
b = input('请输入第二个整数：')
print(type(a), type(b))
# print(a+b)  # 没有进行数据转换
print(int(a) + int(b))

# 也可以在赋值变量的时候就进行数据转换
c = int(input('请输入第一个整数：'))
d = int(input('请输入第二个整数：'))
print(type(a), type(b))
print(c + d)
