message = 'hello world'
me = 'Hello\'s World'
ms = "hello's world"
ma = """this is the world of    
full of surprises """        #here it gives in multiple lines  bcz you written in multiple lines, otherwise single itgives

print(message)
print(me)
print(ms)
print(ma)
print(len(message))       # length of the string
print(len(me))
print(message[3])    #printing the location or index value of the character in the word
print(message[0:4])     #prints  particular characters what u want
print(message[6:])
print((message[:8]))
print(message[-1])            #last character of the word starts with -1


          # slicing the ists and strings


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]
print(my_list)
print(my_list[:])
print(my_list[1:9:2])
print(my_list[:9:-1])       #empty array
print(my_list[-2:1:-3])
print(my_list[::-1])        # reverse the list numbers

sample = 'http://googled.com'
print(sample)

#reverse the url        using the slicing method
print(sample[::-1])
print(sample[7:])       # printind without the http://
print(sample[7:-4])      #printing wiyhout the http:// or .com

print(me.upper(),me.lower())     #here we are using the upper method
print(me.count('/'))             #count method, we should pass atleast 1 argument in the method
print(me.count("\'"),me.count('l'))
print(me.find('e'), me.find('llo'), me.find('star'))   #find method

message = message.replace('world', 'universe')    #replace method
print(message)

       #concatination of strings two methods
greeting = 'Hello'
name = 'Hanu'
print(greeting+' '+name, greeting+', '+name)      #concating the strings
print('{}, {}. Welcome!'.format(greeting,name))   #palceholders and format method to concat
print(f'{greeting} it is {name.upper()}')

person = {"name":'sai', "age":23 , 'class':17}
dc = 'my name is {}, and i\'m {} old'.format(person['name'],person['age'])
dc1 = 'my name is {[name]}, and i\'m {[age]} old'.format(person,person)
dc2 = 'my name is {0[name]}, and i\'m {0[age]} old'.format(person)
dc5 = 'my name is {name}, and i\'m {age} old of Calss {class}'.format(**person)

l = ['hanu', 23]
dc3 = 'my name is {0[0]}, and i\'m {0[1]} old'.format(l)
print(dc)
print(dc1)
print(dc2)
print(dc3)
print(dc5)

dc4 = 'my name is {name}, iam {age} old'.format(name='sai', age=25)
print(dc4)

te = 'h1'
text = 'this the headline'
cd = '<{0}>{1}<{0}>'.format(te,text)
print(cd)

import datetime                                                              #date time methods
my_date = datetime.date(2025, 3, 8)
print(my_date)

my_time = datetime.time(1,20,45)
print(my_time)

my_datetime = datetime.datetime(2025,3,8,1,21,32)
print(my_datetime)

sentence = '{0:%B %d, %Y} is a day of {0:%A} with day number {0:%j}'.format(my_datetime)  #format of date if we write Capital letters display full word, small-short word
print(sentence)

tes = 'shivasai'
target = 's'
for i in range(len(tes)):
    if tes[i] == target:
        print(i)


text = 'shivasai'
target = 's'

for i, char in enumerate(text):
    if char == target:
        print(i)

text1 = [1,2,3,4,2]
target = 2
# c=0
for i in range(len(text1)):
    if text1[i] == target:
        print(i)
        break
        # c+=1
    # if c==2:
    #     print(i)


oj = []
print(oj, id(oj))
oj.append(1)
print(oj, id(oj))
oj.insert(2,"das")
print(oj)
oj.insert(2,"da")
print(oj)
oj.insert(2,"das")
print(oj)
oj.insert(1,"as")
print(oj)
oj.remove(1)
print(oj)
oj.remove("das")
print(oj)
oj.pop()
print(oj)
ns = [1,2,34,23,1,4,2,4,5,3]
ns.remove(1)
print(ns)
ns.pop()
print(ns)
ns.pop(0)
print(ns)
ns.clear()
print(ns,type(ns),id(ns))
bd = ns.clear()
print(bd,type(bd))
fdjk = [1,"sdf",2,6,5,6]
del fdjk[1]
print(fdjk)
del fdjk[:2]
print(fdjk)
del fdjk[:2:1]
print(fdjk)
li = [2,3,4]
l2 = li.copy()
print(li,id(li),l2,id(l2))
l3 = li
li.append(5)
print(li,id(li),l3,id(l3))

                                     # 1 method
# print("enter the two values")
# v = int(input())
# m = int(input())
# print("add of {} and {} is {}".format(v,m,v+m))
#                                      # 2 method
# c1 = float(input("Enter the first value:"))
# c2 = float(input("Enter the second value:"))
# print("mul (%0.2f,%0.2f) is %0.2f" %(c1,c2,c1*c2))
#                                     # 3 method
# c3 = float(input("Enter the first value:")) * float(input("Enter the second value:"))
# print("mul is {}".format(c3))

                                   # 4 method
# print("mul is {}".format(float(input("Enter the first value:")) * float(input("Enter the second value:"))))

# import calendar
# print(calendar.month(2025,6))
# print(calendar.monthcalendar(2025,12))
# print(calendar.calendar(2025))

import random
print(random.randrange(1,10))

a = int(input("Enter the value for tablenumber:"))
for i in range(0,11):
    print("{} X {}= {}".format(a,i,a*i))

g,f,f1= 10,34,4
res,res1,res2 = g << 3, f << 2, f1 >> 2
print(res,res1,res2)


f1 = 4           #=> 0100 in binary
f2 = 5           #=> 0101 in binary
ff = f1 | f2     #=> add above two 0101
             # 0 1 0 0                   0 1 0 1
             # 0 1 0 1  add              1 0 0 1  here 0 + 1 adding will get 1
             # 0 1 0 1  output           1 1 0 1
print(ff)

print(f1 & f2, type(f1&f2))          #0 1 0 0
                                     #0 1 0 1      add here 0 + 1 adding will get 0
                                    # 0 1 0 0

print(~4)   # explanation ~(0 1 0 0 + 1)
                        # -(0 1 0 0 + 1)
                        # - 0 1 0 0
                        #   0 0 0 1  bitwise OR(|)
                        #   0 1 0 1  output           formula= -(n+1)

print(f1^f2)  # explanation     0 1 0 0
                     #          0 1 0 1
                              # 0 0 0 1     same are zero, difference is 1
print(10^4)

#============================  identity operators is ,is not =================================
a =10
b= 10
li = [1,2]
li2 = [1,2]
print(a,b,li,li2,id(a),id(b),id(li),id(li2))
print(a == b,li ==li2,id(a),id(b),id(li),id(li2))
print(a is b,li is li2,id(a),id(b),id(li),id(li2))
#======================================  conditional statements if,if else,if elif else,============
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
    #=============================== Loops conditions ================
a = int(input("Enter the number:"))
n=100
while a<= n:
    print("numbers: {}".format(a))
else:
    print("wrong")
