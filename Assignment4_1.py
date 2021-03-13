

#program statement:
    #Display the power of two using lambda function

#Algoritham:
#1.Input n
#2.Input P
#3.Use lambda function
#4.Display Result

 ####################################################################################################
#Function Name: lambda function
#input :Integer
#output:integer
#Description:Display the power of two using lambda function
#Author: Sunil Bhagwan Jarad
#Date:4/3/2021
 ####################################################################################################
#name=lambda parameters:body
#lambda function
print("Enter the how many terms want to display")
n=int(input())
print("Enter the Power Number")
p=int(input())
power=list(map(lambda i:p**i,range(n)))

def main():
    
    for i in range(n):
        print("{} raised to power {} is {}".format(p,i,power[i]))
       
    
      
if __name__ == "__main__":
    main()







