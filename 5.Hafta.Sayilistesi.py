liste=[4,-3,2,-1,-2,6,-5]
def sayi(list):
    n=len(list)+1
    max=0

    for i in range(2,n):
        for j in range(0,(n-i)):
            top=0
            a=0
            while(a!=(i-1)):
                top=top+list[j+a]
                a=a+1
            if(top>max):
                max=top
    return max
print("En buyuk toplam: ",sayi(liste))
