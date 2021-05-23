#program to check whether the given number is prime or not.

n = int(input("enter a no."))

for i in range(2,n) :
    if n % i==0 :
        print("not a prime no.")
        break
else:
    print("prime..")