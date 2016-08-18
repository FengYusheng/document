.y# 《利用python进行数据分析》读书笔记
## 第一章　准备工作
### 结构化数据(structed data)
它们可以是一个些表格(csv)，关联表(关系数据)，多维数组。将数据结构化是为了方便建模。

### python与R, SAS, MATLAB, Stata
因为python是通用编程语言，可以只用python实现以数据为核心的应用程序。
> 大多数软件都是有两部分代码组成：少量需要占用大部分cpu时间的代码，和大量不经常执行的“粘合剂”代码。

### python不合适的地方
python不适合高并发多线程的应用程序，因为 *GIL（全局解释器锁）* 的存在。

### python里用于科学计算的库
1. Numpy 用于作为数据的容器，在算法间传递数据。实现了多维数据。

2. pandas 处理结构化数据。

3. matplotlib 制作图表。

4. IPython 科学计算的交互环境。

5. SciPy 用于数学计算，与Numpy配合，可以替代MATLAB。

#### 科学计算开发环境
1. Enthought；
2. Python(x,y) 目前只有windows版本。

#### 会用到的其他的库
statsmodels PyTables PyQt xlrd lxml basemap pymongo requests

>Python Package Index(PyPI) 里能找到各个python库的帮助信息。

### 引入惯例
`import NumPy as np`

`import pandas as pd`

`import matplotlib.pylot as plt`

> [`import` vs `from...import...`][]

  [`import` vs `from...import...`]: http://stackoverflow.com/questions/9439480/from-import-vs-import

### 行话，让你像个老司机
1. 数据规整(munge/munging/wrangling)，将非结构化的或散乱的数据处理为结构化的或整洁的数据的过程；

2. 伪码(pseudocode)

3. 语法糖(synatatic sugar), 一种编程语法，作用是使代码更容易读懂。*做个负责任的人，比别让你的代码像坨屎。*

## 第二章　引言
### 关于数据处理涉及的一般（笼统的）步奏
1. 与外界交互，　读写各种各样格式的文件或数据库；

2. 准备，　数据规范，就是把原始数据变形；

3. 转换，　对数据做一些数学计算，产生新的数据集；

4. 建模和计算，　将数据和统计模型，机器学习算法和其他一下攻击联系起来；

5. 展示，　展示你的分析结果。

### 列表推导式
能用列表推导式时就不要用map/filter。

字符串是 [immutable][]，列表是 [mutable][]。

[immutable]:https://docs.python.org/2/glossary.html#term-immutable

[mutable]:https://docs.python.org/2/glossary.html#term-mutable

### colletions
这个库实现了一些容器类型，可以用来替代内置的容器类型，比如dict, list, set , tuple

### sorted() vs list.sort()
sorted(list)返回一个新list, list.sort()改变原来list的元素顺序，不产生新list。它们都是从小到打顺序排序。

>这个sort是稳定的。

详细信息：[Sorting How To][]

[Sorting How To]: https://docs.python.org/2/howto/sorting.html#sortinghowto

### colletions.counter
>这倒是意外收获，[c++ tutorial](http://www.java2s.com/Tutorial/Cpp/0380__set-multiset/Catalog0380__set-multiset.htm)

### 为何在脚本里没有显示图表？
在ipython命令行运行代码时，显示图片所需的库已经在ipython --pylab模式启动时自动加载了。如果想在调用脚本时显示出图表，必须手动添加所需的库。[No plot window shows up with matplotlib.pyplot run with Enthought Canopy python editor][]

[No plot window shows up with matplotlib.pyplot run with Enthought Canopy python editor]:http://stackoverflow.com/questions/21129055/no-plot-window-shows-up-with-matplotlib-pyplot-run-with-enthought-canopy-python

### 本章总结
本章是通过几个例子向读者介绍这些攻击帮助你做什么，后续章节会详细介绍这些工具。

## 第三章　IPYTHON：一种交互式计算和开发环境
###　ipython基础
IPYTHON设计的目的是最大化python的 **交互** 式计算，它鼓励一种“执行－探索（试误法，迭代法）”的工作模式。ipython 就是一个画了淡妆的python解释器。

> 锻炼对常用命令的肌肉记忆是学习曲线中不可或缺的部分

### 执行剪贴板里的代码
`%paste`和`%cpast（显示粘贴的代码）`会执行剪贴板里　**一切** 文本。

> ipython notebook更常用。


### 快捷键

### 魔术命令
一些命令以`%`开头，叫做魔术命令，它们用来方便你操作ipython。
魔术命令默认是允许不带`%`运行的，只要你没有定义与命令相同名字的变量。

> 这家伙也在学python数据分析： http://www.cnblogs.com/zzhzhao/

### 基于QT的富GUI控制台
为ipython添加绘图功能：　`ipython qtconsole pylab=inline`

### 输入与输出
* `_iX`: 显示第X行输入
* `_X` : 显示第Ｘ行输出
* `_`, `__` : 显示最近一次输出和最近两次输出

### 记入输入和输出
`%logstart`开启记录功能，记录你在当前会话的整个工作过程。

### 调试
在ipython中用pdb调试某段脚本：
`run -d -b行号 command.py`

### 性能测试工具
*Wall time: the time on the clock on your wall.*

**这小结回头在要再看一次**

### ipython notebook
现在启动notebook要用`jupyter notebook`

### 利用ipython提供代码开发效率的几点提示
* 加载最新的模块:
      import some_lib
      reload(some_lib)
 或者干脆重启ipython。

* 扁平结构要比嵌套结构要好。

### 让ipython更友好

`__repr__`的作用是返回一个克打印的字符串，这个字符串代表了一个对象。

> *“把这个字符串传给`eval()`，可以重新获取这个对象。”* 网络上的这个言论不准确，不是任何对象都可以这么获取。
https://bytes.com/topic/python/answers/535436-eval-repr-object-hardly-ever-works

## 第４章　NumPy基础：数组和矢量计算
### NumPy 是本书介绍的科学计算工具的基础，它提供了一下功能：

* ndarry，一个具有矢量算术运算和复杂广播能力的快速且节省空间的多维数组；

* 用于对数组进行快速运算的数学函数；

* 用于读写磁盘数据的工具和操作内存映射文件的工具；

* 线性代数，随机数生成以及傅里叶变换功能；

* 用于集成有c, c++, fortran等编写的代码的工具。

对于大部分数据分析应用而言，我们最关注的功能主要集中在：

* 用于数据整理和清理，子集构造和过滤，转换等快速的矢量化数组运算；

* 常用的数组算法，如排序，唯一化，集合运算等；

* 高效的描述统计和数据聚合／摘要运算；

* 用于异构数据集的合并/连接运算的数据对齐和关系型数据运算；

* 将条件逻辑表述为数组表达式（而不是带有if-elif-else分支的循环）；

* 数组的分组运算（聚合，转换，函数应用等）。

### NumPy的ndarray：一种多维数组对象
NumPy最重要的特点就是它提供了一种多维数组对象,ndarray。

ndarray是一个同构数据多维容器。精通面向数组的编程和思维方式是成为python科学计算牛人的一大关键步骤。

### ndarray的数据类型
dtype是让NumPy如此强大灵活的原因之一。

dtype的类型：
![dtype1][]
![dtype2][]

[dtype1]:./dtype1.png
[dtype2]:./dtype2.png

### 数组和标量之间的运算
数组很重要，它可以让你不用编写循环即可对数据进行批量运算，这通常叫做 **矢量化**。大小相等的数组之间的任何算术运算都会应用到元素级，数组与标量的算术运算会将那个标量值传播到各个元素。不同大小的数组之间的运算叫　**广播**。
