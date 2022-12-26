#break

#creating a vending machine

n=int(input("How many cans do you want?" ))

available=10 #no. of cans available in the vending machine

for i in range (1,n+1):
    if (i>available):
        print("Out of stock")
        break
    
    print ("Can", i)
    
