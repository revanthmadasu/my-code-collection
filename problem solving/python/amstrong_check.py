a=int(input())
b=int(input())
arm_count=0
for i in range(a,b+1):
    num=i
    n=len(str(i))
    i=str(i)
    total=0
    123
    for dig in i:
        total=total+int(dig)**n 
    # armstrong case
    if total==num:
        arm_count += 1
        if len(str(total))<1:
            print(total,end="")
        else:
            print(total,end=" ")
if arm_count == 0:
    print("-1")
    