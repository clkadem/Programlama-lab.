import random

#boyutu n olan dizi üret 

def generate_an_array(n):
    #n=10
    my_array=[]
    for i in range(n):
        s=random.randint(0,100)
        my_array.append(s)
    return my_array

print("-------------------")
#a)dizi üzerinde arama yapan fonsiyonu
#b)sıralanmış dizi üzerinde ikili arama yapan fonksiyon

def my_search_c(array_2,item):
    found= False
    indis=-1
    step=0
    for i in range(len(array_2)):
        step=step+1
        if array_2[i]==item:
            found=True
            indis=i
            break
    return (found, indis,step)

array_1=generate_an_array(8)
print("dizi üret: ",array_1)

print("dizide eleman arama: ",my_search_c(array_1,array_1[3]))

print("-------------------")

my_arr_1=generate_an_array(10)

print("dizi 2")
for i in range (len(my_arr_1)):
    print(i,":",my_arr_1[i], end=" ")
    

print("\n-------------------")

def my_bubble_sort (my_array):
    for i in range(len(my_array)-1,0,-1):
        for j in range(i):
            if(my_array[j]>my_array[j+1]):
                t=my_array[j]
                my_array[j]=my_array[j+1]
                my_array[j+1]=t
    print(my_array)
print("sıralanmış dizi2:")
my_bubble_sort(my_arr_1)


