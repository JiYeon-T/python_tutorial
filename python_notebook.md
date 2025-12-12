1.
alt + N: last command
alt + P: next command

查看说明

```python
dir(list), 
dir(tuple)
```

base:

```python
print function
print("hello world\n" * 3)
print(3+5)
print("hello" + "world")	#add string
a = 'me too'
print('i love you.', a)		# 'i love you. me too'
print('i love you. %s' % a)	#'i love you. me too'
```

#compile python files on linux : 

```shell
touch new.py 
python3 new.py
```

3.game	

	print("Welcome to the game.")
	temp = input("Please enter the number:\n")	#default string type
	guess = int(temp)
	if guess == 8:
		print("You're right.\n")
	else:
		print("Wrong input.\n")
	print("This is the end of the game.try again later.")
```python
guess = int(temp)
temp = input()	#input() -> 'str' type
```

```python
5.BIF = Bulit-in-Function	## 内置函数
dir(__builtins__)#search for all the BIF in python
help(input)	#search for the information about input function;enter "Q" to quit.
dir(input)	#顯示input的所有內置方法
MyFirstFunction.__doc__ or  help(MyFirstFunction)	#help(xxx)帶格式顯示函數信息，xxx.__doc__不帶格式
dir(str)	#show all the 'BIF' of str,such as split....
```



6.varible
-----python doesn't have the clear varible type
-----It's diffenent between captial and lower case(qu fen da xiao xie)
eg:

```python
a = 1
A = 'string'
```

7.\\  	\'	\"		#zhuan yi zi fu

```python
print("Let's go")
print('Let\'s go')
print(""""Let's go.""")
```

8.""""""-----output a long string.

```python
str = """
eee,
qu xiang xiang tian ge,
hong mao fu lv shui,
hong zhang bo qing bo.
"""
```



9.

```python
print("Welcome to the game.")
temp = input("Please enter a number:\n")
guess = int(temp)
if(guess == 8):
    print("You're right.\n")
else:
    if(guess > 8):
	print("Too big\n")
else:
	print("Too small\n")
print("This is the end of the game.\n")
```

```python
while True:
    print("Welcome to the game.")
    temp = input("Please enter a number:\n")
    guess = int(temp)
    while guess != 8:
        print("Wrong,Enter again.\n")
        temp = input()
        guess = int(temp)
        if(guess > 8):
            print("Too big.\n")
        else:
        	print("Too small.\n")
    print("You're right.\n")
```

and &&

```pyton
print("Welcome to the game.")
temp = input("Please enter a number:\n")
guess = int(temp)
time = 1
while guess != 8 and time <=3:
    if(guess > 8):
        print("Too big.\n")
    else:
        print("Too small.\n")
    temp = input()
    guess = int(temp)
    time += 1
    if(guess == 8):
        print("You're right.\n")
    else:
        print("You don't have any chance.\n")
```

random module

```python
import random as r
#random模塊下面的函數：randint()
secret = r.randint(1, 10)#give a random integer value to secret between 1 and 10
```

12. value type: int  float  bool  str    str=string#強制類型轉換
    value type transformation: int(),  float(),  str()

```python
a = 5
str(a)		##transform value type  5 -> '5' 
'5'
```

type()	#This function can get the type of value

```python
#type()函數
a = '5'
type(a)	##class 'str', string varible
```

isinstance()##Judge whether two type of value is same. @return:ture false    ,bool

```python
a = 5
isinstance(a, int)#return true
#int is a class, a shi lei de shi li
```

operator: +  -  *  /  %  **(mi yun suan,ci fang, ping fang)  //(float division, )

```python
a += 3    # +=   -=   *=  /=
eg:
3/2 #result = 1.5
3//2#result = 1
3**2#result = 3 * 3 = 9
(-3)*(-3)  #if exist negative number in your program.You'd better add (bracket) #如果乘法中存在負數，最好加上括號(bracked)
```

1. Logic operator  and  or  not
2. elif time > 5:#elif = else if

18.conditional operator:

```python
small = x if x < y else y	# if x<y is ture,small = x,else small = y


```

19.		#for circle  is different from other program language

```python
fav = "favorite"
for i in fav:
	print(i, end = ' ')
```



```python
member = ['james','lebrom','kobe','byrant']
for each in member:
	print(each, len(each))
range()		#always use with 'for'
range(5)	#range(5) equal to range(0, 5)   ;    range = [0 , 1 , 2 , 3 ,4]
range(1,10)	#range = [1, 2, ... ,10]
range(1, 10, 2)	#step = 2, range = [1, 3, 5, 7, 9]
list(range())	#print range
```



```python
for i in range(5):
    print(i)
```


20. break , continue
    eg:
    for i in range(10):	#if the number i is even,print(i+2); else->odd, print(i)
21. ​


```python
if i%2 != 0
    print(i)
    continue
i += 2
print(i)
```

21.list

```python
eg:mix = [1, 2.34, 'list', [1,2,3]]#anthing 
empty = []#create an enpty list

append()#add an element to the list
mix.append("Lebron James")#only one parameter
mix.extend(["abc", "def"])#formal parameter is a list too, it can add many elements
mix.insert(1,"ghi")	#2 parameters. insert a element at mix[1],
##element exchange:
temp = mix[0]
mix[0] = mix[1]
mix[1] = temp
##delete element from list
mix.remove('Lebron James')
del mix[2]	#delete element 2
del mix		#delete this list
mix.pop()	#default: delete last element in list
mix.pop(5)	#delete No.5 element in this list
##list slice	列表分片:可以得到一個新的列表（復制）
	#下標: 1 <= i < 3 (包前不包後)
mix[:2]		#0-1, The second element is noe included
mix[1:]		#1-the last one
mix2 = mix[:]		#copy a new list, mix2 = mix
```





22.list comparsion  	#Actually, it's comparing the ASCII value

```python
list1 = [123, 456]
list2 = [234, 456]#list1 < list2
list3 = list1 + list2#list3=[123, 456, 234, 456], it's same like the string opeeration
#the '+' must operate to the same class(same type)
list1 *= 2;	#list1 = [123, 456, 123, 456],類似於復制，原來兩個元素復制一份
```



