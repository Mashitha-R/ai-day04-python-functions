
""" FUNCTIONS AND PARAMETERS """

def greet():
    print("hello")
greet()


#ARGUMENTS

def sum(a,b):    #positional arguments
    print(f"the sum of {a+b} ")
sum(12,12)
sum(45,25)



def hello(name,age): 
    print(f"your name is {name} and age is {age}")

hello("Mashitha",26)
hello(age=22,name="Banu") #keyword argument


def sum(a,b=40):          #default arguments
    print(f"the sum is {a+b}")
sum(12)
sum(12,36)


#revision

#check pallindrome or not

def pallindrome(st):
    rev=""
    for i in range(len(st)-1,-1,-1):
        rev=rev+st[i]
    if rev==st:
        print(f"{st} is a pallindrome")
    else:
        print(f"{st} is not a pallindrome")
    
pallindrome("mashitha")
pallindrome("NAMAN")



#return

def hello():
    return"how are you"
print(hello())


