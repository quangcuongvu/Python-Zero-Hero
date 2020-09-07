t=(1,2,3,4,5)
print(type(t))
for n in t:
    print (n,end=" ")

t=(1,3,5,7,8,9,3526,90)
i=0
for n in t:
    print(i, end=" ")
    i=i+1
print("\n=======")
t=(1,3,5,7,9)
for n in t:
    print("Python -hihi")

l=[10,20,30,40,50,60,70,80,90,100]
for n in l:
    print(n, end=" ")

print("\n======")
d={'Tuan':'23','huy':'25','Hoang':'22'}
print(d,type(d))
for key in d:
    print(d[key])
    print(key)

print("\n=============")
ss="Vu Quoc Tuan"
for c in ss:
    if  (c !=" "):
        print (c*10)