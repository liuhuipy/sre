# Python知识点总结(默认使用python3.x)

## python基础知识
* python的输入输出
```
# 1.输入
>>> a = input()             #python2.x中input()或raw_input()，input()方法只能输入数字，raw_input()方法返回str类型数据
sssdd
>>> print(a, type(a))       #返回的一个str类型数据
sssdd <class 'str'>
# 2.输出
print('Hello World!')       #python2.x中print 'Hello World!'或print('Hello World!')
```
* python导入一个模块
```
from A import B
import xx
```

## python常见的数据结构：
* 数字(Number)、字符串(Str)、列表(List)、元组(Tuple)、字典(Dict)、集合(Set)等

## 数字
```
python3支持int、float、bool、complex类型。
python3没有python2中的long类型
>>> a, b, c, d = 2, 2.2, True, 4+3j
>>> print(type(a), type(b), type(c), type(d))
<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
```

## 字符串
```
# 1.字符串连接
>>> s1 = 'abc'
>>> s2 = 'def'
>>> s1 += s2
>>> s1
'abcdef'
# 2.查找字符
>>> sS = 'c'
>>> s1.index(sS)        #返回该字符的位置
2
# 3.字符串格式化
>>> '%s is %s years old!!' % ('lbw', 20)
'lbw is 20 years old!!'
# 4.字段宽度和精度
>>> from math import pi
>>> pi
3.141592653589793
>>> 'Pi: %10f' % pi
'Pi:   3.141593'
>>> 'Pi:%.2f' % pi
'Pi:3.14'
# 5.find方法可以在一个较长的字符串中查找子字符串。并返回子串所在位置的最左端索引。
>>> title = "monty python's Flying Circus"
>>> title.find('monty')
0
>>> title.find('python')
6
# 6.join方法是非常重要的字符串方法，它是split方法的逆方法，用来在队列中添加元素
>>> seq = [1,2,3,4,5]
>>> sep = '+'
>>> sep.join(seq)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 0: expected str instance, int found
>>> seq = ['1','2','3','4','5']
>>> sep.join(seq)
'1+2+3+4+5'
>>> '/'.join(seq)
'1/2/3/4/5'
# 7.lower方法返回字符串的小写字母版
>>> 'Treandheim Heardeer Dance'.lower()
'treandheim heardeer dance'
# 8.replace方法返回某字符串的所有匹配项均被替换之后得到的字符串
>>> 'Treandheim Heardeer Dance'.replace('r','ss')
'Tsseandheim Heassdeess Dance'
# 9.split方法是join的逆方法，用来将字符串分割成序列
>>> '1+2+3+4+5'.split('+')
['1', '2', '3', '4', '5']
# 10.strip方法返回去除两侧空格的字符串
>>> '  insert into afds, dsf    '.strip()
'insert into afds, dsf'
```

