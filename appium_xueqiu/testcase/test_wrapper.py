#hellohe goodbye都在重复造轮子，函数里的这部分内容是重复的，函数越来越多 相同内容越来越多，把相同的部分抽离的过程就叫装饰器

#把tmp作为参数传进去
def extend(fuc):
    #自己定义一个函数
    #*args,**kwargs 包含了python所有的参数类型，表示接收任意参数，可以把tmp里面的值 都传进来
    def hello(*args,**kwargs):
        print("hello")
        print(args)
        print(kwargs)
        #主动调tmp
        fuc(*args,**kwargs)
        print("good  bye")
    return hello


@extend
def tmp(a,b,c,d):
 print("tmp")


@extend
def tmp1():
    print("tmp1")


def test_wrapper():
    tmp(1,2,3,d=10)
    tmp1()