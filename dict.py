student = {'name':'virat', 'age':25, 'courses':['phy','sce']}
print(student)
print(student['name'])
print(student['courses'])
print(student.get('phone'))                              #get method
print(student.get('phine','Not found'))
print(student.get('courses'))
print(student.get('courses'))

student['phone'] = 'sefdzxc'
print(student)
student['name'] = 'kohli'
print(student)

student.update({'name':'Punna', 'age':24})               #update method
print(student)

del student['age']                                      #delete method
print(student)

popped = student.pop('name')                           #pop method
print(student)
print(popped)

print(student.keys())                                    #keys method
print(student.values())                                  #values method
print(student.items())                                   #items method

for key in student:                                      #key in for loop
    print(key)

for key, value in student.items():
    print(key,value)
