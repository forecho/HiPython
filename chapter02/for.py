# coding=utf-8
# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

sum = 0
for x in range(101):
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum