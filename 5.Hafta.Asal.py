import math
x=int(input("bir sayi giriniz: "))

def asal(k):
    b=[]

    z=0
    if(k%2==0):

        print("asal degildir")
        a = k
        while (a % 2 == 0):
            a = a // 2
            b.append(2)
        for j in range(3,x,2):
            if (a%j==0):
                while(a%j==0):
                    a=a//j
                    b.append(j)
        print(" carpanlari", b)
    else:
        for i in range(3,k//2,2):
            if(k%i==0):
                print("sayi asal degildir")
                a=k
                z=z+1
                for j in range(3,x,2):
                    while (a%j==0):
                        a=a//j
                        b.append(j)
                print(" carpanlari",b)
                break
        else:
            print("asaldir")


asal(x)