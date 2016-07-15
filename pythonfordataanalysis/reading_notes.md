# 《利用python进行数据分析》读书笔记
## 第一章　准备工作
### 结构化数据(structed data)
它们可以是一个些表格(csv)，关联变(关系数据)，多维数组。将数据结构化是为了方便建模。

### python与R, SAS, MATLAB, Stata
因为python是通用编程语言，可以只用python实现以数据为核心的应用程序。
> 大多数软件都是有两部分代码组成：少了需要占用大部分cpu时间的代码，和大量不经常执行的“粘合剂”代码。

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

3. 语法糖(synatatic sugar), 一种编程语法，作用时使代码更容易读懂。*做个负责任的人，比别让你的代码像坨屎。*

## 第二章　引言
### 关于数据处理涉及的一般（笼统的）步奏
1. 与外界交互，　读写各种各样格式的文件或数据库；

2. 准备，　数据规范，就是把原始数据变形；

3. 转换，　对数据做一些数学计算，产生新的数据集；

4. 建模和计算，　将数据和统计模型，机器学习算法和其他一下攻击联系起来；

5. 展示，　展示你的分析结果。
