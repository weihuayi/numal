# 线性方程组求解


本章主要讨论求解线性方程组 $$Ax=b$$ 的扰动理论，算法及误差分析， 具体包括如下内
容：

* 2.2 节给出 $$Ax=b$$ 的误差扰动理论，这是后面讨论实用误差界的基础。
* 2.3 节给出稠密矩阵的高斯消去算法。
* 2.4 节分析高斯消去算法的误差，并给出一个实用误差界。
* 2.5 讨论如何用一个简单低代价的迭代方法来改进高斯消去法的精度。
* 2.6 讨论如何管理计算的内存，从而加速高斯消去法和其它的线性代数方法。
* 2.7 讨论实际中经常出现的具有特殊性质的矩阵，更快的高斯消去法变体。
