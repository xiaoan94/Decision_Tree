# Decision_Tree
## 决策树学习


###信息熵的公式：
$$H(X) = -\sum_{i=1}^n\ p(x_i)\log p(x_i)$$
其中$p(x_i)$代表随机事件$X$为$x_i$的概率

>* 信息量$-\log p(x_i)$是对一个具体事件发生所产生的信息的度量，事件$x_i$发生的概率越小，产生的信息量越大

>* 熵$H(X)$是在结果出来之前对可能产生的信息量的期望。考虑该随机变量$X$的所有可能取值，即所有可能发生事件所带来的信息量的期望

>* 信息熵可以度量一个系统的复杂程度。若系统越复杂，混合数据越多，随机变量取值的种类越多，则信息熵更高

###条件熵的公式:
\begin{equation}
\begin{aligned}
H(X)&=\sum_{x\epsilon X}p(x)H(Y|X=x)\\
&=-\sum_{x\epsilon X}p(x)\sum_{y\epsilon Y}p(y|x)\log p(y|x)\\
&=-\sum_{x\epsilon X}\sum_{y\epsilon Y}p(x, y)\log p(y|x)
\nonumber
\end{aligned}
\end{equation}

>* 条件熵的定义：在随机变量$X$的条件下，$Y$的条件概率分布的熵对$X$的数学期望。
>* 用随机变量$X$对随机变量$Y$进行分类后，随机变量$Y$的不确定性会减少，因为随机变量$Y$获得了随机变量$X$的信息。信息增益就是不确定性减少的程度。

###信息增益=信息熵-条件熵
数据集$X$在特征$Y$下的信息增益：
$$IG(Y)=H(X)-H(X|Y)$$

>* 信息增益代表在一定的条件下，信息的复杂度（不确定性）减少的程度
>* 决策树选取的特征是信息增益最大的特征，即在这个特征下，信息的复杂度减少的最多
