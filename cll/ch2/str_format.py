name = 'Python'
age = 27
# 打印"我是Python,今年27岁了"
# new_str = "我是" + name + "," +"今年" + age +"岁了"
# print(new_str)

new_str_1= "我是%s,今年%d岁了"%(name,age)
print(new_str_1)

new_str_2 ="我是{},今年{}岁了".format(name,age)
print(new_str_2)

name1 ="111"
age1 = "2"

new_str_3 = f"我是{name1},今年{age1}岁了"
print(new_str_3)

#####
# 检测题验证
x = 'hello world'
y = x.split(' ')
print(x)
print(y)

z = ''.join(['hello','world'])
print(z)

# 课后题
a = 10
b = 2.1
c = a + b
print(c)