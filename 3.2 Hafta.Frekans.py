def frekans_tablosu(list):
    frekans_dict={}
    for item in list:
        if(item in frekans_dict):
            frekans_dict[item]=frekans_dict[item]+1
        else:
            frekans_dict[item]=1

    return frekans_dict




def my_frekans(list):
    frekans_list=[]
    for i in range (len(list)):
        s=False
        for j in range (len(frekans_list)):
           if(list[i]==frekans_list[j][0]):
               frekans_list[j][1]=frekans_list[j][1]+1
               s=True
        if(s==False):
            frekans_list.append([list[i],1])
    return frekans_list


liste=[2,3,2,5,8,3]
print("liste:",liste)
result=frekans_tablosu(liste)
print("freksns (sözlük):",result)
print("frekans (liste):",my_frekans(liste))