## 列表
* 列表是可变类型的(mutable)----可以改变列表的内容
```
# 1.列表长度、最大值和最小值。使用内建函数len、max和min。
>>> alist = [1,2,3,4,5]
>>> len(alist)
5
>>> max(alist)
5
>>> min(alist)
1
# 2.元素赋值
>>> alist[1] = 1
>>> alist
[1, 1, 3, 4, 5]
# 3.删除元素
>>> del alist[1]
>>> alist
[1, 3, 4, 5]
# 4.索引
>>> alist[0]                    
1
>>> alist[-1]
5
# 5.切片
>>> alist[:3]                   
[1, 3, 4]
>>> alist[:]
[1, 3, 4, 5] 
>>> alist[0:4:2]            #步长为2
[1, 4]
>>> alist[4:] = [6,7,8]     #切片赋值
>>> alist
[1, 3, 4, 5, 6, 7, 8]
>>> alist[1:1] = [2]
>>> alist
[1, 2, 3, 4, 5, 6, 7, 8]
# 6.append方法用于在列表末尾追加新的对象
>>> alist.append(6)
>>> alist
[1, 2, 3, 4, 5, 6, 7, 8, 6]
# 7.count方法统计某个元素在列表中出现的次数
>>> alist.count(6)
2
>>> alist.count(3)
1
# 8.extend方法可以
>>> a = [2,2]
>>> alist.extend(a)
>>> alist
[1, 2, 3, 4, 5, 6, 7, 8, 6, 2, 2]
# 9.index方法用于从列表中找出某个值第一个匹配项的索引位置
>>> alist.index(6)
5
# 10.insert方法用于将对象插入到列表中
>>> alist.insert(3, 'four')
>>> alist
[1, 2, 3, 'four', 4, 5, 6, 7, 8, 6, 2, 2]
# 11.pop方法会移除列表中的一个元素(默认是最后一个)，并返回该元素的值
>>> alist.pop()
2
>>> alist.pop()
2
>>> alist
[1, 2, 3, 'four', 4, 5, 6, 7, 8, 6]
# 12.remove方法用于移除列表中某个值的第一个匹配项
>>> alist.remove(6)
>>> alist
[1, 2, 3, 'four', 4, 5, 7, 8, 6]
>>> alist.remove(8)
>>> alist
[1, 2, 3, 'four', 4, 5, 7, 6]
# 13.reverse方法将列表中的元素反向存放
>>> alist.reverse()
>>> alist
[6, 7, 5, 4, 'four', 3, 2, 1]
# 14.sort方法用于在原位置对列表进行排序
>>> alist.remove('four')                    #str和int之间不能排序，先移除'four'字符串
>>> alist.sort()
>>> alist
[1, 2, 3, 4, 5, 6, 7]
>>> x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
>>> x.sort()
>>> x
['aardvark', 'abalone', 'acme', 'add', 'aerate']
>>> x.sort(key=len)                         #sort方法有另外两个可选参数--key和reverse
>>> x
['add', 'acme', 'aerate', 'abalone', 'aardvark']
# 15.list()方法将其他数据类型转换成list类型
>>> a = list('12345')
>>> a
['1', '2', '3', '4', '5']
>>> type(a)
<class 'list'>
```

## 元组
* 元组是不可变类型的()
```
# 1.len()、max()、min()方法分别返回元组元素的个数，元组中元素最大值、最小值
>>> len(a)
3
>>> max(a)
3
>>> min(a)
1
# 2.count()方法查找元组中某元素出现的次数
>>> a.count(1)
1
# 3.index()方法查找元组中某元素第一个索引值
>>> a.index(3)
2
# 4.tuple()返回一个元组
>>> seq = ['a','b','c']
>>> seq[1]
'b'
>>> tuple(seq)
('a', 'b', 'c')
```

## 字典
* 字典是Python中唯一内建的映射类型。字典中的值并没有特殊的顺序，但是都存储在一个特定的键(Key)里。
键可以是数字、字符串甚至是元组。
* 创建和使用字典:
    - phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
