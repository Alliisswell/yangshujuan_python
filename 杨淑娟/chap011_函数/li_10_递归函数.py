# 老 师：杨淑娟
# 学 生：李晓宁
# 时 间：2022/5/10 17:27
# 分隔工具：print('*' * 5, '', '*' * 5)
"""
递归函数
1、定义：如果在一个函数的函数体内调用了该函数本身，这个函数就称为递归函数
2、组成部分：递归调用和递归终止条件
3、调用过程：
    每递归调用一次函数，都会在栈内存分配一个栈帧
    每执行完一次函数，都会释放相应的空间
4、优点：思路简单
5、缺点：占用内存大，效率低
"""


def fac(n):
    if n == 1:
        return 1
    else:
        res = n * fac(n - 1)
        return res


print(fac(6))