in   not in

```python
123 in list1	# return true
'abc' not in list2# return falselist[1][1]	#列表中間嵌套列表，獲取第二個列表中的值
```



```python
mix = [1, 2.34, 'list', [1,2,3]]
mix[3][1]	#mix[3][1] = 2Attention!!!
```



24.#顯示list的所有內置方法（BIF）

dir(list)	#look for the function inside list, show all the list's BIF 

```python
list1.count(123)#count(),times
list1.count(123,3,7)#look for the  '123''s location between mix[3] and mix[7]
list1.reverse()# reverse the list,
mix.reverse()#mix = [[1,2,3], 'list', 2.34, 1]
sort()
list.sort()#form small one to the big one,  small -> big
list.sort(reverse = True)#big -> small
```



```python
#unorderable type 'str'
#Attention!!  True,  False
```

The difference between list and tuple(列表和元組的區別)

```python
# eg1:
tuple1 = (1, 2)
tuple2 = (3, 4)
tup3 = (tuple1 + tuple2)
print tup3
# eg2:
tuple1 = (1, 2, 3, 4 )
insert into tuple
tuple1 = tuple1[:2] + (5,) + tuple1[2:]
#1.元組的元素無法修改，但是可以進行組合(tuple與list非常相似，但是tuple一旦初始化就無法修改)
#2.當元組中只含有一個元素時，需要加一個逗號來消除歧義
	#3.因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
# eg3:
tuple1 = ('a', 'b', ['x', 'y'])
tuple1[2][0] = 'A'
tuple1[2][1] = 'B'
tuple1		#tuple中含有list,list中的元素又可以修改了
```

26.str 		#string

```python
str1 = 'i love you'##相關BIF中文解釋:https://fishc.com.cn/forum.php mod=viewthread&tid=38992&extra=page%3D1%26filter%3Dtypeid%26typeid%3D403
str1.capitalize()#The first character must captialize
str1.casefole()	#all turn into lower case
str1.center(width)#Let the string at center of width
str1.center(40)#center of 40 
str1.count('abc',3,7)#Search for the time of 'abc' from 3 to 7
str1.count('abc')
str1.endswith('u')#If string ends with 'u', return True, else return false
str1.endswith('you')
str1.endswith('u',3,7)
str1.expandtabs()#Expand the tab '\t' key
eg:str1 = "i\tlove\tyou.
str1.expandtabs(10)#return:i	  love 		you.
find(sub[,start,[end]])    #find sun in the string,from start to end;

eg:str1.find('you')#return: 7
index(sub[,start[,end]])#find a string in str1 

#return index or error
#index()與find()都是查找字符串中時候存在一個字符(串)，不同的是：如果不存在，index會拋出一個異常，ValueError

str1.index('sub')#return :ValueError: substring not found
isalpha()	#if the element of string is all alpha(zi mu) return True, else:False
isalnum()	#if the element of string is all alpha or number return:True, else: False
str1.isalnum()	#return false,casuse '\t'
isdecimal()	#if the string only have number, return True, else False.
isdigit()	#is number return True,else False
islower()	#If the string elements are all lower case,return True.
isnumeric()	#all numeric character,return True
isspace()	#There are only space string between two words, return True.
istitle()	#all of the begining character is captial,other  is lower case.
join(sub)	#enter the string bet ween characters
str1 = 'abc'
str1.join("123")#result:1abc2abc3abc
ljust(width)	#left :  zuo dui qi
rjust(width)	#right:	  you dui qi	
lower()		#tranform all characters into lower case
upper()		#into upper case
strip()		#delete all space at both forward and backward sides
lstrip()	#drop all space at the left side of string
eg:str1 = ["\t\t\tabc"]				#
        str1.lstrip()	#return:abc
                        rstrip()	#right
                        partition(sub)	#search for sub in this string,and then transform this string into 3 				#strings;	if not found,Nothing did	
                        eg:str1 = "i love you."
                            str1.partition('l')#return:('i ','l','ove you')
                            replace(old,new[,count])#relace the old string with new one,if count is defined,count <= count

                            ```
                            #return a new string
                            ```

                            rfind(sub[,start[,end]])
   rindex(sub[,start[,end]])#[] zhong wei xuan tian nei rong 
   rjust(width)
   rpartition(sub)	#from right side
   rstrip()
   split(sep = None,maxsplit = -1)#default:Split string with space '\0',

   ```
   	#return a list []
   ```

   eg:str1.split()	#return: ["i", "love", "you"]	
   splitlines()	#split string with '\n'
   starstwith(sub[,start[,end]])
   swapcase()	#change the case: captial <-> lower case
   title()		#return the Title style
   eg:str1 = "i love you"
   str1.title()	#return: ("I Love You")
   translate(table)# to get table -> str1.maketrans('a', 'b')

   ```
   	# transform 'a' into 'b' in string
   ```

   eg:str1.translate(str1.maketrans('a', 'b'))
   zfill(width)	#return the string, width ,black location fill with zero; right you dui qi

eg:
str1 = "i love you."
str1.title().split()	#方法的重復調用
```




27. """string's format"""	#字符串的格式化
    eg1:"{0} love {1}".format("I","you")#return: I love you

    key words parameter:#關鍵字參數
    eg2:"{a} love {b}".format(a = "I", b = "you")#return: I love you
    eg3:'{0:.1f}{1}'.format(27.568,'GB')	#return
    		#':' is the begin signal of string's format,":"字符串格式開始標志
    		#.1f(保留一位定點數)

28.%c  %d  %s
'%c %c %c' % (97, 98, 99)
'%d + %d = %d' % (4, 5, 4+5)
'%#o' % 10		#return 0o12

