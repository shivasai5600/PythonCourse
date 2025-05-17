courses = ['History', 'Math', 'Physics', 'CSE']
course_1 = ['No', 'cat', 'bad']
print(courses)
courses.append('ECE')                    #append method
print(courses)
courses.insert(0,'YES')    #INSERT method
print(courses)
courses.extend('Noasd')                  #extend method
print(courses)

print(course_1)
courses.extend(course_1)
print(courses)

courses.insert(1,course_1)
print(courses)
courses.remove('Math')       #remove moethod
print(courses)
courses.pop()                #pop method
print(courses)
popped = courses.pop()
print(popped)
print(courses)

courses.reverse()            #reverse method
print(courses)

course_1.sort()              #sort method
print(course_1)

course_1.sort(reverse=True)
print(course_1)

sorted_courses = sorted(course_1)
print(sorted_courses)

nums = [1,23,45,46,3,6]
print(min(nums))
print(sum(nums))
print(max(nums))
print(nums.count(46))
print(nums.index(3))
print(5 in nums)
print(6 in nums)

for i in nums:
    print(i)
for index, cor in enumerate(nums,start=1):
    print(index,cor)
nums_es = ','.join(course_1)
print(nums_es)
nums_es = '-'.join(course_1)
print(nums_es)

cs_cous = {'History', 'Math', 'Phy', 'Com'}
art_cous ={'History', 'Math', 'Sci', 'Tel'}
print(cs_cous.intersection(art_cous))
print(cs_cous.difference(art_cous))
print(cs_cous.union(art_cous))
