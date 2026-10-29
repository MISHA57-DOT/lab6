numbers = [2, 3, 2, 5, 3, 2, 5, 8]
dic={}
for num in numbers:
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1
print(dic)