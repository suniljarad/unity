

def ChkPrime(List):
    prime=[]
    sum=0
    for num in List:
        c=0
        for i in range(1,num):
            if(num%i==0):
                c=c+1                             
                
        if(c==1):
            prime.append(num)
           
            print("prime Number List:",prime)
            sum=sum+num
            print("Addition of Prime numbers is:",sum)
            