* 字典由多个键及与其对应的值构成的对组成。字典中的键是唯一的。
```
# 1.dict函数
>>> items = [('name', 'Gumby'), ('age', 42)]
>>> d = dict(items)
>>> d
{'name': 'Gumby', 'age': 42}
>>> d['name']
'Gumby'
# 2.返回字典键值对的数量
>>> len(d)
2
# 3.d[k]返回关联到键k上的值
>>> d['age']
42
# 4.d[k] = v将值v关联到键k上
>>> d['home'] = 'China'
>>> d
{'name': 'Gumby', 'age': 42, 'home': 'China'}
# 5.del d[k]删除键为k的项
>>> del d['home']
>>> d
{'name': 'Gumby', 'age': 42}
# 6.k in d检查字典中是否含有键为k的项
>>> 'name' in d
True
>>> 'aaa' in d
False
# 7.clear方法清除字典中所有的项。这是原地操作(类似于list.sort)
>>> d.clear()
>>> d
{}
# 8.copy方法返回一个具有相同键值对的新字典(这个方法实现的是浅复制)
>>> x = {'username': 'admin', 'machines': ['foo','bar','baz']}
>>> y = x.copy()
>>> y
{'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
>>> x['username'] = 'root'
>>> x['machines'].remove('foo')
>>> x
{'username': 'root', 'machines': ['bar', 'baz']}
>>> y
{'username': 'admin', 'machines': ['bar', 'baz']}
# 3.fromkeys方法使用给定的键建立新的字典，每个键默认对应的值为None
>>> dict.fromkeys(a)
{1: None, 2: None, 3: None}
>>> dict.fromkeys(a, 'unknown')                 #指定默认值
{1: 'unknown', 2: 'unknown', 3: 'unknown'}
# 4.get方法是个更宽松的访问字典项的方法
>>> b = {1: 'unknown', 2: 'unknown', 3: 'unknown'}
>>> print(b.get(4))                             #get访问一个不存在的键时，没有任何异常，得到了None值。
None
>>> print(b.get(3))
unknown
# 5.has_key方法可以检查字典中是否含有给出的键。表达式d.has_key(k)相当于表达式k in d。python3.x没有这个函数
# 6.items方法返回一个迭代器对象。python2.x中items方法将所有的字典项以列表方式返回，iteritems方法相当于python3.x中的items方法
>>> d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
>>> d.items()
dict_items([('spam', 0), ('title', 'Python Web Site'), ('url', 'http://www.python.org')])
# 7.keys方法将字典中的键以列表形式返回
>>> d.keys()
dict_keys(['spam', 'title', 'url'])
# 8.pop方法用来获得对应于给定键的值，然后将这个键值对从字典中删除
>>> d
{'spam': 0, 'title': 'Python Web Site', 'url': 'http://www.python.org'}
>>> d.pop('spam')
0
>>> d
{'title': 'Python Web Site', 'url': 'http://www.python.org'}
# 9.popitem方法类似于list.pop，不过popitem弹出随机的项，list.pop弹出列表最后一个元素。
>>> d.popitem()
('title', 'Python Web Site')
# 10.setdefault方法在某种程度上类似于get方法，就是能够获得与给定键相关联的值，除此之外，还能在字典
# 中不含有给定键的情况下设定相应的键值。
>>> d.setdefault('url')
'http://www.python.org'
>>> d.setdefault('name','N/A')
'N/A'
>>> d
{'name': 'N/A', 'url': 'http://www.python.org'}
# 11.update方法可以利用一个字典项更新另外一个字典
>>> d = {'title': ' Python Web Site', 'url': 'http://www.python.org', 'changed': 'Mar 22:02:21 2017'}
>>> x = {'title': 'Python Language Website'}
>>> d.update(x)
>>> d
{'changed': 'Mar 22:02:21 2017', 'title': 'Python Language Website', 'url': 'http://www.python.org'}
# 12.values方法以列表的形式返回值的迭代器。python2.x中values方法返回字典中的值，itervalues方法相当于python3.x中values方法。
>>> d.values()
dict_values(['Mar 22:02:21 2017', 'Python Language Website', 'http://www.python.org'])
```

## 集合
```
# 集合set是Python中一种基本数据类型，它分为可变集合(set)和不可变集合(frozenset)两种。类似于其他语言，集合是一个无序不
# 重复元素集，包括集合set、向集合中添加元素、删除集合中的元素、求集合的交集、并集、差集等操作。
# 1.set创建集合。set集合类需要的参数必须是迭代器类型的。如：序列、字典等，然后转换成无序不重复的元素集。
>>> ss = set([])                    #创建空集合
>>> ss
set()
>>> st = set(())
>>> st
set()
>>> s = set('createSet')            #创建非空集合
>>> s
{'c', 'a', 't', 'S', 'e', 'r'}
>>> s1 = set([1,2,3,4,5,6,7])
>>> s1
{1, 2, 3, 4, 5, 6, 7}
# 2.集合添加
>>> s1.add('f')                     #add方法把要传入的元素作为一个整体添加到集合中
>>> s1
{1, 2, 3, 4, 5, 6, 7, 'f'}
>>> s1.update('8910')               #update把要传入的元素拆分成单个字符，存入集合中，并去掉重复的字符
>>> s1
{1, 2, 3, 4, 5, 6, 7, '8', '9', '0', 'f', '1'}
# 3.集合删除
>>> s1.remove(4)
>>> s1
{1, 2, 3, 5, 6, 7, '8', '9', '0', 'f', '1'}
# 4.集合的遍历
>>> for i in s1:                    #集合的遍历跟序列的遍历方法完全一样
...     print(i, end=' ')
... 
1 2 3 5 6 7 8 9 0 f 1
# 5.pop()方法删除并返回一个元素
>>> s1.pop()
1
>>> s1
{2, 3, 5, 6, 7, '8', '9', '0', 'f', '1'}
>>> s1.pop()
2
>>> s1
{3, 5, 6, 7, '8', '9', '0', 'f', '1'}
>>> s1.pop()
3
# 6.交集
>>> st1 = set('python')
>>> st2 = set('php')
>>> st1 & st2
{'p', 'h'}
# 7.并集
>>> st3 = set('html')
>>> st1 | st3
{'m', 'h', 't', 'y', 'l', 'o', 'n', 'p'}
# 8.差集
>>> st1 - st2
{'o', 't', 'y', 'n'}
>>> st1 - st3
{'o', 'n', 'y', 'p'}
```