29. The relation between list,tuppel and string: All of them can found element through index.
    eg:str1 = "i love you"
    list(str1)
    list	#return list = ['i', 'l','o','v','e','y','o','u']
    min(list)#return i
    max(list)
    sum(list)
    sum(list, 8)#sum(list) + 8
    sorted()
    reversed()#return a iterator object
    eg:
    numbers = [1, 2, 3, -100, 56]
    list(reversed(numbers))	#return:[56, -100, 3, 2, 1]
    enumerate()#return a iterator too, 用于将一个可迭代对象组合成一个 index 和 元素的组合的形式
    eg:
    list(enumerate(numbers))#return: [(0, 1), (1, 2), (2, 3), (3,100), (4,56)]	, add a index
    eg2:
    li = [100, 101, 102, 103, 104, 105]
    for ix in enumerate(l):
    print(ix, li[ix]) # (0, 1), (1, 2), (2, 3), ...


zip()			#return a literator too
eg:
a = [1, 2, 3, 4, 5]
b = [1, 3, 5, 7, 9, 11, 13]
zip(a, b)		#return: [(1, 1), (2, 3), (3, 5), (4, 7), (5, 9)]

30:The founction to get maximum element in this list:
tuple1 = (1, 2, 3, 4, 5)
max = tuple1[0]
for each in tuple1:
	if max < each:
		max = each
print(max)

31.define a function:
eg1:No parameter
def MyFirstFunction():		#define a function,name - 大駝峯
	print('a\n')
	print('b\n')
	print('c\n')
eg2:
def Add(num1, num2):
	result = num1 + num2
	print(result)

32.parameter & argument
key words parameter or default parameter
eg1:
Add(num1 = 1, num2 = 2)
eg2:default parameter
def SaySome(name = 'Litte fish', words = 'Let the program change the world!'):		##單引號內部爲函數參數默認值
	print(name + '->' + words)
SaySome()		#return:Litte fish->Let the program change the world!
eg3:
SaySome(name = 'James', words = 'You are loser.')	
			#return:James->You are loser.
eg4:
SaySome('A', 'B')	#return: A->B

33.shou ji can shu
eg1:
def Test(*params):
	print('The length of parameters is:', len(params));	#Why add ';' ???
	print('The second parameter is:', params[1]);
test(1, 'abc',3,4,1.23,10)

eg2:With other parameter
def Test(*params, exp = 8)		#In this case, We'd better give a default value to exp
	print('The length of parameters is:', len(params), exp);
	print('The second parameter is:', params[1]);

33.funcion:
eg:
def back():
	return [1, 1.23, 'abc']		#return 1, 1.23, 'abc' is OK
back()
eg:
def Price():
	a = float(input("Please the price:"))
	discount = float(input("Please enter the discount:"))
	print("You need to pay:", discount * a)

34. varible: global varible, local varible

    34.'global'#全部變量
    eg1:
    count = 5
    def change():
    count = 10
    change()
    print(count)	#return: 5，函數內部的count是一個局部變量，和外面的count不一樣，如果想對全局變量操作則 -> 加上global val

eg2:
def change()
	global count	#必須先申明，再對全局變量賦值
	count = 10
change()
print(count)		#return: 10

35. inner function	#內嵌函數
    eg1:
    def Function1():
    print("Function1 was get.")
    def Function2():
    	print("Function2 was get.")
    Function2()
    eg2:
    i = 1
    def fun1():
    print('fun1 was called.')
    print(i)
    def fun2():
    	global i
    	i = 2
    	print('fun2 was called.')
    	print(i)
    	def fun3():
    		global i
    		i = 3
    		print('fun3 was called.')
    		print(i)
    		def fun4():
    			global i
    			i = 4
    			print('fun4 was called.')
    			print(i)
    		fun4()
    	fun3()
    fun2()
    fun1()

    36. 閉包		#closure
        eg1:
        def FunX(x):
        def FunY(y):
        return x * y
        return FunY
        eg2:
        def FunX():
        x = 5
        def FunY():
        x *= x			#This will cause a error,
        			#solution: add 'nonlocal x' before 'x*=x'
        return x
        return FunY

eg3:
##閉包測試1,裝飾器的本質就是閉包
def Maker(name):
	print(name)
	def fun1(age, height, weight):
		age += 1
		height += 1
		weight += 1
		print(age, height, weight)
	return fun1#閉包的實現方式1：直接調用
maker = Maker('libai')
maker(100, 200, 300)

eg4:
def Maker(step):	#包裝器
	num = 1
	def fun1():
		nonlocal num
		num += step
		print(num)
	return fun1

j = 1
fun2 = Maker(3)			#<class 'function'>
while(j < 5):
	fun2()			#調用內部函數四次，輸出：4， 7， 10， 13
	j += 1			#可以看出，Maker()的局部變量num=1以及傳入的參數step都被記憶了下來
				#所以才有：1+3=4; 4+3=7; 
##比較容易理解的方式
fun2 = Maker(3)
fun2()		#4
fun2()		#7
fun2()		#10
		#...

maker = Maker('libai')（1， 2， 3）	#調用方式2

37. lambda  			#ni ming han shu , lambda biao da shi
    			#return a funciont object
    eg:
    def add(x, y):
    return x + y
    add(1, 2)

    g = lambda x, y : x + y	
    g(1, 2)			#return 3

    37. filter()		#2 argument, return the True ,list type
        filter(None, [1, 0, 'False', False, True, 'True'])#return the list object
        list(filter(None, [1, 0, 'False', False, True, 'True']))#list to print them

#arugument is function
eg:
def odd(x):
	return x % 2		#return function is True,When the number is odd, return 1,print
temp = range(1)
result = filter(odd, temp)
list(result)			#return: [1, 3, 5, 7, 9]

eg:Accomplish this function through lambda
list(filter(lambda x : x%2, range(10))) 	##return: [1, 3, 5, 7, 9],range(10) = range(0, 10)
						#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
						#range(1, 3) = [1, 2]

38. map()		##映射
    eg:
    result = map(lambda x : x * 2, range(3))	#return: object type
    list(result)		#return:  [0, 2, 4]

    39.recursion	#遞歸調用
    change the default time:(100)
    import sys
    sys.setrecursionlimit(150)	#100 -> 150
    eg:
    def recursion():
    return recursion()		#default times: 100
    set the recursion times:
    import sys
    sys.setrecursionlimit(1000)
    eg1: 5! = 120
    def f(i):
    if i == 0:
    	return 1
    else:
    	return i * f(i - 1)
    number = int(input("Please enter a  integer:\n"))
    result = f(number)
    print("%d's factorial is %d." %(number, result))
    eg2:Fibonacci
    def f(i):
    if i <= 2:
    	return 1
    else:
    	return f(i - 1) + f(i - 2)

