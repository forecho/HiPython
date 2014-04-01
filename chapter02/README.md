#Python基础

1. 坚持使用4个空格为缩进
1. Python 程序大小写敏感
1. Python内置的一种数据类型是列表：`list`。`list`是一种有序的集合，可以随时添加和删除其中的元素。(可以理解为数组)，示例：```classmates = ['Michael', 'Bob', 'Tracy']```
1. 另一种有序列表叫元组：`tuple`。`tuple`和`list`非常类似，但是`tuple`一旦初始化就不能修改。示例：```classmates = ('Michael', 'Bob', 'Tracy')```
1. `tuple`的陷阱：当你定义一个`tuple`时，在定义的时候，tuple的元素就必须被确定下来。只有1个元素的`tuple`定义时必须加一个逗号`,`，来消除数学公式中的小括号歧义。
1. 要创建一个内容也不变的`tuple`怎么做？那就必须保证`tuple`的每一个元素本身也不能变。
1. elif是else if的缩写。
1. Python的循环有两种，一种是for...in循环，**依次把list或tuple中的每个元素迭代出来**。
1. 用Ctrl+C（或 control+z）退出程序，或者强制结束Python进程。
1. Python内置了字典：`dict`的支持，`dict`全称dictionary，在其他语言中也称为`map`，使用键-值（key-value）存储，具有极快的查找速度(可以理解为JSON)。格式示例：```d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}```
2. 和`list`比较，`dict`有以下几个特点：查找和插入的速度极快，不会随着key的增加而增加；需要占用大量的内存，内存浪费多。所以，`dict`是用空间来换取时间的一种方法。
3. `dict`的key必须是不可变对象。
4. 通过key计算位置的算法称为哈希算法（Hash）。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而`list`是可变的，就不能作为key。
5. `set`和`dict`类似，也是一组key的集合，但不存储value。由于key不能重复，所以，**在set中，没有重复的key。**
6. `set`可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作。
7. `set`和`dict`的唯一区别仅在于没有存储对应的value，但是，`set`的原理和`dict`一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
8. 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。