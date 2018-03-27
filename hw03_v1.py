dict1 = {}
s=input('輸入字元:')
for i in s:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1

for i in dict1:
    number=dict1.get(i)
    print("'", i, "': ", number)
    number=dict1.get(i)