## range()和xrange()
* python3.x：range()函数与python2.x中的xrange()一样，返回的是一个生成器。
* python2.x：range()生成一个列表，xrange()返回一个生成器，用法和range()一样。
```
>>> range(2,10)
range(2, 10)
>>> type(_)
<class 'range'>
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> for i in range(0,10,2):
...     print(i, end=' ')
... 
0 2 4 6 8 
```

## 条件、循环和其他语句
* 略。。。和其他语言没有太大差异

## python内置函数
* abs()函数获取绝对值
```
>>> abs(-10)
10
>>> a = -10
>>> a.__abs__()
10
```
* bin(),oct(),hex()三个函数将十进制分别转换为2/8/16进制
* bool()函数测试一个对象是True还是False
```
>>> bool(1)
True
>>> bool(1 == 2)
False
```
* bytes()函数将一个字符串转换成字节类型
```
>>> s = 'python'
>>> x = bytes(s, encoding='utf8')
>>> x
b'python'
>>> a = '湖北'
>>> y = bytes(a, encoding='utf8')
>>> y
b'\xe6\xb9\x96\xe5\x8c\x97'
```
* str()函数将字符类型/数值类型等转换为字符串类型
```
>>> str(b'\xe6\xb9\x96\xe5\x8c\x97', encoding='utf8')
'湖北'
>>> str(222)
'222'
```
* callables()函数判断对象是否可以被调用，能被调用的对象就是一个callables对象。
```
>>> callable([1,2,3])
False
>>> callable(abs)
True
>>> callable(max)
True
>>> callable(str)
True
>>> callable('str')
False
```
* chr(),ord()函数查看十进制数对应的ASCII字符和查看某个ASCII对应的十进制数
```
>>> chr(66)
'B'
>>> ord('B')
66
```
* complex()复数函数
* delattr()删除对象的熟悉
* eval()将一串基本数据类型的字符串，转化成基本数据类型
```
>>> alist = "[1,2,3,4]"
>>> l = eval(alist)
>>> l
[1, 2, 3, 4]
```
* dir()查看某个类型下的所有方法
```
>>> l = [1,2,3]
>>> dir(l)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
  '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
  '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', 
  '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
   'remove', 'reverse', 'sort']
```
* divmod()获取两个数相除后的商和余数
```
>>> divmod(5,2)
(2, 1)
```
* max(),min(),sum()分别获取某个可迭代对象的最大值，最小值，和。
* pow(a,b)获取a的b次方
```
>>> pow(3,3)
27
```
* type()查看数据类型
```
>>> type('aaa')
<class 'str'>
>>> type([1,1,1])
<class 'list'>
>>> type({1:2})
<class 'dict'>
```
* filter()将一个可迭代对象按某种特定方式过滤，生成一个新的可迭代对象
```
>>> for i in f:
...     print(i, end=',')
... 
6,7,8,9,
```
* sorted()将一个可迭代序列排序，与list.sort不同的是，sorted()将返回一个排序后的副本，而不是原地排序。
```
>>> a = [4,2,6,1,3]
>>> sorted(a)
[1, 2, 3, 4, 6]
>>> a
[4, 2, 6, 1, 3]
```
* zip()将两个或多个列表拼接成一个元组列表
```
>>> list1 = [1,2,3,4]
>>> list2 = ['a','b','c','d']
>>> z = zip(list1, list2)
>>> z
<zip object at 0x102975a88>
>>> for i in z:
...     print(i)
... 
(1, 'a')
(2, 'b')
(3, 'c')
(4, 'd')
```
* map()函数包含两个参数，第一个是一个函数，第二个是序列。
```
def f(x):
    return x * x

print(map(f, [1,2,3,4,5,6,7,8,9]))
输出结果：<map object at 0x1005a1a20>        
python2.x中输出结果：[1, 4, 9, 10, 25, 36, 49, 64, 81]
```