number = int(input("Please enter a number"))
result = f(number)
print("%d's result is :%d" % (number, result))
eg3:hanoi
def hanoi(n, x, y, z):
	if n == 1:
		print(x, '->', z)
	else:
		hanoi(n-1, x, y, z)	#
		print(x, '->', z)
		hanoi(n-1, y, x, z)

40. dictonary  			#字典
    key <-> value		#鍵 <-> 值
    (key, value) pairs	#鍵值對

dict(mapping) -> new dictionary initialized from a mapping object's
 |      

eg1:				#use index(索引)
brand = ["LiNing", "Nike", "adidas"]
slogan = ['Noting is impossible', 'Just do it.', 'everything is possible']
print("adidas's slogan is : ", slogan[brand.index("adidas")])		#index

eg2:
dict1 = {"LiNing":'Noting is impossible', "Nike":'Just do it.'}			#dictionary 									
							#da kuo hao	
print("LingNing's slogan is :", dict1['LiNing'])	#key -> value
eg3:
dict2 = {1:'one', 2:'two', 3:'three'}
or:
dict2 = dict((('1',one), ('2',two), ('3',three)))	#key, value
or:
dict2 = dict(1 = 'one', 2 = 'two', 3 = 'three')		#fu zhi fang shi
or:
dict2 = dict('1' = 'one', '2' = 'two', '3' = 'three')
Add element to the dictionary:
dict2['4'] = 'four'		#This way like the vim open file on linux, if don't have ,create 					#one
dict2[4] = 'four'		#dictionary, you give the 'key', it will return the 'value' to you.-----mapping
				#通過鍵來索引相應的值
41.
fromkeys(...)
dict.fromkeys(s[,v]) 	#new dict with keys from S and values equal to v (v defaults to None)
dict1 = dict.fromkeys(range(10),"hello")
keys()			#visit the dict----------keys(),values(),items()
values()
items()
dict1.keys()		#dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
dict1.values()
dict1.items()		#dict_items([(0, 'Fuck'), (1, 'Fuck'),..., (8, 'Fuck'), (9, 'Fuck')])
eg:
for each in dict1.items():
	print(each)			#return:(0, 'fuck'),.....

43. member operator: in  , not in	#cheng yuan zi ge cao zuo fu
    11 in dict1		#return false
    #clear the dictionary
    clear()
    dict1.clear()		#return: dict1 = {}, You would better use clear
    copy()
    dict2 = dict1.copy()	#build a new area , It's different from '='		
    eg:
    a = {1:’one’, 2:’two’, 3:’three’}
    b = a			#浅拷贝,id(b) = id(a)
    c = a.copy()		#深拷贝，新开辟一块内存，id(c) != id(a)
    pop()
    dict1.pop(2)	#delete key'2' and it's value
    popitem()	#randomly delete a item
    setdefault()
    dict1.setdefault(5)#set default key
    update()	#insert a dictionary to another dictionary
    eg:
    b = {4 : 'four', 5 : 'five'}
    dict1.update(b)	#dict1 = {1 : 'one', 2 : 'two',...,5 : 'five' }
    ###if the key '4' and '5' exist already, It will change the key's value(4 and 5).

44.
dict2[1]			#return  one

45. set			#集合, gather	- unique
    >> num2 = {1, 2, 3, 4, 5}#define 
>>> num2
>>> {1, 2, 3, 4, 5}
>>> type(num2)
>>> <class 'set'>			#set's type

gather = set([1, 2, 3, 3, 2, 1])
gather				#return: {1, 2, 3}, 	wei yi
eg:## qu chong fu 
num1 = [1, 1, 2, 2, 3, 3]
num2 = list(set(num1))

46. gather's BIF list:
    add()
    remove()

    frozenset		#不可變集合
    num1 = frozenset([1, 1, 2, 2, 3, 4])
    num1		#return: {1, 2, 3, 4}

47. file's input and output
    open('','')
    eg:
    f = open('/home/qz/Desktop/test.txt')
    ####Must close the file after use it.###
    f.close()
    f.read()
    f.readline()		#only read one row
    f.tell()		#return the location of bookmark(shu qian)
    f.seek(offset, from)		#change the location of file pointer
    eg:
    f.seek(0, 0)		#pian yi offset ge wei zhi from from location
    48.list(f)
    			#crate a new list through f file
    			#return:['abcdefg\n', 'higklmn\n', 'opq\n', 'rst\n', 'uvwxyz\n']
    eg:
    f = open('/home/qz/Desktop/test.txt', 'a+')#read and write mode,add string at the end of 
    eg1:
    for eachlline in (list(f)):#This will create a large list, Therefor, It's not a good way
    print(eachline)
    eg2:
    for each_line in f:	#Officially standard way
    print(each_line)
    f.write()		#write a string to the file, cover the old data

    f.writelines()	#add a new string to the file from the location of bookmask
    f.close()
    eg2:
    f = open('/home/qz/Desktop/test.txt', 'a+')#a-write mode; + - write&read mode
    f.seek(0, 0)		#At the begin of the file
    f.tell()
    f.write('hello')
    f.read()
    f.close()		#close


49.    #Error chat_record file
       		#P30 you hen da de wen ti


50.module		#mo kuai
import random
secret = random.randint(1, 10)

51.OS = Operating System		#IOS = iphone Operating System
		# file operating
Home = /home/qz
Desktop = /home/qz/Desktop
getcwd()			#return current path
chdir('/home/qz/Desktop/python/')	#os.getcwd()
				# '.' - current path, '..' - last path
