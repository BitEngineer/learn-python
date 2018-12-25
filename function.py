# 函数

print('==== 函数定义和调用 ====')
# 定义函数
def say_hello() :
    print('hello')
# 调用函数
say_hello()


print('==== 带参函数 ====')
# 带参数的函数
def print_max(a, b) :
    if a >= b :
        print(a)
    else :
        print(b)
#调用
print_max(1,2)


print('==== 函数返回值 ====')
# 函数的返回值
def get_max(a, b) :
    if a >= b :
        return a
    else :
        return b
# 调用
print(get_max(1 ,2))