## 正则表达式
* 正则表达式为高级的文本模式匹配、抽取、或文本形式的搜索和替换功能提供基础。简单的说，正则表达式(regex)是一些由字符和特殊符号
组成的字符串，它们描述了模式的重复或者表述多个字符，于是正则表达式能按照某种模式匹配系列有相似特征的字符串。
* python通过标准库中的re模块来支持正则表达式。
### 特殊符号和字符
* 使用择一匹配符配多个正则表达式模式
   - 表示择一匹配的管道符号(|)，表示一个'从多个模式中选择其一'的操作。它用于分割不同的正则表达式。
   ```
   正则表达式模式              匹配的字符串
   at | home                 at、home
   r2de | c3po               r2d2、c3po
   bat | bet | bit           bat、bet、bit   
   ```
* 匹配任意单个字符
   - 点号或者句点(.)符号匹配除了换行符\n以外的任何字符()。
   ```
   正则表达式模式              匹配的字符串
   f.o                       匹配在字母"f"和"o"之间的任意一个字符：例如fao、fco、foo、f#o等 
   ..                        任意两个字符
   ```
* 从字符串起始或结尾或单词边界匹配
   - 有些符号和相关的特殊字符用于在字符串的起始和结尾部分指定用于搜索的模式。
   ```
   正则表达式模式              匹配的字符串
   ^From                     任何以From开头的字符串
   /bin/tcsh$                任何以/bin/tcsh结尾的字符串
   ^Subject:hi$              任何由单独的字符串Subject:hi构成的字符串
   ```
* 创建字符集
   - 匹配方括号中包含的任何字符。
   ```
   正则表达式模式              匹配的字符串
   b[aeiu]t                  bat、bet、bit、but
   [cr][23]                  c2、c3、r2、r3   
   ```
* 限定范围和否定
   - 方括号中两个符号之间用连字符(-)连接，用于指定一个字符的范围。
   ```
   正则表达式模式              匹配的字符串
   z.[0-9]                   字母'z'后面跟着任何一个字符，然后跟着一个数字
   [a-z]                     一个小写字母  
   ```
* 实现存在性和频数匹配
   - '+'操作符将匹配一次或者多次出现的正则表达式
   - '?'操作符将匹配零次或者一次出现的正则表达式
   - '*'操作符将匹配其左边正则表达式出现零次或者多次的情况
* 表示字符集的特殊字符
   - 使用\d表示匹配任何的十进制数字相当于[0-9]；使用\w能够用于表示全部字母数字的字符集，相当于[A-Za-z0-9]。
* 使用圆括号指定分组
   - (\w+)-(\d+)
### re模块：核心函数和方法
* 匹配对象以及group()和groups()方法
    - group()要么返回整个匹配对象，要么根据要求返回特定子组。groups()则仅返回一个包含唯一或者全部子组的元组。    
