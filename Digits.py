#sum of digits
#multiplication of digits
#reverse the number

class Numeric:  
    def sum_num(self,n):
        s=0
        while(0<n):
            s = (n%10)+s
            n = n//10
        print(f"sum ofthe digit:{s}")
        
    def mul_num(self,n):
        mul=1
        while(0<n):
            mul = (n%10)*mul
            n = n//10
        print(f"Multiplication of the digit:{mul}")

    def rev_num(self,n):
        rev=0
        while(0<n):
            rev = (n%10)+ rev*10 
            n=n//10
        print(f"Reverse of the digit:{rev}")
ob=Numeric()
ob.sum_num(int(input("Enter the n number:")))
ob.mul_num(int(input("Enter the n number:")))
ob.rev_num(int(input("Enter the n number:")))