os.listdir(path='.')
os.listdir('.')
os.listdir('..')
os.mkdir()
os.mkdir('/home/qz/Desktop/new')	#creat the 'new' file
os.makedirs('/home/qz/Desktop/new/old/new/old')		#di gui chuang jian duo ge 
os.rmdir('/home/qz/Desktop/new')	#delete one file
os.removedirs('/home/qz/Desktop/new/old/new/old')	#di gui shan chu duo ge 

os.system('firefox')			#open the firefox browser
os.curdir		#current directory
os.listdir(os.curdir)	#  = os.listdir('.')	

52.import os.path
os.path.basename('/home/qz/Desktop/python/new/hello.txt')	#return: hello.txt
os.path.dirname('/home/qz/Desktop/python/new/hello.txt')#return: '/home/qz/Desktop/python/new'
os.path.join()		#connect the direction
os.path.split('/home/qz/Desktop/python/new/test.txt')	#split the direction and filename
eg:
list = path.split('/home/qz/Desktop/python/new/new.txt')
list[0]			##return:'/home/qz/Desktop/python/new'
list[1]			##return:'test.txt'
os.listdir(list[0])	#show other file in the same directory 	

getatime()		#leatest visit time
getctime()		#create time
getmtime()		#modify time
eg:
t = os.path.getctime('/home/qz/Desktop/new/new.txt')	#return:1581596017.4306374
import time
time.localtime(t)	#show the current time
exists()
isbas()
isfile()
islink()
samefile(path1, path2)	#judge whether the path ponint to the same file. return: True, False

53.import pickle
pickle.dump()
pickle.load()
eg:
> os.getcwd()			##'/home/qz'
> >> os.chdir('/home/qz/Desktop/new/')
> >> os.getcwd()			##'/home/qz/Desktop/new'

>>> pickle_file = open('my_pickle.pkl', 'wb')	#creat my_pickle.pkl file
>>> pickle.dump(my_list, pickle_file)
>>> pickle_file.close()
>>> pickle_f = open('my_pickle.pkl', 'rb')
>>> list2 = pickle.load(pickle_f)
>>> pickle_f.close()
>>> print(list2)
>>> [1, 2.34, 'abc', [5, 6, 7]]

54.try except
try:
	xxx
except OSError as reason:
	yyy			#chu cuo yuan yin
eg1:	
try:
	sum = 1 + '1'		# TypeError
	f = open('1.txt')	#1.txt is not exist, so this move will report Error -> OSError
	print(f.read())
	f.close()
except OSError as reason:	#Error reason -> as reasion
	print('File Error happened\n, The reason is :' + str(reason))
except TypeError as reason:
	print('Type Error happened\n, The reason is :' + str(reason))
eg2:
try:
	f = open('1.txt')
except (OSError, TypeError) as reason:
	print('A errosr happened, reason:' + str(reason))
eg3:
try:
	f = open('1.txt', 'w')
	f.write('I love you .')
	1/0
	f.close()			#A error happened, f.close() will nor do
except (OSError, ZeroDivisionError) as reason:
	print('A error happened, reason is :' + str(reason))
finally:
	f.close()			#無論如何都會被執行的操作

eg4:
try:
	f= open('/home/qz/Desktop/test.py', 'w')
	f.write('i love you')
	sum = 1 + 'a'			#TypeError
	f.close()
except (OSError, ValueError, TypeError) as errReason:
	print('戳錯啦！\n錯誤的原因是：' + str(errReason))
finally:
	f.close()			#無論如何都要執行的操作，文件可以被保存

55. else
    当while中有break语句打断时，else不会执行。

当while中没有被break语句打断时，else就会执行。

while:
	xxx
else:
	xxx
eg1:
try:
	int('123')	#ValueError
except (ValueError) as reason:				#reason is't str type
	print('A error happened:' + str(reason))
else:
	print('No error!')

eg2:
i = 3
while i > 0:
	print(i)
	i -= 1
else:				#without 'break'
	print('No')		#return: 3 2 1 No

eg2:
for i in range(3):
	print(i)
else:				#without 'break'
	print('No')		#return: 0 1 2 No
eg3:
for i in range(3):
	if(i == 3):
		break
	print(i)
else:
	print('execute Else T_T')	##not 'break',execut 'else'

eg4:
for i in range(3):
	if(i == 2):
		break
	print(i)
else:
	print('execute Else T_T')	##execute, 'break',No   'else'	

eg5:
i = 5
while i > 0:
	if i == 3:			#i=3的時候程序跳出，不會執行else
		print(i)
		break	
	print(i)
	i -= 1
else:
	print('正常執行結束')

eg6:try-except-else
try:
	print('測試開始')
	1/0
	print('測試結束')
except (OSError, ZeroDivisionError) as errorReason:
	print('出錯啦\n出錯的原因是：' + str(errorReason))
else:
	print('測試完美運行結束')



56. with
    eg1:				#auto close the file
    try:
     with open('/home/qz/Desktop/new/new.txt', 'w') as f:
             for each in f:
                     print(each)
    except OSError as reason:
     print('An error occurred:' + str(reason))


57. EasyGui module  		#You can write a module by yourself
    install EasyGui steps:
    pip3 install EasyGui
    https://sourceforge.net/projects/easygui/ 
    tar -zxvf easygui_ 0 .98.tar.gz
    sudo python3 setup.py install#error:No module named '_tkinter', please install the python3-tk package
    sudo apt install python3-tk
    eg:
    import eastgui
    easygui.msgbox('Enter')	# return a box

import easygui as g
g.msgbox('Enter')
#2 aruguments
g.msgbox('parameter', 'title')

choices = ['yes', 'no']
reply = g.choicebox('Would you like to ?', choices  = choices)

58. def msgbox(msg="(Your message goes here)", title="", ok_button="OK"):
    eg:
    g.msgbox(msg = 'i love you', title = 'love', ok_button = 'me to0')


ccbox(msg='Shall I continue?', title=' ', choices=('Continue', 'Cancel'), image=None)
g.ccbox(msg = 'dou you love me ?',title = 'love', choices = ('Yes', 'No'))	#return 1 or 0
eg:
ask = g.ccbox(msg = 'dou you love me ?',title = 'love', choices = ('Yes', 'No'))
if ask == 1:
	g.msgbox('Ok')
