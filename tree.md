#列表的append和extend方法
```python
>>> a= [1, 2, 3] 

>>> b= [4, 5, 6] 

>>> a.append(b)

[1, 2, 3, [4, 5, 6]] 
>>> a.extend(b)

[1, 2, 3, 4, 5, 6]  
```

#列表的count方法
###str.count(sub, start=0, end=len(string))用于统计字符串中的子字符串出现的次数，可选参数为在字符串中搜索的开始和结束的位置。
>* sub 为要搜索的子字符串
>* start为字符串开始搜索的位置，默认为字符串的第一个字符的位置，第一个字符的索引值为0
>* end为字符串结束搜索的位置，默认为字符串的最后一个位置。
```python
>>> str = "this is string example....wow!!!"

>>> str.count("i", 4, 40)

2

>>> str.count("wow")

1
```

#列表的del用法
###删除列表或列表中的某些元素
```python
>>> a = [-1, 3, 'aa', 85] 
>>> a
[-1, 3, 'aa', 85]
>>> del a[0] # 删除第0个元素
>>> a
[3, 'aa', 85]
>>> del a[2:4] # 删除从第2个元素开始，到第4个为止的元素。包括头不包括尾
>>> a
[3, 'aa']
>>> del a # 删除整个list
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```

#matplotlib图标正常显示中文
```python
>>> import matplotlib.pyplot as plt
>>> plt.rcParams['font.sas-serig']=['SimHei'] #用来正常显示中文标签
>>> plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
```
