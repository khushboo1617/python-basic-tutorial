#break statement.
a=5
x= int(input("enter no."))
i=1
while i<=x:

    if i>a :
        print("exit.")
        break

    print("hii")
    i+=1


#pass statements.
    for i in range(1,20):

        if i%3==0:
            pass  #is used for skip the statements, it's diff from 'continue' statement.

        else:
            print(i)

