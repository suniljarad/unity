#
#Step 1 : Understand the problem statement
#step 2 : Write the Algorithm
#Step 3 : Decide the programming language
#Step 4 : Write the Program
#Step 5 : Test the Written Program

#program statement:
#Create on module named as Arithmetic which contains 4 functions as Add()for addition,Sub()for subtraction,Mult()for multiplication and Div()for division.
# All functions accepts two parameters as number and perform the operation.

 ##################################################################################################
#Algorithm
#Start 
#Accept first number  as no1
#Accept second number as no2
#perform all operation (addition,subtraction,multiplication,division) given as two parameters as number
#Display addition,subtraction,multiplication,division on Screen
##End

 ####################################################################################################
#Function Name: Display()
#input :Integer,Integer
#output:Integer
#Description:Display addition,subtraction,multiplication,division on Screen
#Author: Sunil Bhagwan Jarad
#Date:19/2/2021
 ####################################################################################################
 
#import Arithmetic
#import Arithmetic as AR
#from Arithmetic import Add,Sub,Mult,Div
from Arithmetic import *
def main():
     print("enter first number:")
     value1 = int(input())

     print("enter second number:")
     value2=int(input())

     ret1 = Add(value1,value2)
     print("Addition of {} and {} is {}".format(value1, value2, ret1))

     ret2 = Sub(value1,value2)
     print("Substraction of {} and {} is {}".format(value1,value2,ret2))
     
     ret3 = Mult(value1,value2)
     print("Substraction of {} and {} is {}".format(value1,value2,ret3))
     
     ret4 = Div(value1,value2)
     print("Substraction of {} and {} is {}".format(value1,value2,ret4))


if __name__ =="__main__":
    main()


