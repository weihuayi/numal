# 《数值代数课程简介》

<!---这里简单介绍课程的相关的资源和工具--->

## 教师助教信息 

* **任课教师:** 魏华祎
* **电话:** 15973229281
* **办公室:** 数学院南楼 227
* **邮箱：** weihuayi@xtu.edu.cn


## 课程内容简介

科学计算中的很多模型问题，最后都能化成代数计算问题，因此有必要专门研究代数问题
在计算机上的高效求解算法。

该课程主要讲解以下四类问题的求解方法及相关数学理论：

1. 线性方程组问题
1. 最小二乘问题
1. 特征值问题
1. 奇异值问题

其中的求解方法又可分为两类：

* 直接法
* 迭代法

算法只有转化为实际的程序或软件才能发挥作用。要学好用好一个算法，深入理解算法的数
学原理和动手实现并应用是相辅相成的两个过程。 因此本课程还会加入一些编程基础的内容。课
程当中也会穿插介绍以下内容： 

1. Python 基础
1. Numpy 基础
1. Scipy 基础


## 课程学习资源与工具

### 参考教材 

1. James W. Demmel. Applied Numerical Linear Algebra, SIAM, 1997.
1. R. Barrett and M. Berry and T. F. Chan and J. Demmel and J. Donato and J.
   Dongarra and V. Eijkhout and R. Pozo and C. Romine and H. Van der Vorst,
   Templates for the Solution of Linear Systems: Building Blocks for Iterative
   Methods, SIAM, 1994.

### [Python](www.python.org)

Python 语言的特点：

* 支持面向对象编程的解释性语言，无需编译，易学易用。
* 代码可读性非常强
* 有庞大的用户社群，包括 NASA, ANL, Google 等国际知名的科研机构和公司都选择 Python 做为高性能计算的开发语言。Python 的初学者和开发者很容易从社群中获得帮助和开发文档。
* 有丰富的科学计算基础软件包， 如：
    + NumPy:  http://numpy.scipy.org - Numerical Python，主要提供多维数组及相关运算功能。
    + SciPy:  http://www.scipy.org - Scientific Python，提供高效的优化、FFT、稀疏矩阵等科学计算模块。
    + Matplotlib: http://www.matplotlib.org - Graphics library，提供成熟 2D 和 3D 画图软件功能。
    + SymPy： http://www.sympy.org - 数学符号计算。
* 开源免费

### Markdown 语言

Markdown 是一种轻量级的文本标记语言，可以让你使用易读易写的纯文本格式编写美观的文档。

在本课程中我将会简要介绍 Markdown 语言的基本用法，便于学生和老师之间更方便的交流。

* [作业部落](https://www.zybuluo.com/mdeditor)
* [Markdown 的基本语法](https://github.com/younghz/Markdown)

## [Perusall](http://www.perusall.com/)

Perusall 是一个网络教学平台，具有以下功能和特点

* 教师可以在上面创建课程，并招收学生。
* 教师可以在 Perusall 布置阅读作业。
* 教师和学生都可以在阅读材料旁做笔记，其他人可以看到并回复。
* 批注支持前面介绍的 Markdown 语言，可以很好的支持数学公式的输入
* 学生完成作业后，网站可以自动根据学生的活跃情况进行自动打分，并向教师反馈学生的阅读情况。


### [Dataquest](www.dataquest.io)

Dataquest 是一个大数据的自主学习网站，里面有免费学习 Python 的基础课程，课程语言
为英语。它的课程设计非常适合自学，Dataquest 把每门课程分解为很多由浅入深的小知识
点，每个知识点后面都有配套编程练习。注意它的编程练习，不需要学生自己搭建本地编程
环境，而是直接在网页的代码框写代码即可。写完代码后，可直接运行，网站自动判断程序
是否正确。学生只有完成了每个知识点的练习，才能进行下一步的学习。


<div id="container"></div>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/theme-next/theme-next-gitment@1/default.css"/>
<script src="https://cdn.jsdelivr.net/gh/theme-next/theme-next-gitment@1/gitment.browser.js"></script>

<script>
var gitment = new Gitment({
  id: 'window.location.pathname', 
  owner: 'weihuayi',
  repo: 'weihuayi.github.io',
  oauth: {
    client_id: '7dd9c9fc3ac45352b55b',
    client_secret: '4e6f74b82a7ac18671c7e9e0d17a1ceb9359a5ad',
  },
})
gitment.render('container')
</script>
