list1 = [9, 1, -4, 3, 7, 11, 3]
print(len(list1))
print(max(list1))
print(min(list1))
print('{}'.format(list1.count(3)))

# 列表的改变
list2 = ['a', 'c', 'd']

# 结尾添加一个新元素'e'
list2.append('e')
print('list2=', list2)

# 在a和c之间插入一个b
list2.insert(1, 'b')
print('list2=', list2)

# 删除list2里的b
list2.remove('b')
print('list2=', list2)

list2[0] = '1'
print(list2)

# 列表中的元素可更改，但字符串中特定元素的值不可改变，如下
# a = '123'
# a[0] = '4'

# 列表翻转
list3 = [1, 2, 3]
list3.reverse()
print('list3=',list3)

# 列表排序
list4 = [9, 1, -4, 3, 7, 11, 3]
# sort 默认是正向排序
list4.sort(reverse=True)
print('list4=', list4)

# 作业：复杂列表的上述应用练习
list5 = [1, 2, 'd', [1, 3], -7, ['a',5,'d']]

list6 =[1,2,3,4]
print(list6*2+[4,5,6])