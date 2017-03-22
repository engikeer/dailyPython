+ 变量变换
大部分编程语言中交换两个变量的值时，不得不引入一个临时变量
```python
# 通常写法
>>> a = 1
>>> b = 2
>>> tmp = a
>>> a = b
>>> b = tmp

# pythonic
>>> a, b = b, a
```
+ 循环遍历区间元素
```python
# 通常写法
for i in [0, 1, 2, 3, 4, 5]:
    print i


# pythonic
for i in range(6):
    print i
```
+ 带有索引位置的集合遍历
```python
# 通常写法
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print i, '--->', colors[i]

# pythonic
for i, color in enumerate(colors):
    print i, '--->', color
```
+ 字符串连接
```python
# 通常写法
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

s = names[0]
for name in names[1:]:
    s += ', ' + name
print s

# pythonic
print ', '.join(names)
```
+ 打开/关闭文件
使用 with 语句，系统会在执行完文件操作后自动关闭文件对象。
```python
# 通常写法
f = open('data.txt')
try:
    data = f.read()
finally:
    f.close()

# pythonic
with open('data.txt') as f:
    data = f.read()
```
+ 列表推导式
```python
# 通常写法
result = []
for i in range(10):
    s = i  2
    result.append(s)

# pythonic
[i2 for i in xrange(10)]
```
+ 善用装饰器  
装饰器可以把与业务逻辑无关的代码抽离出来，让代码保持干净清爽，而且装饰器还能被多个地方重复利用。比如一个爬虫网页的函数，如果该 URL 曾经被爬过就直接从缓存中获取，否则爬下来之后加入到缓存，防止后续重复爬取。
```python
# 通常写法
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

# pythonic
import urllib #py2
#import urllib.request as urllib # py3

def cache(func):
    saved = {}

    def wrapper(url):
        if url in saved:
            return saved[url]
        else:
            page = func(url)
            saved[url] = page
            return page

    return wrapper


@cache
def web_lookup(url):
    return urllib.urlopen(url).read()
```
+ 合理使用列表
    + 列表对象（list）是一个查询效率高于更新操作的数据结构，比如删除一个元素和插入一个元素时执行效率就非常低，因为还要对剩下的元素进行移动
    + deque 是一个双向队列的数据结构，删除元素和插入元素会很快
```python
# 通常写法
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']
names.pop(0)
names.insert(0, 'mark')

# pythonic
from collections import deque
names = deque(['raymond', 'rachel', 'matthew', 'roger',
               'betty', 'melissa', 'judith', 'charlie'])
names.popleft()
names.appendleft('mark')
```
+ 序列解包
```python
# 通常写法
p = 'vttalk', 'female', 30, 'python@qq.com'

name = p[0]
gender = p[1]
age = p[2]
email = p[3]

# pythonic
name, gender, age, email = p
```
+ 遍历字典的 key 和 value
    + 方法一速度没那么快，因为每次迭代的时候还要重新进行hash查找 key 对应的 value。
    + 方法二遇到字典非常大的时候，会导致内存的消耗增加一倍以上。
    + iteritems 返回迭代器对象，可节省更多的内存，不过在 python3 中没有该方法了，只有 items 方法，等值于 iteritems。


```python
# 通常写法
# 方法一
for k in d:
    print k, '--->', d[k]

# 方法二
for k, v in d.items():
    print k, '--->', v

# pythonic
for k, v in d.iteritems():
    print k, '--->', v
```
+ 链式比较操作
```python
# 通常写法
age = 18
if age > 18 and x < 60:
    print("yong man")

# pythonic
if 18 < age < 60:
    print("yong man")
# 所以
>>> False == False == True 
False
```
+ if/else 三目运算
```python
# 通常写法
if gender == 'male':
    text = '男'
else:
    text = '女'

# pythonic
text = '男' if gender == 'male' else '女'
```
+ 真值判断
```python
# 通常写法
if attr == True:
    do_something()

if len(values) != 0: # 判断列表是否为空
    do_something()

# pythonic
if attr:
    do_something()

if values:
    do_something()

```
+ for/else语句
```python
# 通常写法
flagfound = False
for i in mylist:
    if i == theflag:
        flagfound = True
        break
    process(i)

if not flagfound:
    raise ValueError("List argument missing terminal flag.")

# pythonic
for i in mylist:
    if i == theflag:
        break
    process(i)
else:
    raise ValueError("List argument missing terminal flag.")
```
+ 字符串格式化  
format更易于理解。
```python
# 通常写法
s1 = "foofish.net"
s2 = "vttalk"
s3 = "welcome to %s and following %s" % (s1, s2)

# pythonic
s3 = "welcome to {blog} and following {wechat}".format(blog="foofish.net", wechat="vttalk")
```
+ 列表切片  
获取列表中的部分元素最先想到的就是用 for 循环根据条件提取元素，这也是其它语言中惯用的手段，而在 Python 中还有强大的切片功能。
```python
# 通常写法
items = range(10)

# 奇数
odd_items = []
for i in items:
    if i % 2 != 0:
        odd_items.append(i)

# 拷贝
copy_items = []
for i in items:
    copy_items.append(i)

# pythonic
# 第1到第4个元素的范围区间
sub_items = items[1:4]
# 奇数
odd_items = items[1::2]
#拷贝
copy_items = items[::] 或者 items[:]
```
+ 列表元素的下标不仅可以用正数表示，还是用负数表示，最后一个元素的位置是 -1，从右往左，依次递减。
```python
--------------------------
 | P | y | t | h | o | n |
--------------------------
   0   1   2   3   4   5 
  -6  -5  -4  -3  -2  -1
--------------------------
```
+ 善用生成器  
生成器的好处就是无需一次性把所有元素加载到内存，只有迭代获取元素时才返回该元素，而列表是预先一次性把全部元素加载到了内存。此外用 yield 代码看起来更清晰。
```python
# 通常写法
def fib(n):
    a, b = 0, 1
    result = []
     while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# pythonic
def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
```
+ 获取字典元素
```python
# 通常写法
d = {'name': 'foo'}
if d.has_key('name'):
    print(d['name'])
else:
    print('unkonw')

# pythonic
d.get("name", "unknow") 
```
+ 预设字典默认值
```python
# 通常写法
data = [('foo', 10), ('bar', 20), ('foo', 39), ('bar', 49)]
groups = {}
for (key, value) in data:
    if key in groups:
        groups[key].append(value)
    else:
        groups[key] = [value]

# pythonic
#　第一种方式
groups = {}
for (key, value) in data:
    groups.setdefault(key, []).append(value) 

# 第二种方式
from collections import defaultdict
groups = defaultdict(list)
for (key, value) in data:
    groups[key].append(value)
```
+ 字典推导式
```python
# 通常写法
numbers = [1,2,3]
my_dict = dict([(number,number*2) for number in numbers])
print(my_dict)  # {1: 2, 2: 4, 3: 6}

# pythonic
numbers = [1, 2, 3]
my_dict = {number: number * 2 for number in numbers}
print(my_dict)  # {1: 2, 2: 4, 3: 6}

# 还可以指定过滤条件
my_dict = {number: number * 2 for number in numbers if number > 1}
print(my_dict)  # {2: 4, 3: 6}
```