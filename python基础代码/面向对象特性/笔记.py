'''
1. 使用面向对象开发，第一步是设计类
2. 使用类名（）创建对象，创建对象 的动作有两步：
      1）在内存中分配空间
      2）使用初始化方法__init__()为对象初始化
3.对象创建之后，内存中就有一个实实在在的存在---实例
4.因此，经常会把：
            1）创建出来对象叫做类的 实例
            2）创建出来的 动作叫做 实例化
            3）对象的 属性 叫做 实例属性
            4）对象调用的方法叫做 实例方法
结论：1）每个对象都有自己独立的内存空间，保存各自不同的属性
      2）个对象的方法，在内存中只有一份，在调用方法时，需要把对象
         的引用传递到发放内部
'''

'''-------------------------------------------------------------'''

'''
__new__方法负责给对象分配空间；
__init__方法负责给对象初始化；
'''