elif ask == 0:			#elif = else if, more easy type
	sys.exit(0)

buttonbox(msg='', title=' ', choices=('Button1', 'Button2', 'Button3'), image=None, root=None)
eg:
str1 = g.buttonbox(msg = 'Do you lobe me?', choices = ('Yes', 'No', "No"))
type(str1)	#return : class 'str'
str1		#return : 'Yes'

indexbox(msg='Shall I continue?', title=' ', choices=('Yes', 'No'), image=None)	
						#return  0 or 1
						#The first button return 0
boolbox(msg='Shall I continue?', title=' ', choices=('Yes', 'No'), image=None)
						#opposite whith 'indexbox()'
						##如果第一个按钮被选中则返回 1，否则返回 0。
image 		##image 赋值，这是设置一个 .gif 格式的图像（注意仅支持 GIF 格式
eg:
msg = 'do you love me ?'
title = 'love'
choices = ('yes', 'No', 'I don\'t know')
g.choicebox(msg = msg, title = title, choices = choices)

multchoicebox()	# many choices

enterbox()
enterbox(msg='Enter something.', title=' ', default='', strip=True, image=None, root=None)
​	
intergerbox()
passwordbox()
multpasswordbox()
textbox()
codebox()

diropenbox()
diropenbox(msg=None, title=None, default=None)
eg:
g.fileopenbox(msg = 'Please choose', title = 'Files', default= '/home/qz/Desktop')
fileopenbox()
fileopenbox(msg=None, title=None, default='*', filetypes=None)
filesavebox()
### Error  excute
exceptionbox()
eg:
try:
	print('i love you .')
	int('abc')		#Error occured
except:
	g.exceptionbox()	#g.exceptionbox(),show the error information

59. 对象 = 属性（静态，变量） + 方法（函数）
    eg:
    class Turtle:		## class  lei,tong guo lei lai ding yi dui xiang
    ## shu xing
    color = 'green'
    weight = '10'
    gender = 'male'
    ​	
    ## fang fa
    def climb(self):
    	print('pa')
    def run(self):
    	print('pao')
    def eat(self):
    	print('chi')
    ##create a object  -> OO, object oriented, mian xiang dui xiang
    tt = Turtle()

list1 = list[1, 2, 3]
list1.sort()
list1.append(4)		#Actually, list is an object too.

60. ji cheng
    class MyList(list):#ji cheng list
    pass
    list1 = MyList()# a object
    list1.append(1)	#ji cheng list.append()
    list1	#return [1]

    61. self		#c++'s this pointer
        eg:
        class Ball:
         def setName(self, name):
             self.name = name
         def kick(self):
             print('My name is: %s' % self.name)
        class Ball:
         def setName(self, name):
             self.name = name
         def kick(self):
             print('My name is: %s' % self.name)
>>> a = Ball()
>>> a.setName('Football')
>>> a.kick()
>>> My name is: Football

62. python's magic way  -> 		#Magic way1; __init__
    eg:
    __init__(self, parm1, parm2,...)
    eg:
    class Ball:
    ##modify __init__ method , chong xie '__init__' fang fa (han shu)
    def __init__(self, name):
    	self.name = name
    def kick(self):
    	print('My name is: %s' % self.name)

63. private member and the key to get the private member
    '__' means private
    eg:
    class Student:
    __name = 'lebron James'
    def getName(self):
    	return self.__name			#
    a = Student()
    a.__name	##Error
    a.getName()#right way to get the private member '__name'

64. fu lei(ji lei)
    eg:
    class Parent:
    def hello(self):
    	print('wo shi ba ba')
    class Son(Parent)	#ji cheng
    pass
    a = son()
    a.hello()	#get Parent's inner methods

65.
import random as r
eg:Fish and Shark
class Fish:
	def __init__(self):
		self.x = r.randint(0, 10)		#a random integer between 0 - 10
		self.y = r.randint(0, 10)
	def move(self):
		self.x -= 1
		print('My location is :(%d, %d)' % (self.x, self.y))
class GoldFish(Fish):
	pass
class Corp(Fish):
	pass
class Shark(Fish):
	def __init__(self):
		##Key1: Fish.__init__(self)
		super().__init__()		##tui jian shi yong 
		print('I\'m hungry.')

#'Shark' object has no attribute 'x'

66. duo lei ji cheng
    class Base1:
     def fool1(self):
             print('a')

class Base2:
     def fool2(self):
             print('b')

class C(Base1, Base2):		#duo chong ji cheng, shen yong
     pass			#Python shell zhong bu neng tong shi ding yi duo ge lei 
... 
c = C()
c.fool1()
				#return: a
c.fool2()
				#return: b

67. zu he  
    eg:
>>> class Fish:
>>> ...     def __init__(self, x):
>>> ...             self.num = x
>>> ##
>>> class Turtle:
>>> ...     def __init__(self, y):
>>> ...             self.num = y
>>> ##
>>> class Pool:
>>> ...     def __init__(self, x, y):		#lei de zu he
>>> ...             self.turtle = Turtle(x)			
>>> ...             self.fish = Fish(y)
>>> ...     def print_num(self):
>>> ...             print('turtle:%d, Fish:%d.' % (self.turtle.num, self.fish.num))  #diao yong fa fa 
>>> p = Pool(1, 10)
>>> p.print_num()
>>> turtle:1, Fish:10.

68. __bases__	'多继承'		#Magic wday  -> "dir(list)" :show all magic way
    多继承 的实现就会创建新类，有时，我们在运行时，希望给类A添加类B的功能时，也可以利用python的元编程特性，__bases__属性便在运行时轻松给类A添加类B的特性
    #mei you zhao dao '__bases__', why ?

69. mix-in
    #https://fishc.com.cn/forum.php?mod=viewthread&tid=48888&extra=page%3D1%26filter%3Dtypeid%26typeid%3D403	

    69.bang ding	#
    '__dict__'	#look for the object's attribute
    		#(1)C.__dict__	(2)c.__dict__
    eg:
    class C:
    pass
    C.__dict__	#return all
    c = C()		
    c.__dict__	#return: {}, an empty dictionary

