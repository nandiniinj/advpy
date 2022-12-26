'''Given a list of integers
    print only the first integer that is a multiple of 5
    else print "Not Found" only once.'''


# This is a For- Else block:---


lst=[12,26,14,25,74,80,44] #contains 2 numbers divisible by 5


for i in lst:

    if i%5==0:
        
        print(i)
        break     #if you want only the first output fulfilling the condition

    '''
    else:
        print("Not found") #this will print "Not found" for every iteration
        '''

else:

    print("Not Found")





print("----------------------------------------------------------------------")




lst=[12,26,14,23,74,81,44]   #no number divisible by 5


for i in lst:

    if i%5==0:
        
        print(i)
        break     #if you want only the first output fulfilling the condition

    '''
    else:
        print("Not found") #this will print "Not found" for every iteration
        '''

else:

    print("Not Found")