* 使用match()方法匹配字符串
```
# match()函数试图从字符串的起始部分对模式进行匹配。如果匹配成功，就返回一个匹配对象。匹配失败则返回None。匹配对象的
# group()方法能够用于显示那个成功的匹配。
>>> import re
>>> m = re.match('foo', 'foo')
>>> if m is not None:
...     m.group()
... 
'foo'
>>> m
<_sre.SRE_Match object; span=(0, 3), match='foo'>
>>> m = re.match('foo', 'far')                      #如果匹配失败，则返回None
>>> if m is not None:
...     m.group()
... 
>>> m = re.match('foo', 'food on the table')        #匹配成功。只要模式从字符串的起始部分开始匹配，即使字符串比模式
                                                    #长，匹配也仍然能够成功
>>> m.group()
'foo'
```
* 使用search()在一个字符串中查找模式(搜索与匹配的对象)。search()会用它的字符串参数，在任意位置对给定正则表达式模式搜索
第一次出现的匹配情况。
```
>>> m = re.match('foo', 'seafoo')                   #如果使用match()方法，它会从字符串起始位置开始匹配模式，即'f'
>>> if m is not None: m.group()                     #将匹配到字符串的首字母's'上，故匹配失败
... 
>>> m = re.search('foo', 'seafoo')                  #search()函数不但会搜索模式在字符串中第一次出现的位置，而且会
>>> if m is not None: m.group()                     #严格地对字符串从左到右搜索。故匹配成功
... 
'foo'
```
* 匹配多个字符串
```
>>> bt = 'bat|bet|bit'                              #正则表达式模式：bat、bet、bit
>>> m = re.match(bt, 'bat')                         #'bat'是一个匹配
>>> if m is not None: m.group()
... 
'bat'
>>> m = re.match(bt, 'blt')                         #'blt'没有匹配成功
>>> if m is not None: m.group()
... 
>>> m = re.match(bt, 'He bit me!')                  #不能匹配字符串
>>> if m is not None: m.group()
... 
>>> m = re.search(bt, 'He bit me!')                 #通过搜索查找'bit'
>>> if m is not None: m.group()
... 
'bit'
```
* 匹配任何单个字符
```
>>> anyend = '.end'
>>> m = re.match(anyend, 'bend')                    #点号匹配'b'
>>> if m is not None: m.group()
... 
'bend'
>>> m = re.match(anyend, '\nend')                   #除了\n之外的任何字符
>>> if m is not None: m.group()
... 
>>> m = re.search(anyend, 'The end')                #在搜索中匹配' '
>>> if m is not None: m.group()
... 
' end'
```
* 创建字符集
```
>>> m = re.match('[cr][23][dp][o2]', 'c3po')        #匹配'c3po'
>>> if m is not None: m.group()
... 
'c3po'
>>> m = re.match('[cr][23][dp][o2]', 'c2do')        #匹配'c2do'
>>> if m is not None: m.group()
... 
'c2do'
>>> m = re.match('[cr][23][dp][o2]', 'ccdo')        #不匹配'ccdo'
>>> if m is not None: m.group()
... 
```
* 重复、特殊字符以及分组
```
>>> patt = '\w+@(\w+\.)?\w+\.com'                   #'(\w+\.)?\w+'匹配主机名,包含0个或1个子域名
>>> re.match(patt, 'nobody@xxx.com').group()
'nobody@xxx.com'
>>> re.match(patt, 'nobody@xxx.yyy.com').group()
'nobody@xxx.yyy.com'
>>> patt = '\w+@(\w+\.)*\w+\.com'
>>> re.match(patt, 'nobody@xx.yy.zz.aa.com').group()    #允许任意数量的中间子域名存在
'nobody@xx.yy.zz.aa.com'
>>> m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')        #匹配分组
>>> m.group()                                           #完整匹配
'abc-123'
>>> m.group(1)                                          #子组1
'abc'
>>> m.group(2)                                          #子组2
'123'
>>> m.groups()                                          #全部子组
('abc', '123')
```
* 使用findall()和finditer()查找每一次出现的位置
    - findall()查询字符串中某个正则表达式模式全部的非重复出现情况。总是返回一个列表，如果匹配失败则返回空列表。
    ```
    >>> re.findall('car','car')
    ['car']
    >>> re.findall('car','scary')
    ['car']
    >>> re.findall('car','carry my team the barcardi to the car')
    ['car', 'car', 'car']
    ```
    - finditer()函数完成的所有额外工作都旨在获取它的输出来匹配findall()的输出。
* 使用sub()和subn()搜索与替换
    - subn()和sub()都是将某字符串中所有匹配正则表达式的部分进行某种形式的替换。subn()和sub()一样，但subn()
    还返回一个表示替换的总数，与替换后的字符串作为元组返回。
    ```
    >>> re.sub('X', 'liuhui', 'My name is X,X niubi!')
    'My name is liuhui,liuhui niubi!'
    >>> re.sub('[ae]', 'XX', 'abcedfg')
    'XXbcXXdfg'
    >>> re.subn('[ae]', 'XX', 'abcedfg')
    ('XXbcXXdfg', 2)
    ```
