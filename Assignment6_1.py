#Demo class contains two instance variables as no1 ,no2. 
#That class contains one class variable as Value. 
#There are two instance methods of class as Fun and Gun which displays values of instance variables. 
#Initialise instance variable in init method by accepting the values from user. 
 
#After creating the class create the two objects of Demo class as 
#Obj1 = Demo(11,21) 
#Obj2 = Demo(51,101) 
#Now call the instance methods as 
#Obj1.Fun() 
#Obj2.Fun() 
#Obj1.Gun() 
#Obj2.Gun() 
 #############################################################################################


class Demo:
    value=11
    def __init__(self,no1,no2):
        self.i=no1
        self.j=no2
        print("Inside Constructor")
        
    def __del__(self):              #Destructor
        print("Inside Destructor")
        
    def fun(self):
        print("inside Fun")
        print(self.i)
        print(self.j)
        
    def gun(self):
        print("inside Gun")
        print(self.i)
        print(self.j)
               
def main():
    obj1=Demo(11,51)
    obj2=Demo(51,101)
    print("value of i from obj1",obj1.i)            #accesing instance members
    print("value of i from obj2",obj2.i)
    print("value of i from obj1",Demo.value)        #accesing class members
    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()

if __name__=="__main__":
    main()
        