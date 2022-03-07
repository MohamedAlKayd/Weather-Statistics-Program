# Mohamed Mahmoud
# Weather Statistics Program

# - Start of the Program -

real=[]
final=[]
newer=[]
mylist = []
n =input("Enter readings: ")
mylist.append(n)
while n!="stop":
    n =input("Enter readings: ")
    if n=="stop":
        continue
    mylist.append(n)
for i in range(len(mylist)):
        variable=mylist[i].split()
        for j in range(len(variable)):
            newer=variable[j]
            final.append(newer)
for i in range(len(final)):
    var=float(final[i])
    real.append(var)
    for j in range(len(real)):
        if real[j]>50 or real[j]<-50:
            real.remove(real[j])
            
num=0
for i in range(len(real)):
    num+=1
print("Average termperature:",(round((sum(real))/num,1)))
 
print("Min 3 temperatures:")

real=sorted(real)

print(round(real[0],1))
print(round(real[1],1))
print(round(real[2],1))
print("Max 3 temperatures:")
print(round(real[-1],1))
print(round(real[-2],1))
print(round(real[-3],1))

# - End of the Program -