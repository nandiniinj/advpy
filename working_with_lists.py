'''working with lists'''

nums=[13,20,42,30,80,88,40,60,10,70,13]
print(nums)
print(nums[5])
print(nums[-2])
print(nums.count(13))

names=['parth','jay','ira','kopal','ram','om','dev','ravi']
print(names)
print(nums[:4])
print(nums[3:])

'''lists can consists elements of different data types'''
values=[201,'abcd',30,'pqrs','xyz',50,405,62,'qwerty','kilo',602,'loki']
print(values)

'''lists can consists of more than one lists'''
mil=[nums, names]  
print(mil)

'''lists are mutable'''
nums.append(90) #adds the element at the end
print(nums)

nums.insert(2,91)  #adds the element 91 at index 2
print(nums)

nums.remove(40)   #removes the given element
print(nums)

nums.pop(2)   #removes the element at index 2
print(nums)

nums.pop() #if no value is given it removes the last element
print(nums)

del nums[4:]   #removes sequence of elements
print(nums)

del names[1:3]
print(names)

del values[:5]
print(values)

nums.extend([82,43,74])  #adds more than one elements
print(nums)


'''mathematical operations'''
print(min(nums))
print(max(nums))
print(sum(nums))

nums.sort()
print(nums)