70. del
    del C		#delete C object

    71. issubclass()	#check whether is subclass,
        class A:
        eg:
        pass
        class B(A):
        pass
        issubclass(B, A)#return True,   B shi A de zi lei
        issubclass(B, B)#return True
        issubclass(A, object)#return: True, object is 
        a = A()

        isinstance(a, A)#True	,a shi A de shi li
        isinstance(a, (A, B, C))#True

        72. some BIF	#dui 'dui xiang' cao zuo
            hasattr(object, name)#has attribute , return: True or False
            setattr(object, name[,default])#set attribute
            getattr(object, name[default])#get attribute
            delattr(object, name)#delete the attribute
            eg:
            class Base:
            def __init__(self, x)
            self.x = x
            b = Base('abc')#  dir(__builtins__) show all BIF(nei zhi han shu)
            hasattr(b, 'x')#return : True
            setattr(b, 'x', 'abc')
            getattr(b, 'x', 'Not found')#default,If Not found the attribut 'x', execute 'default'
            delattr(b, 'x')

73.
property() 
class C:
	def __init__(self, size = 10):
		self.size = size
	def setSize(self, value):
		self.size = value
	def getSize(self):
		return self.size
	def delSize(self):
		del self.size
	x = property(getSize, setSize, delSize)
c = C()
c.x = 19
c.size		#return: 19
c.getSize	#return: 19

74. _init__		#------Magic way2
    ###Note: __init__ can't return, cause Error
    eg:
    class Rectangle:
    def __init__(self, x, y):
    	self.x = x
    	self.y = y
    def getArea(self):
    	return self.x * self.y
    r = Rectangle(1, 2)
    r.getArea()	#return 2

##magic way3 __new(class[,])

75.#构造函数 and 析构函数
__init__			#构造函数，对象被创建马上执行(lei de shi li) one time
__del__			#析构函数,si wang de shi hou zhi xing yi ci
eg1:
class CapStr(str):
	def __new__(cls, string):		#dui str de __new__ chong xie
		string = string.upper()
		return str.__new__(cls, string)
eg2:
class C:
	def __init__(self):			#gou zao han shu
		print('__init__ was created.')
	def __del__(self):			#xi gou han shu
		print('__del__was created.')
c = C()
c1 = c
del c1
del c		#return: __del__was created.

76. '__new__'		
    #我们首先得从__new__(cls[,...])的参数说说起，__new__方法的第一个参数是这个类，而其余的参数会在调用成功后全部传递给__init__方法初始化，这一下子就看出了谁是老子谁是小子的关系。'__new__':jiang jun, '__init__': xiao bai xing
    eg1.:
    class A(object):
    def __init__(self):
    	print('__init__')
    def __new__(cls):
    	print('__new__')
    	return super().__new__(cls)		#bu dong le ???
    def __del__(self):
    	print('__del__')
    a = A()	# '__new__' earlier than '__init__'
    del a	# '__del__'

    76. suan shu yun suan 	##yun suan fu chong zai, shi xian dui xiang de xiang jia 
        eg:
        class New_Int(int):# ji cheng lei,		dir(int),__add__,__sub__...
        def __add__(self, other):
        return int.__add__(self, other)		#chong xie add
        def __sub__(self, other):
        return int.__sub__(self, other)
>>> a = New_Int(3)
>>> b = New_Int(5)
>>> a + b
>>> 8
>>> a - b
>>> -2

76. operator Overload		#lei de yun suanf fu
    			#class's operator
    eg:
    class NewInt(int):
    def __radd__(self, other):
    	return int.__radd__(self, other)
    a = NewInt(5)
    a + 1 	#return: 6
    1 + a	#return 6

76.(1)
__repr__		##print message when run object,  __repr__------magic way4
eg:
class A:
	def __repr__(self):
		return("123456789")
a = A()
a		#return: 123456789
(2)__str__
eg:
class A:
	def __str__(self):
		return('abc')
	__repr = __str__		#zhu yi suo jin  -> SyntaxError



77.			##p45 -> hui tou kan
      eg:Write a timer class
      import time as t

t.localtime()
lei de ding zhi ------ji shi qi lei		## Timer class

78.    #attribute's magic way
       setattr()
       getattr()
       delattr()	#dui dui xiang(object) jin xing cao zuo
       eg1: 'property() function'
       ##如果 c 是 C 的实例化, c.x 将触发 getter,c.x = value 将触发 setter ， del c.x 触发 deleter。
       ##如果给定 doc 参数，其将成为这个属性值的 docstring，否则 property 函数就会复制 fget 函数的 docstring（如果有的话）。
       class C:
       def __init__(self, size = 10):	#when default was set  ->  c = C()  / c = C(1)	
       	self.size = size
       def getSize(self):
       	return self.size
       def setSize(self, value):
       	self.size = value
       def delSize(self):
       	del self.size
       x = property(getSize, setSize, delSize, 'What\'s ')		# property method, zi dong shi 								#bie ,diao yong 
       c = C()
       c.x		# getattr()
       c.x = 5		#setattr()
       del c.x		#delattr()

       getattr(c, 'size', 'Not Found')	#reutrn: 5
       setattr(c, 'size', 10)
       getattr(c, 'size')	#return: 10
       delattr(c, 'size')	#key2: del c.size

## Magic way
__setattr()__
__getattr()__
__delattr()__
eg2:
class C(object):
	def __getattribute__(self, name):		#when attribute exist
		print('getattribute')
		return super().__getattribute__(name)	#super() function
	def __getattr__(self, name):
		print('getattr')		#when attribute does not exist
	def __setattr__(self, name, value):
		print('setattr')
		super().__setattr__(name, value)
	def __delattr__(self, name):
		print('delattr')
		super().__delattr__(name)
>>> c =C()
>>> c.x			#c.x attribute does not exist
>>> getattribute
>>> getattr
>>> c.x = 1		#c.x exist
>>> setattr
>>> c.x
>>> getattribute
>>> 1
>>> del c.x
>>> c.x
>>> getattribute
>>> getattr
>>>

