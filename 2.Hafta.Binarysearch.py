def mysearchselection(my_array):
    swapsayisi=0
    for i in range(len(my_array)-1,0,-1):
        positionofmax=0
        for location in range(1,i+1):
            #print("j:",location,"i:",i,end="\n")
            if(my_array[location]>my_array[positionofmax]):
                positionofmax=location
        temp=my_array[location]
        my_array[location]=my_array[positionofmax]
        my_array[positionofmax]=temp
        swapsayisi+=1

    print("swapsayisi:",swapsayisi)   
    return

my_arr=[21,54,85,6,52,23]

print("------------------")

print("dizi:",my_arr)

print("------------------")

mysearchselection(my_arr)

print("sıralanmış dizi:",my_arr)

def my_binary_search(my_sorted_array,item):
    first=0
    last=len(my_sorted_array)-1
    found=False
    while(first<=last and not found):
        midpoint=(first+last)//2
        #print("last - first:",last,first)
        
        if(my_sorted_array[midpoint]==item):
            found=True
        else:
            if(item<my_sorted_array[midpoint]):
                last=midpoint-1
            else:
                first=midpoint-1

    return found,items,midpoint


my_binary_search(my_arr,21)

print("binary search:",my_binary_search(my_arr,21))