* 在限定模式上使用split()分隔字符串
    - 如果给定分隔符不是使用特殊符号来匹配多重模式的正则表达式，那么re.split()与str.split()工作方式相同。
    ```
    >>> re.split(':', 'str1:str2:str3')
    ['str1', 'str2', 'str3']
    ```
    - 更复杂的处理
    ```
    >>> DATA = (
    ...     'Mountain View, CA 94040',
    ...     'Sunnyvale, CA',
    ...     'Los Altos, 94023',
    ...     'Cupertino 95014',
    ...     'Palo Alto CA',
    ... )
    >>> for datum in DATA:
    ...     print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum))
    ... 
    ['Mountain View', 'CA', '94040']
    ['Sunnyvale', 'CA']
    ['Los Altos', '94023']
    ['Cupertino', '95014']
    ['Palo Alto', 'CA']
    ```
* 正则表达式应用示例
```
#创建编写rewho.py程序
import re

f = open('whodata.txt', 'r')
for eachLine in f:
    print(re.split(r'\s\s+', eachLine))
f.close()

#将who命令结果输出到whodata.txt文件中
$ who > whodata.txt
$ python rewho.py                           #执行rewho.py
['liuhui', 'console', 'Dec 12 17:33']
['liuhui', 'ttys000', 'Dec 14 19:45']
['liuhui', 'ttys002', 'Dec 18 15:46']

#创建编写rewho2.py。在不手动创建whodata.txt文件情况下，使用os.popen方法获取命令结果。
import os
import re

with os.popen('who', 'r') as f:
    for eachLine in f:
        print(re.split(r'\s\s+|\t', eachLine.strip()))

$ python rewho2.py 
['liuhui', 'console', 'Dec 12 17:33']
['liuhui', 'ttys000', 'Dec 14 19:45']
['liuhui', 'ttys002', 'Dec 18 15:46']
```


## 网络编程
### 套接字(Socket)
* 套接字地址：主机-端口号
* 面向连接的套接字：面向连接的通信提供序列化的、可靠的和不重复的数据交付，而没有记录边界。
* 无连接的套接字


## python监控Linux系统
### 多功能系统资源统计工具dstat
* dstat是一个用Python语言实现的多功能系统资源统计工具，用来取代Linux下的vmstat、iostat、netstat和ifstat等命令。
* dstat功能特性：
    - 综合了vmstat、iostat、ifstat、netstat等监控工具的功能，并且提供了更多的监控信息；
    - 实时显示监控数据；
    - 在问题分析和故障排查时，可以监视最重要的计数器，也可以对计数器进行排序；
    - 模块化设计；
    - 使用Python语言编写，更方便扩展现有的工作任务；
    - 容易扩展，便于添加自定义的计数器；
    - 包含许多扩展插件；
    - 可以分组统计块设备/网络设备，并给出汇总信息；
    - 可以显示每台设备中断信息；
    - 非常准确的时间精度，即便是系统负荷较高也不会延迟显示；
    - 准确显示单位，限制转换误差范围；
    - 用不同的颜色显示不同的单位，增加可读性；
    - 支持CSV格式输出，便于将监控信息导入Gnumeric和Excel以生成图形。
* 安装使用dstat（这里使用Centos7）
```angular2html
yum install dstat
dstat --version         # 除了显示dstat的版本之外，还会显示操作系统的版本、Python语言的版本、cpu的个数，
                        # 以及dstat支持的插件列表等详细信息。

dstat --list            # 直接在终端输入dstat命令，dstat将以默认参数运行。默认情况下，dstat会收集cpu、磁盘、网络、
                        # 换页和系统信息，并以一秒钟一次的频率进行输出，直到我们按ctrl+c结束。
            
```
* dstat常用选项
    - -c：显示cpu的使用情况。显示了cpu时间花费在各类操作的百分比，包括执行用户代码(usr)、执行系统代码(sys)、空闲(idl)和
    等待IO(wai)。如果usr的值较高，说明当前系统钟cpu负载较大；如果wai长期处于较大值，说明IO等待比较严重；
    - -d：显示磁盘的读写情况，在进行性能测试时可以使用该字段观察当前的磁盘负载；
    - -n：网络设备发送和接收的数据，这一栏显示网络收发数据的总数。







