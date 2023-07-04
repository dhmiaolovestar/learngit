import math,myelse#引用ceil函数，先声明使用math模块，import 文件名，即可使用该py文件内所有的函数，以方式的形式使用
#import 文件名 as 更改名，更改名.引用函数名（函数内变量（没有就空着））
from myelse2 import less
#也可以用，from 文件名 import 引用函数名，可只
#from myelse2 import *，可以导入该文件中的所有函数，可直接以函数的形式使用

a=1
b=2

zz=myelse.sum(a,b)#引用自己所建函数，或系统自带文件函数，文件名.引用函数名（函数内变量（没有就空着））
print(zz)
yy=less(b,a)#当只导入一个函数时，直接以函数的形式使用该函数，引用函数名（函数内变量（没有就空着））
print(yy)

print(a+b)#print是输出

c="沙壁当"
d="老壁灯"
print(c+d[0:2])#加双引号代表字符串类型的变量，d[0:2]代表从d的第一位到第三位（切片），第三位不算，[a]代表第a+1个字符，[a:b]代表第b+1到a个字符

def sum(sum1,sum2):#def 函数名（函数中变量1，函数中变量2）：函数内部
	result=sum1+sum2
	return result#返回result作为函数值
#取消缩进即代表该函数结束
e=sum(a,b)
print(e)

class person:#类型class 类型名：
	def __init__(self,name,high,wright):#def __init__(self,特征一，特征二)，特征为实例类型，初始化方法
		self.name = name#self.特征一=特征一
		self.high = high#self.特征二=特征二
		self.wright=wright

	def say(self):#类型中定义的函数称为方法，默认将个体传入到self中
		print("我是" + self.name)

f=person("dhm",175,140)#引用类型，实例名=类型名（特征一，特征二）

f.say()#使用类型中的方法，个体名.方式名（），默认将个体传入到self中


print(f.high)#通过.号访问个体，实例的特征，属性

g=1.5
h=2

print(g+h)#等输入整形时自动识别为整形，输入浮点型时自动识别为浮点型，运算时会优先同时转换为浮点型进行运算

#双斜杠是整除运算符//

print(float(h))#类型名（变量），表示将变量强制转换成该类型

#abs(a)取a的绝对值，round(a)四舍六入五凑偶，pow(a,b)a的b次方，math.ceil向上取整

print(round(g))
print(pow(g,h))
print(math.ceil(g))

print(111)
print(len(f.name))#len(字符串名)，代表字符串的长度，是函数

print(f.name.capitalize())#字符串名.capitalize（），代表将该字符串的首字母大写，是方式
print(f.name.upper())#字符串名.upper（），代表将该字符串的所有字母大写，是方式，字符串名.lower（），代表将该字符串的所有字母小写，是方式

print(f.name.replace("hm","sg"))#字符串名.replace("字符串中元素"，"需要改成的元素")，代表将该字符串中的元素进行定向替换，是方式
print(f.name.find("hm"))#查找该字符串中的第一个需要查找元素的位置

#布尔类型，a=Ture,b=False

print(f.name.isupper())#判断是否全部大写，输出为布尔类型

l=[1,2,3,4,5]#中括号是列表
l[3]=9#将列表中的第3+1项元素改成9
l.append(6)#在列表最后添加一项，数值是6
l.pop(3)#删除列表的第3+1项
l.remove(3)#删除列表中是3的元素
l.insert(1,0)#在列表的第1+1个位置插入一个0，该位置后面的元素均往后退一个位置
l.index(2)#查找列表的第一个二的位置
l.sort()#将列表中元素从小到大排列
l.reverse()#将列表中元素从大到小排列
print(l)

m=(1,2,3,4,5)#小括号是元组，也就是不能修改的列表，相当于常量
print(m[2])
print(m)

n=list(m)#将元组强制转换成列表

o={"name":"dhm","condition":'f',"else":[1,2,3],"else1":(1,2,3)}
#大括号代表字典，字典中存放键值对，字典名={"键值对名"："内容"}，内容可以是数字，字符串，元组，列表等
o["else2"] = 114514#在字典中添加元素，字典名【“添加元素名”】=内容
o.pop("else1")#删除字典的某一项，字典名.pop("要删除的键值对名")
print(o["else"])#调用字典中元素，中括号中是"键值对名"
print(o.keys())#keys表示键值对中所有的键值对名，是方法
print(o.values())#values表示键值对中所有的内容，是方法

p={1,2,4,3,2,3}#集合也同样使用大括号，其中为确定的值，集合名={数值}，集合中重复的元素会被自动删除,元素没有位置的概念，不能通过位置找元素
print(p)
q=set(l)#可以通过set(内容)，将列表，元组等强制转换为集合
print(q)
p.add(11)#在集合中加入元素
p.discard(4)#在集合中减少元素
print(p.intersection(q))#intersection求两集合的并集
print(p.difference(q))#求q的补集与p的交集
print(p.issubset(q))#判断q是否是p的子集


#值类型变量：数字，布尔
#引用类型变量：列表，元组，字典，集合，字符串

r=1
s=r
r=2
print(r,s)

r=1
s=r
s=2
print(r,s)
#变量名称直接对应它的值

u=[1,3,5]
v=u
u=[2,4,6]
print(u,v)

u=[1,3,5]
v=u
v=[2,4,6]
print(u,v)

u=[1,3,5]
v=u
u[1]=2
print(u,v)

u=[1,3,5]
v=u
v[1]=2
print(u,v)
#创建的【1，3，5】单独存放在一个地址中，列表名中存储的是地址，当v=u时，他们两个指向同一个地址，当该地址中 内容 变化时，他们两个列表同时变化
#每当再创建一个类似【2，4，6】时，都会给一个新的地址存放，v=[2,4,6]，也就是让v指向了一个新的地址，原来那个地址的变化不会再影响到v

if(1==1):
	print("Yes")
elif(1<1):
	print("OK")
else:
	print("No")
#Python在取消缩进前相当于一个代码块,只能一个if和一个else（可以嵌套多个条件与循环），elif可以有多个,:相当于c中的{}

w=1
while(w<=5):
	print(w)
	w=w+1

print("循环结束")

#序列：字符串，列表，元组等

x="donotgogental"
for y in x:#将x中含有的元素依次赋给y,for 被依次赋值的变量名 in 序列：执行语句
	print(y)

z=["do","not","go","gental"]
for y in z:
	print(y)

print(list(range(0,8,2)))
#range函数，第一个数字到第二个数字是一个左闭右开的区域，第三个数字是每个数字之间的间距，也就是从第一个数字数到小于最后一个数字的数字，该函数可转化为列表

aa=[1,2,3,4,5,6,1,6,1,3]
for y in range(0,len(aa),2):
	print(aa[y])
#运用range函数和for循环可隔位输出序列中的元素

print(list(range(5)))
#当range函数中只有一个数字时，则默认该数字为终止数字，默认起始数字为0，步距为1

for y in range(8):
	print(y)
	if(y==3):
		break
#用break可跳出上一级的循环


for y in range(8):
	if(y%2):
		continue
	print(y)
#continue语句表示跳过该次循环在continue后面的内容，直接去执行下一次循环