79. shu xing de fang wen		#get attribute
    __getattribute__() -> __getattr__()
    eg:
    class Rectangle():
    def __init__(self, width = 0, height = 0):
    	self.width = width
    	self.height = height
    ##def __setattr__
    def __setattr__(self, name, value):	
    	if name == 'square':
    		self.width = value
    		self.height = value
    	else:
    		##self.name = value-----Recursion Error
    		#super().__setattr__(name, value)	#key1:Use super() function
    							#key2:__dict__
    		self.__dict__[name] = value
    ##calculate the area of rectangele
    def getArea(self):
    	return self.width * self.height
    r = Rectangle()
    r.square = 10
    r.getArea()	#We can use r.__dict__ to view the details of this object

r2 = Rectangel(3,5)
r2.getArea()

r3 = Rectangle()
r3.width = 3
r3.height = 5
r3.getArea()

80.  discriptor		
     #一般来说，一个描述器是一个有“绑定行为”的对象属性(object attribute)，它的访问控制被描述器协议方法重写。这些方法是 __get__(), __set__(), 和 __delete__() 。有这些方法的对象叫做描述器。
     __get__
     __set__
     __delete__
     eg:
     class MyDescriptor:
     def __get__(self, instance, owner):
     	print('getting', self, instance, owner)
     def __set__(self, instance, value):
     	print('setting', self, instance, value)
     def __delete__(self, instance):
     	print('deleting', self, instance)
     class Test:
     x = MyDescriptor()

81. write our own property() function

    82. rong qi	-> ding zhi xu lie,
        ##can't change -> must include: len(),getitem()
        ##can change -> setitem(), delitem()
        eg1:
        class CountList:
        def __init__(self, *args):# '*' can shu ge shu qu que ding
        			# The number of arguments is not clear
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)			
        			#dict.fromkeys(),range(),len(), 
        def __len__(self):
        return len(self.values)
        def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]
        c1 = CountList(1, 3, 5, 7, 9)
        c2 = CountList(2, 4, 6, 8, 10)
        c1[1]
        c2[1]
        c1[1] + c[2]
        c1.values

eg2:
class MyList:				#key <-> values, MyList type, our own class
	def __init__(self, *args):
		self.keys = [i for i in args]
		self.values = {}.fromkeys(range(len(self.keys)), 'abc')	# 'dict' type
	def __len__(self):
		return len(self.keys)
	def __getitem__(self, key):
		return self.values[key]

eg3:
class MyList:
	def __init__(self, *args):
		self.keys = [i for i in args]
		self.values = {}.fromkeys(range(len(self.keys)), 'default')
	def __getitem__(self, key):
		return self.values[key]
	def __setitem__(self, key, value):
		self.values[key] = value
	def __delitem__(self, key):
		del self.values[key]
a = MyList(1, 2, 3, 4)
a.values
print(a[1])	#get
a[1] = 'ABCDE'
del a[3]	#key and value all were deleted, others not change

eg4:
class Tag:
    def __init__(self):
        self.change={'python':'This is python',
                     'php':'PHP is a good language'}
     
    def __getitem__(self, item):
        print('调用getitem')
        return self.change[item]
     
    def __setitem__(self, key, value):
        print('调用setitem')
        self.change[key]=value

a=Tag()
print(a['php'])
a['php']='PHP is not a good language'
print(a['php'])

83. iterator : iter()   next()			# die dai qi
    such as: list, tuple, string, dict...
    eg1:
    for i in string 'abcde':
    print(i)
    eg2:
    dict1 = {'a':'i love you', 'b':'No'}
    for i in dict1:
    print(i, dict1[i])
    print('%s -> %s.' % (i, dict1[i]) )

    #### iter() and next()	##########
    eg1:
    string = 'abcde'
    it = iter(string)
    next(it)	#StopIteration

eg2:
list1 = [1, 2, 3.14, 'abc', [1,2,3]]
it = iter(list1)
next(it)

eg3:
while True:
	try:
		each  = next(it)		
	except StopIteration:			#next() -> StopIteration
		break
	print(each)				#

84. iterator's magic way  : __iter__,  __next__
    eg:
    class Fibs:
    def __init__(self):
    	self.a = 0
    	self.b = 1
    def __iter__(self):
    	return self			# return a iterator object
    def __next__(self):
    	self.a, self.b = self.b, self.a + self.b
    	return self.a
    (1)test
    fibs = Fibs()# lei de shi li
    for each in fibs:
    print(each)
    (2)test
    fi = Fibs()
    for each in fi:
    if each < 20:
    	print(each)
    else:
    	break
    eg3:control the iterator times with n
    class Fibs:
    def __init__(self, max = 10):
    	self.max = max
    	self.a = 0
    	self.b = 1
    def __iter__(self):
    	return self		# return a iterator object
    def __next__(self):
    	self.a, self.b = self.b, self.a + self.b
    	if self.a > self.max:
    		raise StopIteration
    	return self.a
    fibs = Fibs()
    for each in fibs:
    print(each, end = ' ')	#rang shu chu bu zi dong huan hang 

    85. generator -> yield		#sheng cheng qi
        eg:
        def myGen():		#bi xu ding yi wei han shu
        print("generator was get.")
        yield 1
        yield 2




83. List comprehension 			##lie biao tui dao shi 
    eg:
    list1 = [i for i in range(1)]
    list2 = [i**2 for i in range(1, 11)]
    list3 = [i**2 for i in range(1, 11) if i%2 == 0]









82. create our own module  #dierctory: /usr/lib/python3.5  -> sitepackage
    			#/home/qz/.local/lib/python3.5/site-packages
    import sys
    sys.path


83. 	Learn a new module
     #look for the information and discription of a new module
     eg:
     import timeit
     (1)timeit.__doc__
     print(timeit.__doc__)
     (2)dir(timeit)#search the BIF of this module
     (3)timeit.__all__#get the most important function that can be recalled by the out fun
     ##Note:
     from time import *#only timeit.__all__ can be used
     (4)timeit.__file__	#We can the the source file of this module
     (5)help(timeit)


























































































































































































































​	









 
























































































































