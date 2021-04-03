
def ZSQ(func):
    print("函数开始")
    def fun(func):
        func()
    print("函数结束")
    return fun

@ZSQ
def func():
    print("这是func内部")

s = "123"
s1 = str("123")
list()
type()
def func1():
    print("这是func1内部")


def func2():
    print("这是func2内部")





func()